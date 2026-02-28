# -*- coding: utf-8 -*-
# data_handler.py
import maya.cmds as cmds
import json
import io
import os
from . import utils, config

def get_joint_data_from_selection():
    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints:
        cmds.warning("Selection is empty. Please select joints.")
        return None
    
    joint_data = {}
    for joint in selected_joints:
        joint_name = utils.remove_namespace(joint)
        try:
            t = cmds.getAttr("{}.translate".format(joint))[0]
            r = cmds.getAttr("{}.rotate".format(joint))[0]
            joint_data[joint_name] = {
                "translation": {"x": t[0], "y": t[1], "z": t[2]}, 
                "rotation": {"x": r[0], "y": r[1], "z": r[2]}
            }
        except: 
            pass
    return joint_data

def smart_select_hierarchy():
    if not cmds.textField("root_text_field", exists=True): return False
    root_name = cmds.textField("root_text_field", query=True, text=True)
    
    if not root_name or root_name == ":ROOT":
        selected = cmds.ls(selection=True)
        if not selected:
            cmds.error("Text field is empty and nothing is selected.")
        return True

    if not cmds.objExists(root_name):
        cmds.error(u"Object not found: {}".format(root_name))

    descendants = cmds.listRelatives(root_name, allDescendents=True, fullPath=True) or []
    descendants.append(root_name)

    target_joint = None
    for obj in descendants:
        if obj.split("|")[-1].split(":")[-1].lower() == "pelvis":
            target_joint = obj
            break
    if not target_joint:
        for obj in descendants:
            if obj.split("|")[-1].split(":")[-1].lower() in ["centre", "center"]:
                target_joint = obj
                break

    if target_joint:
        print("Found target: {}".format(target_joint))
        cmds.select(target_joint, replace=True)
        cmds.select(hierarchy=True)
        return True
    else:
        cmds.error(u"Could not find 'pelvis' inside {}".format(root_name))
        return False

def _core_export(get_file_dialog):
    joint_data = get_joint_data_from_selection()
    if not joint_data:
        return

    if get_file_dialog:
        file_path = cmds.fileDialog2(fileFilter="JSON Files (*.json)", dialogStyle=2, fileMode=0)
        if file_path:
            with open(file_path[0], 'w') as f: json.dump(joint_data, f, indent=4)
            cmds.confirmDialog(title="Success", message="Export saved: %s" % file_path[0], button="OK")
    else:
        output_path = config.TEMP_FILE_PATH
        try:
            with open(output_path, 'w') as f: json.dump(joint_data, f, indent=4)
            print("Temp Export saved.")
        except Exception as e: cmds.error("Error: {}".format(str(e)))

def _core_import(use_temp_file):
    if use_temp_file:
        file_path = config.TEMP_FILE_PATH
        if not os.path.exists(file_path): cmds.error(u"Temp file not found.")
    else:
        file_path_list = cmds.fileDialog2(fileFilter="JSON Files (*.json)", dialogStyle=2, fileMode=1)
        if not file_path_list: return
        file_path = file_path_list[0]

    try:
        with io.open(file_path, 'r', encoding='utf-8') as f: joint_data = json.load(f)
    except Exception as e:
        cmds.error(u"Error reading file: %s" % str(e))
        return
    _apply_data_logic(joint_data)

def _apply_data_logic(joint_data):
    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints: cmds.error(u"Select joints.")
    
    for joint in selected_joints:
        joint_name = utils.remove_namespace(joint)
        if joint_name in joint_data:
            t = joint_data[joint_name]["translation"]
            r = joint_data[joint_name]["rotation"]
            for axis in "XYZ":
                utils.unlock_attribute("{}.translate{}".format(joint, axis))
                utils.unlock_attribute("{}.rotate{}".format(joint, axis))
            try: cmds.setAttr("{}.translate".format(joint), t["x"], t["y"], t["z"])
            except: pass 
            try: cmds.setAttr("{}.rotate".format(joint), r["x"], r["y"], r["z"])
            except: pass 
            
    try: cmds.keyTangent(ott='step', animation='objects', g=True)
    except: pass 

# --- Public Wrappers ---
def export_joint_transformations(): _core_export(get_file_dialog=True)
def export_temp_joint_transformations(): _core_export(get_file_dialog=False)
def apply_joint_transformations(): _core_import(use_temp_file=False)
def apply_temp_joint_transformations(): _core_import(use_temp_file=True)

# ИЗМЕНЕНИЯ ЗДЕСЬ:
def on_copy_click_wrapper():
    # Проверяем галочку Hierarchy
    use_hierarchy = True
    if cmds.checkBox("cb_hierarchy", exists=True):
        use_hierarchy = cmds.checkBox("cb_hierarchy", query=True, value=True)
    
    # Если галочка стоит, пытаемся выделить иерархию. Если нет - работаем с тем, что выделено.
    if use_hierarchy:
        if smart_select_hierarchy():
            export_temp_joint_transformations()
    else:
        # Ручной режим
        export_temp_joint_transformations()

def on_paste_click_wrapper():
    use_hierarchy = True
    if cmds.checkBox("cb_hierarchy", exists=True):
        use_hierarchy = cmds.checkBox("cb_hierarchy", query=True, value=True)
        
    if use_hierarchy:
        if smart_select_hierarchy():
            apply_temp_joint_transformations()
    else:
        # Ручной режим
        apply_temp_joint_transformations()

def key_all_keyable():
    selected = cmds.ls(selection=True)
    if not selected: cmds.error("Select objects.")
    for obj in selected:
        attrs = cmds.listAttr(obj, keyable=True)
        if attrs: cmds.setKeyframe(obj, attribute=attrs)