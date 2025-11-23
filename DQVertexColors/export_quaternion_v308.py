# -*- coding: utf-8 -*-
import maya.cmds as cmds
import json
import os
import re
import time

"""
---------------------------------------------------------------------------------------------------------------
DQ Blend Weights Tool for Autodesk Maya
=======================================

This script provides a set of tools for working with Dual Quaternion (DQ) weights on skinned meshes.
It allows you to export DQ weights,
convert DQ weights to a grayscale color set for visualization and further use in Unreal Engine

Инструмент DQ Blend Weights
==========================================

Этот скрипт предоставляет набор инструментов для работы с весами Dual Quaternion (DQ) на скинниных мешах. 
Он позволяет экспортировать DQ веса, 
конвентировать DQ веса в колор сет с градацией серого для визуализации и для дальнейшего использования в анриле
---------------------------------------------------------------------------------------------------------------
"""

# --- load plugin automatically ---
PLUGIN_PATH = r"E:\maya_plugins\DQ_weights\applyDQVertexColorsCmd\x64\Release\applyDQVertexColors.mll"
if not cmds.pluginInfo(PLUGIN_PATH, query=True, loaded=True):
    try:
        cmds.loadPlugin(PLUGIN_PATH)
        print("Plugin loaded:", PLUGIN_PATH)
    except Exception as e:
        cmds.warning("Failed to load plugin: %s" % e)
        
EXPORT_DIR = r"D:\export_dq_blend_weights"  # export folder, created automatically if it doesn't exist / папка для экспорта, создает автоматически, если её нет
DECIMAL_PLACES = 4  # number of decimal places for weights / количество знаков после запятой
SAVE_ZERO_WEIGHTS = True    # save zero weights or skip / сохранять нулевые веса при экспорте или нет
MERGE_COLORSET = True   # combine colorsets or replace / объединять колорсеты или заменить
CHECK_DQ_WEIGHTS = False    # check if weights exist before export / проверка на DQ веса перед экспортом


# --- Convert faces, edges -> vert ---
def get_selected_vertices():
    """
    -----------------------------------------------------
    Gets all selected vertices from the current selection
    Converts faces/edges to vertices if necessary

    Получает все выбранные вертексы из текущего выделения
    Автоматически конвертирует фэйсы/эджи в вертексы
    -----------------------------------------------------
    """
    sel = cmds.ls(selection=True, flatten=True)
    if not sel:
        return []
    verts = cmds.polyListComponentConversion(sel, toVertex=True)
    verts = cmds.ls(verts, flatten=True)
    return verts


# --- Build export path with versioning ---
def build_export_path(mesh_name, suffix=""):
    """
    -------------------------------------------------------------
    Creates an export path with automatic version addition
    Creates a folder for saving files if one doesn't exist

    Создает путь для экспорта с автоматическим добавлением версии
    Создает папку для сохранений файлов, если её нет
    -------------------------------------------------------------
    """
    scene_path = cmds.file(query=True, sceneName=True)
    scene_name = "untitled" if not scene_path else os.path.splitext(os.path.basename(scene_path))[0]

    # create a subfolder for the scene
    scene_dir = os.path.join(EXPORT_DIR, scene_name)
    if not os.path.exists(scene_dir):
        os.makedirs(scene_dir)

    base_name = "{}_{}".format(scene_name, mesh_name)
    if suffix:
        base_name += "_{}".format(suffix)
    base_name_clean = re.sub(r'_v\d{2}$', '', base_name)

    version = 1
    while True:
        versioned_name = "{}_v{:02d}.json".format(base_name_clean, version)
        final_path = os.path.join(scene_dir, versioned_name)
        if not os.path.exists(final_path):
            return final_path
        version += 1


# --- Save JSON ---
def save_json_singleline_vertices(data, path):
    """
    --------------------------------------------------------------------------------------------------
    Saving JSON to a file also creates arrays for vertices in one line for easier reading

    Сохранение JSON в файла, вдобавок создает массивы для вертексов в одну строку для удобства чтения
    --------------------------------------------------------------------------------------------------
    """
    text = json.dumps(data, indent=4)

    def one_line_vertices(match):
        arr = match.group(1)
        arr = arr.replace("\n", "").replace(" ", "")
        numbers = arr.strip("[],")
        nums = [n for n in numbers.split(",") if n]
        return '"vertices": [%s]' % ", ".join(nums)

    text = re.sub(r'"vertices": \[(.*?)\]', one_line_vertices, text, flags=re.S)
    with open(path, "w") as f:
        f.write(text)


