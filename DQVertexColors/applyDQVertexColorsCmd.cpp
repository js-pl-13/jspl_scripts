#include <maya/MPxCommand.h>
#include <maya/MFnPlugin.h>
#include <maya/MGlobal.h>
#include <maya/MSelectionList.h>
#include <maya/MFnMesh.h>
#include <maya/MColor.h>
#include <maya/MColorArray.h>
#include <maya/MIntArray.h>
#include <maya/MSyntax.h>
#include <maya/MArgList.h>
#include <maya/MStatus.h>
#include <algorithm>
#include <maya/MDagPath.h>
#include <maya/MObject.h>

class ApplyDQVertexColorsCmd : public MPxCommand {
public:
    ApplyDQVertexColorsCmd() {}
    virtual MStatus doIt(const MArgList& args) override;
    static void* creator() { return new ApplyDQVertexColorsCmd; }
    static MSyntax newSyntax();
    static const char* kName() { return "applyDQVertexColors"; }
};

MSyntax ApplyDQVertexColorsCmd::newSyntax() {
    MSyntax syn;
    syn.addFlag("-mesh", "-m", MSyntax::kString);
    syn.addFlag("-colors", "-c", MSyntax::kDouble, MSyntax::kDouble, MSyntax::kDouble); // repeated triples
    syn.addFlag("-verts", "-v", MSyntax::kLong); // repeated integers
    syn.addFlag("-set", "-s", MSyntax::kString);
    syn.addFlag("-merge", "-M", MSyntax::kBoolean); // новый флаг
    syn.useSelectionAsDefault(false);
    syn.enableQuery(false);
    syn.enableEdit(false);
    return syn;
}

MStatus ApplyDQVertexColorsCmd::doIt(const MArgList& args) {
    MStatus status;

    MString meshName;
    MString colorSetName = "dqColorSet";
    bool merge = true; // по умолчанию объединять
    MIntArray vertArray;
    MColorArray colors;

    // --- Парсинг флагов ---
    for (unsigned int i = 0; i < args.length(); ++i) {
        MString token = args.asString(i, &status);
        if (token == "-mesh" || token == "-m") {
            meshName = args.asString(++i, &status);
        }
        else if (token == "-set" || token == "-s") {
            colorSetName = args.asString(++i, &status);
        }
        else if (token == "-merge" || token == "-M") {
            merge = args.asBool(++i, &status);
        }
        else if (token == "-verts" || token == "-v") {
            ++i;
            while (i < args.length()) {
                MString tok = args.asString(i, &status);
                if (tok.length() > 0 && tok.asChar()[0] == '-') { --i; break; }
                int v = args.asInt(i, &status);
                vertArray.append(v);
                ++i;
            }
        }
        else if (token == "-colors" || token == "-c") {
            ++i;
            while (i + 2 < args.length()) {
                MString tok = args.asString(i, &status);
                if (tok.length() > 0 && tok.asChar()[0] == '-') { --i; break; }
                double r = args.asDouble(i, &status);
                double g = args.asDouble(i + 1, &status);
                double b = args.asDouble(i + 2, &status);
                colors.append(MColor((float)r, (float)g, (float)b, 1.0f));
                i += 3;
            }
            --i;
        }
    }

    if (meshName.length() == 0) { MGlobal::displayError("applyDQVertexColors: -mesh required."); return MS::kFailure; }
    if (vertArray.length() == 0) { MGlobal::displayError("applyDQVertexColors: no vertices provided."); return MS::kFailure; }
    if (colors.length() == 0 || colors.length() != vertArray.length()) {
        MGlobal::displayError("applyDQVertexColors: colors missing or count mismatch.");
        return MS::kFailure;
    }

    // --- Получение меша ---
    MSelectionList sel;
    sel.add(meshName);
    MDagPath meshDag;
    status = sel.getDagPath(0, meshDag);
    if (!status) { MGlobal::displayError("applyDQVertexColors: mesh not found."); return MS::kFailure; }
    meshDag.extendToShape();
    MFnMesh fnMesh(meshDag, &status);
    if (!status) { MGlobal::displayError("applyDQVertexColors: failed to get MFnMesh."); return MS::kFailure; }

    // --- Создание colorSet с учетом merge ---
    MStringArray existing;
    fnMesh.getColorSetNames(existing);
    bool hasSet = false;
    for (unsigned int i = 0; i < existing.length(); ++i) {
        if (existing[i] == colorSetName) { hasSet = true; break; }
    }

    if (!merge && hasSet) {
        fnMesh.deleteColorSet(colorSetName);
        hasSet = false;
    }

    if (!hasSet) { fnMesh.createColorSet(colorSetName); }
    fnMesh.setCurrentColorSetName(colorSetName);

    // --- Прогресс окно ---
    MGlobal::executeCommand(
        "progressWindow -title \"Applying DQ Colors\" "
        "-progress 0 "
        "-max " + MString() + vertArray.length() +
        " -status \"Applying vertex colors...\" -isInterruptable true"
    );

    // --- Обработка блоками по 666 вершин ---
    const unsigned int blockSize = 666;
    for (unsigned int start = 0; start < vertArray.length(); start += blockSize) {
        unsigned int end = std::min(start + blockSize, (unsigned int)vertArray.length());

        MIntArray blockVerts;
        MColorArray blockColors;
        for (unsigned int i = start; i < end; ++i) {
            blockVerts.append(vertArray[i]);
            blockColors.append(colors[i]);
        }

        fnMesh.setVertexColors(blockColors, blockVerts);

        // Обновление прогресса
        MGlobal::executeCommand(MString("progressWindow -edit -progress ") + end);

        // Проверка отмены
        MString cancelled;
        MGlobal::executeCommand("progressWindow -query -isCancelled", cancelled);
        if (cancelled == "true") {
            MGlobal::executeCommand("progressWindow -edit -endProgress");
            MGlobal::displayWarning("Vertex color application cancelled by user.");
            return MS::kFailure;
        }
    }

    // Завершение прогресс окна
    MGlobal::executeCommand("progressWindow -edit -endProgress");

    // Включить отображение цветов
    MPlug displayColorsPlug = fnMesh.findPlug("displayColors", false, &status);
    if (status) displayColorsPlug.setValue(true);

    return MS::kSuccess;
}

// --- Plugin entry ---
MStatus initializePlugin(MObject obj) {
    MStatus status;
    MFnPlugin plugin(obj, "dqTools", "1.0", "Any", &status);
    if (!status) return status;

    status = plugin.registerCommand(
        ApplyDQVertexColorsCmd::kName(),
        ApplyDQVertexColorsCmd::creator,
        ApplyDQVertexColorsCmd::newSyntax
    );
    return status;
}

MStatus uninitializePlugin(MObject obj) {
    MStatus status;
    MFnPlugin plugin(obj);
    status = plugin.deregisterCommand(ApplyDQVertexColorsCmd::kName());
    return status;
}
