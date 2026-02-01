#include <maya/MPxCommand.h>
#include <maya/MFnPlugin.h>
#include <maya/MGlobal.h>
#include <maya/MString.h>
#include <maya/MStringArray.h>
#include <maya/MSelectionList.h>
#include <maya/MItSelectionList.h>
#include <maya/MDagPath.h>
#include <maya/MFnMesh.h>
#include <maya/MFnTransform.h>
#include <maya/MFnDagNode.h>
#include <maya/MPlug.h>
#include <maya/MPoint.h>
#include <maya/MVector.h>
#include <maya/MMatrix.h>
#include <maya/MQuaternion.h>
#include <maya/MBoundingBox.h>
#include <maya/MArgList.h>
#include <maya/MMeshIntersector.h>

#include <cstdio>

class fixLocators : public MPxCommand
{
public:
    fixLocators() {};
    virtual MStatus doIt(const MArgList& args);
    static void* creator();
};

void* fixLocators::creator()
{
    return new fixLocators;
}

MString d2s(double val)
{
    char buffer[64];
    snprintf(buffer, sizeof(buffer), "%.6f", val);
    return MString(buffer);
}

MStatus fixLocators::doIt(const MArgList& args)
{
    MStatus status;

    MGlobal::displayInfo("========================================");
    MGlobal::displayInfo("PLUGIN VERSION: v22 (FIXED PYTHON CALLS)");
    MGlobal::displayInfo("========================================");

    // Загружаем nearestPointOnMesh если нужно
    MGlobal::executeCommand("if (!`pluginInfo -q -l nearestPointOnMesh`) catchQuiet(`loadPlugin nearestPointOnMesh`);");

    if (args.length() != 1)
    {
        MGlobal::displayError("Usage: fixLocators <mesh_transform_or_shape>");
        return MS::kFailure;
    }

    MString meshArg = args.asString(0, &status);
    if (!status) return status;

    // Находим меш
    MSelectionList meshList;
    if (!meshList.add(meshArg))
    {
        MGlobal::displayError("Object '" + meshArg + "' not found.");
        return MS::kFailure;
    }

    MDagPath meshDagPath;
    meshList.getDagPath(0, meshDagPath);

    MString meshTransName = meshDagPath.fullPathName();

    // Ищем shape (не intermediate)
    unsigned int numShapes = 0;
    meshDagPath.numberOfShapesDirectlyBelow(numShapes);
    bool shapeFound = false;
    for (unsigned int i = 0; i < numShapes; ++i)
    {
        MDagPath shapePath = meshDagPath;
        shapePath.extendToShapeDirectlyBelow(i);
        MFnDagNode fnNode(shapePath);
        if (!fnNode.isIntermediateObject())
        {
            meshDagPath = shapePath;
            shapeFound = true;
            MGlobal::displayInfo("Using Shape: " + fnNode.name());
            break;
        }
    }
    if (!shapeFound) meshDagPath.extendToShape();

    MString meshShapeName = meshDagPath.fullPathName();
    MFnMesh fnMesh(meshDagPath, &status);
    if (!status)
    {
        MGlobal::displayError("Failed to create MFnMesh");
        return status;
    }

    // Интерсектор в local space
    MObject meshObj = meshDagPath.node();
    MMeshIntersector intersector;
    status = intersector.create(meshObj);
    if (!status)
    {
        MGlobal::displayError("Failed to create MMeshIntersector");
        return status;
    }

    MMatrix meshInclusive = meshDagPath.inclusiveMatrix();
    MMatrix meshInverse = meshInclusive.inverse();

    // Центр bounding box в world
    MBoundingBox bbox = fnMesh.boundingBox();
    MPoint headCenterLocal = bbox.center();
    MPoint headCenterWorld = headCenterLocal * meshInclusive;

    // Собираем все *_pos локаторы (кроме уже *_fixed)
    MGlobal::executeCommand("select \"*_pos\"");
    MSelectionList selList;
    MGlobal::getActiveSelectionList(selList);

    // Считаем средний центр локаторов (для направления)
    MPoint locatorsCenter(0, 0, 0);
    int locCount = 0;
    {
        MItSelectionList iterCalc(selList, MFn::kTransform);
        for (; !iterCalc.isDone(); iterCalc.next())
        {
            MDagPath locPath;
            iterCalc.getDagPath(locPath);
            MFnTransform fnLoc(locPath);
            if (strstr(fnLoc.name().asChar(), "_fixed") != nullptr) continue;
            MMatrix locMat = locPath.inclusiveMatrix();
            MPoint pos(locMat(3, 0), locMat(3, 1), locMat(3, 2));
            locatorsCenter += pos;
            locCount++;
        }
    }
    if (locCount > 0) locatorsCenter = locatorsCenter / static_cast<double>(locCount);

    // closestPointOnMesh нода для faceIndex
    MString cpmName = "temp_fixLocators_CPM_v22";
    MGlobal::executeCommand("if(`objExists " + cpmName + "`) delete " + cpmName);
    MGlobal::executeCommand("createNode closestPointOnMesh -n " + cpmName);
    MGlobal::executeCommand("connectAttr -f \"" + meshShapeName + ".worldMesh[0]\" \"" + cpmName + ".inMesh\"");

    // Основной цикл обработки
    int fixedCount = 0;
    MItSelectionList iter(selList, MFn::kTransform);
    for (; !iter.isDone(); iter.next())
    {
        MDagPath locPath;
        iter.getDagPath(locPath);
        if (!locPath.hasFn(MFn::kTransform)) continue;

        MFnTransform fnLoc(locPath);
        MString badLocName = fnLoc.name();
        MString badLocFull = locPath.fullPathName();

        if (strstr(badLocName.asChar(), "_fixed") != nullptr) continue;

        MMatrix locMat = locPath.inclusiveMatrix();
        MPoint locPos(locMat(3, 0), locMat(3, 1), locMat(3, 2));

        MQuaternion rot;
        fnLoc.getRotation(rot, MSpace::kWorld);

        MVector dirVec = locPos - locatorsCenter;
        if (dirVec.length() > 0.0001) dirVec.normalize();
        else dirVec = MVector(0, 0, 1);

        MPoint virtualTargetWorld = headCenterWorld + (dirVec * 0.15);
        MPoint virtualTargetLocal = virtualTargetWorld * meshInverse;

        MPointOnMesh pointInfo;
        status = intersector.getClosestPoint(virtualTargetLocal, pointInfo);

        MPoint finalPosLocal = status ? pointInfo.getPoint() : headCenterLocal;
        MPoint finalPosWorld = finalPosLocal * meshInclusive;

        // Получаем face index через CPM
        MString setPosCmd = "setAttr \"";
        setPosCmd += cpmName + ".inPosition\" ";
        setPosCmd += d2s(finalPosWorld.x) + " ";
        setPosCmd += d2s(finalPosWorld.y) + " ";
        setPosCmd += d2s(finalPosWorld.z);
        MGlobal::executeCommand(setPosCmd);

        int finalFaceId = -1;
        MGlobal::executeCommand("getAttr " + cpmName + ".closestFaceIndex", finalFaceId);

        // Лог
        MString logMsg = "LOC: " + badLocName + " -> Face: " + (MString() + finalFaceId) +
            "  XYZ: " + d2s(finalPosWorld.x) + ", " +
            d2s(finalPosWorld.y) + ", " + d2s(finalPosWorld.z);
        MGlobal::displayInfo(logMsg);

        // Создаём новый локатор
        MString fixedName = badLocName + "_fixed";
        MStringArray result;
        MGlobal::executeCommand("spaceLocator -n \"" + fixedName + "\"", result);
        if (result.length() == 0) continue;

        MString createdName = result[0];
        MSelectionList tempList; tempList.add(createdName);
        MDagPath fixedPath;
        tempList.getDagPath(0, fixedPath);

        MFnTransform fnFixed(fixedPath);
        MString fixedFull = fixedPath.fullPathName();

        // pointOnPolyConstraint через Python cmds
        MString popCmd = "import maya.cmds as cmds; ";
        popCmd += "cmds.pointOnPolyConstraint('";
        popCmd += meshTransName + ".f[" + (MString() + finalFaceId) + "]', '";
        popCmd += fixedFull + "', mo=True, weight=1.0)";

        if (MGlobal::executePythonCommand(popCmd) != MS::kSuccess)
        {
            MGlobal::displayWarning("pointOnPolyConstraint failed for " + fixedName);
            continue;
        }

        // Устанавливаем позицию после констрейнта
        MPlug tx = fnFixed.findPlug("translateX", &status);
        if (status) tx.setDouble(finalPosWorld.x);

        MPlug ty = fnFixed.findPlug("translateY", &status);
        if (status) ty.setDouble(finalPosWorld.y);

        MPlug tz = fnFixed.findPlug("translateZ", &status);
        if (status) tz.setDouble(finalPosWorld.z);

        fnFixed.setRotation(rot, MSpace::kWorld);

        // parentConstraint через Python cmds
        MString pcCmd = "import maya.cmds as cmds; ";
        pcCmd += "cmds.parentConstraint('";
        pcCmd += fixedFull + "', '";
        pcCmd += badLocFull + "', mo=True, weight=1.0)";
        MGlobal::executePythonCommand(pcCmd);

        fixedCount++;
    }

    // Уборка
    MGlobal::executeCommand("delete " + cpmName);

    MString msg = "Fixed " + (MString() + fixedCount) + " locators (v22)";
    MGlobal::displayInfo(msg);

    MGlobal::executeCommand("select -cl");

    return MS::kSuccess;
}

MStatus initializePlugin(MObject obj)
{
    MFnPlugin plugin(obj, "MayaTools", "2025", "Any");
    return plugin.registerCommand("fixLocators", fixLocators::creator);
}

MStatus uninitializePlugin(MObject obj)
{
    MFnPlugin plugin(obj);
    return plugin.deregisterCommand("fixLocators");
}