# --- Export DQ blend weights ---
def export_dq_blend_weights(output_path, verts_only=False):
    """
    ---------------------------------------------------------------
    Exports DQ weights from the selected mesh or selected vertices

    Экспортирует DQ веса из выбранного меша или выбранных вертексов
    ---------------------------------------------------------------
    """
    global DECIMAL_PLACES, SAVE_ZERO_WEIGHTS, CHECK_DQ_WEIGHTS

    if verts_only:
        sel_verts = get_selected_vertices()
        if not sel_verts:
            cmds.error("Please select vertices")
        mesh = sel_verts[0].split(".")[0]
        mesh_shape = cmds.listRelatives(mesh, shapes=True, fullPath=True)[0]
    else:
        sel = cmds.ls(selection=True, dag=True, shapes=True)
        if not sel:
            cmds.error("Please select a mesh.")
        mesh_shape = sel[0]
        mesh = cmds.listRelatives(mesh_shape, parent=True, fullPath=True)[0]

    history = cmds.listHistory(mesh_shape) or []
    skin_clusters = cmds.ls(history, type='skinCluster')
    if not skin_clusters:
        if CHECK_DQ_WEIGHTS:
            cmds.warning("No skinCluster found on the selected mesh. Export canceled.")
            return
        else:
            skin_cluster = None
    else:
        skin_cluster = skin_clusters[0]

    raw_weights = {}
    threshold = 10.0 ** (-DECIMAL_PLACES)

    if skin_cluster:
        if verts_only:
            for v in sel_verts:
                idx = int(v.split("[")[-1].split("]")[0])
                w = float(cmds.getAttr("%s.blendWeights[%d]" % (skin_cluster, idx)))
                if abs(w) < threshold:
                    if SAVE_ZERO_WEIGHTS:
                        w = 0.0
                    else:
                        continue
                if w > 1.0:
                    w = 1.0
                weight_str = "{0:.{1}f}".format(w, DECIMAL_PLACES).rstrip("0").rstrip(".")
                raw_weights[idx] = weight_str
        else:
            num_verts = cmds.polyEvaluate(mesh, vertex=True)
            for i in range(num_verts):
                w = float(cmds.getAttr("%s.blendWeights[%d]" % (skin_cluster, i)))
                if abs(w) < threshold:
                    if SAVE_ZERO_WEIGHTS:
                        w = 0.0
                    else:
                        continue
                if w > 1.0:
                    w = 1.0
                weight_str = "{0:.{1}f}".format(w, DECIMAL_PLACES).rstrip("0").rstrip(".")
                raw_weights[i] = weight_str

        if CHECK_DQ_WEIGHTS and (not raw_weights or all(float(w) == 0.0 for w in raw_weights.values())):
            cmds.warning("Mesh '%s' has no Dual Quaternion weights. Export canceled." % mesh)
            return

    grouped = {}
    for vtx, w_str in raw_weights.items():
        grouped.setdefault(w_str, []).append(vtx)

    dq_weights_sorted = [
        {"weight": w_str, "vertices": sorted(verts)}
        for w_str, verts in sorted(grouped.items(), key=lambda x: float(x[0]))
    ]

    export_data = {
        "mesh": mesh,
        "skinCluster": skin_cluster if skin_cluster else "",
        "exportMode": "verts" if verts_only else "mesh",
        "blendWeights": dq_weights_sorted
    }

    save_json_singleline_vertices(export_data, output_path)
    print("Exported DQ blend weights to %s" % output_path)


