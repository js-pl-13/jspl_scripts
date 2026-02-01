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
#include <vector>

// Структура для хранения вычисленных данных
struct LocatorData {
    MString badLocFullPath; // Путь к исходному локатору
    MString fixedLocName;   // Имя для нового локатора
    MPoint finalPos;        // Вычисленная позиция
    MQuaternion rotation;   // Вычисленное вращение
    int faceId;             // ID полигона
};

class fixLocators : public MPxCommand
{
public:
    fixLocators() {}
    virtual ~fixLocators() {}

    virtual MStatus doIt(const MArgList& args);
    virtual MStatus redoIt();
    virtual MStatus undoIt();
    virtual bool isUndoable() const { return true; } // Включаем поддержку Ctrl+Z

    static void* creator();

private:
    MString m_meshTransName;
    // Хранилище данных для Redo
    std::vector<LocatorData> m_taskData;
    // Список созданных нод для Undo (локаторы и констрейны)
    MStringArray m_createdNodes;
};

void* fixLocators::creator()
{
    return new fixLocators;
}

MString d2s(double val)
{
    char buffer[64];
    // Используем snprintf для безопасности
#ifdef _WIN32
    _snprintf_s(buffer, 64, _TRUNCATE, "%.6f", val);
#else
    snprintf(buffer, sizeof(buffer), "%.6f", val);
#endif
    return MString(buffer);
}

MStatus fixLocators::doIt(const MArgList& args)
{
    MStatus status;
    m_taskData.clear();

    if (args.length() != 1)
    {
        MGlobal::displayError("Usage: fixLocators <mesh_transform_or_shape>");
        return MS::kFailure;
    }

    MString meshArg = args.asString(0, &status);
    if (!status) return status;

    MSelectionList meshList;
    if (!meshList.add(meshArg))
    {
        MGlobal::displayError("Object not found: " + meshArg);
        return MS::kFailure;
    }

    MDagPath meshDagPath;
    meshList.getDagPath(0, meshDagPath);
    m_meshTransName = meshDagPath.fullPathName();

    // 1. Поиск шейпа (не intermediate)
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
            break;
        }
    }
    if (!shapeFound) meshDagPath.extendToShape();

    MString meshShapeName = meshDagPath.fullPathName();
    MFnMesh fnMesh(meshDagPath, &status);
    if (!status) return status;

    // 2. Инициализация Intersector
    MObject meshObj = meshDagPath.node();
    MMeshIntersector intersector;
    status = intersector.create(meshObj);
    if (!status) return status;

    MMatrix meshInclusive = meshDagPath.inclusiveMatrix();
    MMatrix meshInverse = meshInclusive.inverse();

    MBoundingBox bbox = fnMesh.boundingBox();
    MPoint headCenterLocal = bbox.center();
    MPoint headCenterWorld = headCenterLocal * meshInclusive;

    // 3. Сбор локаторов
    MGlobal::executeCommand("select \"*_pos\"");
    MSelectionList selList;
    MGlobal::getActiveSelectionList(selList);

    MPoint locatorsCenter(0, 0, 0);
    int locCount = 0;
    {
        MItSelectionList iterCalc(selList, MFn::kTransform);
        for (; !iterCalc.isDone(); iterCalc.next())
        {
            MDagPath locPath;
            iterCalc.getDagPath(locPath);
            MFnTransform fnLoc(locPath);
            if (strstr(fnLoc.name().asChar(), "_fixed") != NULL) continue;
            MMatrix locMat = locPath.inclusiveMatrix();
            MPoint pos(locMat(3, 0), locMat(3, 1), locMat(3, 2));
            locatorsCenter += pos;
            locCount++;
        }
    }
    if (locCount > 0) locatorsCenter = locatorsCenter / static_cast<double>(locCount);

    // 4. Создаем временную ноду CPM (только для расчета!)
    MString cpmName = "temp_fixLocators_CPM_Calc";
    MGlobal::executeCommand("if(`objExists " + cpmName + "`) delete " + cpmName);
    MGlobal::executeCommand("createNode closestPointOnMesh -n " + cpmName);
    MGlobal::executeCommand("connectAttr -f \"" + meshShapeName + ".worldMesh[0]\" \"" + cpmName + ".inMesh\"");

    // 5. ОСНОВНОЙ РАСЧЕТ (Заполняем m_taskData)
    MItSelectionList iter(selList, MFn::kTransform);
    for (; !iter.isDone(); iter.next())
    {
        MDagPath locPath;
        iter.getDagPath(locPath);
        if (!locPath.hasFn(MFn::kTransform)) continue;

        MFnTransform fnLoc(locPath);
        MString badLocName = fnLoc.name();

        if (strstr(badLocName.asChar(), "_fixed") != NULL) continue;

        LocatorData data;
        data.badLocFullPath = locPath.fullPathName();
        data.fixedLocName = badLocName + "_fixed";

        // Математика векторов
        MMatrix locMat = locPath.inclusiveMatrix();
        MPoint locPos(locMat(3, 0), locMat(3, 1), locMat(3, 2));

        fnLoc.getRotation(data.rotation, MSpace::kWorld);

        MVector dirVec = locPos - locatorsCenter;
        if (dirVec.length() > 0.0001) dirVec.normalize();
        else dirVec = MVector(0, 0, 1);

        MPoint virtualTargetWorld = headCenterWorld + (dirVec * 0.15);
        MPoint virtualTargetLocal = virtualTargetWorld * meshInverse;

        MPointOnMesh pointInfo;
        status = intersector.getClosestPoint(virtualTargetLocal, pointInfo);

        MPoint finalPosLocal = status ? pointInfo.getPoint() : headCenterLocal;
        data.finalPos = finalPosLocal * meshInclusive; // World Space

        // Получаем Face ID через ноду
        MString setPosCmd = "setAttr \"";
        setPosCmd += cpmName + ".inPosition\" ";
        setPosCmd += d2s(data.finalPos.x) + " ";
        setPosCmd += d2s(data.finalPos.y) + " ";
        setPosCmd += d2s(data.finalPos.z);
        MGlobal::executeCommand(setPosCmd);

        int fId = 0;
        MGlobal::executeCommand("getAttr " + cpmName + ".closestFaceIndex", fId);
        data.faceId = fId;

        // Сохраняем задачу
        m_taskData.push_back(data);
    }

    // Удаляем временную ноду (расчет окончен)
    MGlobal::executeCommand("delete " + cpmName);

    // Вызываем Redo для создания объектов
    return redoIt();
}