# --- Apply DQ weights to vertex color ---
def apply_dq_weights_with_plugin(json_path, color_set_name='dqColorSet'):
    """
    --------------------------------------------------------
    Apply DQ weights from JSON to selected mesh via plugin

    Применяет DQ веса из JSON к выбранному мешу через плагин
    --------------------------------------------------------
    """
    start_time = time.time()  # старт таймера
    if not cmds.pluginInfo('applyDQVertexColors', query=True, loaded=True):
        cmds.loadPlugin('applyDQVertexColors')

    with open(json_path, 'r') as f:
        data = json.load(f)

    mesh_name = data['mesh']

    # If it's a transform, we take shape
    if cmds.objExists(mesh_name) and cmds.objectType(mesh_name, isType='transform'):
        shapes = cmds.listRelatives(mesh_name, shapes=True) or []
        if shapes:
            mesh_name = shapes[0]

    # We form lists of vertices and colors
    verts = []
    colors = []
    for block in data['blendWeights']:
        w = float(block['weight'])
        for idx in block['vertices']:
            verts.append(int(idx))
            colors.extend([w, w, w])

    # Generating arguments for the plugin
    args = ['-mesh', mesh_name, '-set', color_set_name, '-M', MERGE_COLORSET]

    for v in verts:
        args.extend(['-verts', int(v)])

    for i in range(0, len(colors), 3):
        args.extend(['-colors', float(colors[i]), float(colors[i+1]), float(colors[i+2])])

    # Run plugin
    cmds.applyDQVertexColors(*args)
    end_time = time.time()
    print("Time to apply DQ vertex colors: {:.3f} seconds".format(end_time - start_time))

# --- Export + Apply ---
def export_apply_combine_colors(file_field, verts_only=True):
    """
    -----------------------------------
    Exporting DQ weights and using them
    Экспорт весов DQ и их использование
    -----------------------------------
    """
    if verts_only:
        sel_verts = get_selected_vertices()
        if not sel_verts:
            cmds.warning("Select vertices")
            return
        mesh = sel_verts[0].split(".")[0]
        suffix = "vrt"
    else:
        sel = cmds.ls(selection=True, dag=True, shapes=True)
        if not sel:
            cmds.warning("Select a mesh")
            return
        mesh = cmds.listRelatives(sel[0], parent=True)[0]
        suffix = ""

    final_path = build_export_path(mesh, suffix=suffix)
    cmds.textFieldButtonGrp(file_field, edit=True, text=final_path)

    # --- Export ---
    export_dq_blend_weights(final_path, verts_only)

    # --- Apply via plugin ---
    if os.path.exists(final_path):
        apply_dq_weights_with_plugin(final_path)



# --- Remove color set ---
def remove_dq_color_set(*args):
    """
    ---------------------------------------------
    Remove dqColorSet from mesh if it exists

    Удаляет dqColorSet с меша, если он существует
    ---------------------------------------------
    """
    sel = cmds.ls(selection=True, dag=True, shapes=True)
    if not sel:
        cmds.warning("Select at least one mesh")
        return

    for shape in sel:
        color_sets = cmds.polyColorSet(shape, query=True, allColorSets=True) or []
        for cs in color_sets:
            try:
                current = cmds.polyColorSet(shape, query=True, currentColorSet=True)
                ####
                if current == cs:
                    cmds.polyColorSet(shape, create=True, colorSet="__temp__")
                    cmds.polyColorSet(shape, currentColorSet=True, colorSet="__temp__")
                cmds.polyColorSet(shape, delete=True, colorSet=cs)
            except Exception as e:
                cmds.warning("Failed to remove '%s' from '%s': %s" % (cs, shape, e))



# --- UI ---
def dq_weights_v308_ui():
    global MERGE_COLORSET, CHECK_DQ_WEIGHTS
    window_name = "dqWeightToolUI_v3.0.8"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)

    window = cmds.window(window_name, title="DQ Blend Weights Tool v3.0.8", widthHeight=(360, 650), sizeable=True)
    cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnAlign="center")

    file_field = cmds.textFieldButtonGrp(
        label="DQ Weights JSON",
        buttonLabel="Browse",
        columnWidth=[(1, 100)],
        adjustableColumn=2
    )

    def browse_json(*args):
        file_path = cmds.fileDialog2(
            fileFilter="JSON Files (*.json)",
            dialogStyle=2,
            fileMode=1,               
            startingDirectory=EXPORT_DIR  # open a specific folder
        )
        if file_path:
            cmds.textFieldButtonGrp(file_field, edit=True, text=file_path[0])


    def run_export_mesh(*args):
        sel = cmds.ls(selection=True, dag=True, shapes=True)
        if not sel:
            cmds.warning("Select a mesh")
            return
        mesh_transform = cmds.listRelatives(sel[0], parent=True)[0]
        final_path = build_export_path(mesh_transform)
        cmds.textFieldButtonGrp(file_field, edit=True, text=final_path)
        export_dq_blend_weights(final_path, False)

    def run_export_verts(*args):
        sel_verts = get_selected_vertices()
        if not sel_verts:
            cmds.warning("Select vertices")
            return
        mesh = sel_verts[0].split(".")[0]
        final_path = build_export_path(mesh, suffix="vrt")
        cmds.textFieldButtonGrp(file_field, edit=True, text=final_path)
        export_dq_blend_weights(final_path, True)

    def run_export_apply_mesh(*args):
        export_apply_combine_colors(file_field, False)

    def run_export_apply_verts(*args):
        export_apply_combine_colors(file_field, True)

    def run_apply(*args):
        path = cmds.textFieldButtonGrp(file_field, query=True, text=True)
        if os.path.exists(path):
            apply_dq_weights_with_plugin(path)
        else:
            cmds.warning("Invalid path/JSON")



    def toggle_vertex_color_display(*args):
        sel = cmds.ls(selection=True, dag=True, shapes=True)
        if not sel:
            cmds.warning("Select at least one mesh")
            return
    
        #### check
        for shape in sel:
            try:
                current_state = cmds.getAttr("%s.displayColors" % shape)
                new_state = not current_state
                cmds.setAttr("%s.displayColors" % shape, new_state)
    
                #### upd modelpanel
                for panel in cmds.getPanel(type='modelPanel'):
                    try:
                        cmds.modelEditor(panel, edit=True, displayColors=new_state)
                    except:
                        pass
            except Exception as e:
                cmds.warning("Failed to toggle displayColors for '%s': %s" % (shape, e))


    def change_decimal_places(value):
        global DECIMAL_PLACES
        DECIMAL_PLACES = int(value)

    def toggle_save_zero(value):
        global SAVE_ZERO_WEIGHTS
        SAVE_ZERO_WEIGHTS = bool(value)

    def toggle_merge_colorset(value):
        global MERGE_COLORSET
        MERGE_COLORSET = bool(value)

    def toggle_check_dq(value):
        global CHECK_DQ_WEIGHTS
        CHECK_DQ_WEIGHTS = bool(value)

    cmds.textFieldButtonGrp(file_field, edit=True, buttonCommand=browse_json)
    cmds.intSliderGrp(label="Decimal Places", field=True, min=2, max=20, value=DECIMAL_PLACES, changeCommand=change_decimal_places)


    cmds.rowLayout(numberOfColumns=3, adjustableColumn=3, columnAlign=(1, 'left'), columnAttach=[(1, 'left', 0), (2, 'left', 0), (3,'left',0)])
    cmds.checkBox(label="Save Zero Weights", value=SAVE_ZERO_WEIGHTS, changeCommand=toggle_save_zero)
    cmds.checkBox(label="Merge colorset", value=MERGE_COLORSET, changeCommand=toggle_merge_colorset)
    cmds.checkBox(label="Check DQ before Export", value=CHECK_DQ_WEIGHTS, changeCommand=toggle_check_dq)
    cmds.setParent('..')
    cmds.separator(height=5)
    cmds.button(label="Export DQ from Mesh", height=25, command=run_export_mesh)
    cmds.button(label="Export DQ from Selection", height=25, command=run_export_verts)
    cmds.button(label="Apply as Vertex Color", height=25, command=run_apply)

    cmds.separator(height=1)
    cmds.button(label="Export+Apply from Mesh", height=35, bgc=(0.6, 0.8, 0.9), command=run_export_apply_mesh)
    cmds.button(label="Export+Apply from Selection", height=35, bgc=(0.4, 0.8, 0.4), command=run_export_apply_verts)

    cmds.separator(height=1)
    cmds.button(label="Toggle Display Color", height=30, command=toggle_vertex_color_display)
    cmds.button(label="Remove Color Set", height=30, command=remove_dq_color_set)

    cmds.separator(height=5)

    cmds.setParent('..')
    cmds.showWindow(window)


def export_quaternion_v308():
    """
    Function that launches the interface from the script manager (its name must match the file name)
    """
    dq_weights_v308_ui()


if __name__ == '__main__':
    export_quaternion_v308()