MStatus fixLocators::redoIt()
{
    MStatus status;
    m_createdNodes.clear(); // Чистим список перед новым созданием

    for (size_t i = 0; i < m_taskData.size(); ++i)
    {
        const LocatorData& data = m_taskData[i];

        // 1. Создаем Локатор
        MStringArray result;
        // Удаляем если существует (на случай повторного запуска без undo)
        MGlobal::executeCommand("if(`objExists \"" + data.fixedLocName + "\"` ) delete \"" + data.fixedLocName + "\"");

        MGlobal::executeCommand("spaceLocator -n \"" + data.fixedLocName + "\"", result);
        if (result.length() == 0) continue;

        MString createdName = result[0];
        m_createdNodes.append(createdName); // Запоминаем для Undo

        MSelectionList tempList; tempList.add(createdName);
        MDagPath fixedPath;
        tempList.getDagPath(0, fixedPath);
        MFnTransform fnFixed(fixedPath);
        MString fixedFull = fixedPath.fullPathName();

        // 2. PointOnPoly Constraint
        MString popCmd = "import maya.cmds as cmds; result = ";
        popCmd += "cmds.pointOnPolyConstraint('";
        popCmd += m_meshTransName + ".f[" + (MString() + data.faceId) + "]', '";
        popCmd += fixedFull + "', mo=True, weight=1.0); result"; // Возвращаем результат

        MStringArray constraints;
        status = MGlobal::executePythonCommand(popCmd, constraints);
        if (status && constraints.length() > 0) {
            for (unsigned int k = 0; k < constraints.length(); k++) m_createdNodes.append(constraints[k]);
        }

        // 3. Установка позиции (Direct Plugs)
        MPlug tx = fnFixed.findPlug("translateX", &status);
        if (status) tx.setDouble(data.finalPos.x);

        MPlug ty = fnFixed.findPlug("translateY", &status);
        if (status) ty.setDouble(data.finalPos.y);

        MPlug tz = fnFixed.findPlug("translateZ", &status);
        if (status) tz.setDouble(data.finalPos.z);

        fnFixed.setRotation(data.rotation, MSpace::kWorld);

        // 4. Parent Constraint
        MString pcCmd = "import maya.cmds as cmds; result = ";
        pcCmd += "cmds.parentConstraint('";
        pcCmd += fixedFull + "', '";
        pcCmd += data.badLocFullPath + "', mo=True, weight=1.0); result";

        constraints.clear();
        status = MGlobal::executePythonCommand(pcCmd, constraints);
        if (status && constraints.length() > 0) {
            for (unsigned int k = 0; k < constraints.length(); k++) m_createdNodes.append(constraints[k]);
        }
    }

    return MS::kSuccess;
}

MStatus fixLocators::undoIt()
{
    // Удаляем в обратном порядке
    for (int i = m_createdNodes.length() - 1; i >= 0; --i)
    {
        MString node = m_createdNodes[i];
        // Проверяем существование, чтобы не спамить ошибками
        MString cmd = "if(`objExists \"" + node + "\"` ) delete \"" + node + "\"";
        MGlobal::executeCommand(cmd);
    }
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