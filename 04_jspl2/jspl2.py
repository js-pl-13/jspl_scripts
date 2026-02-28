import maya.cmds as cmds
import json
import io
import os
import tempfile
import shutil

# --- КОНСТАНТЫ ПУТЕЙ ---
BASE_PROJECT_PATH = r"D:\!MyScripts\jspl_transform_anims\projects"

# --- УТИЛИТЫ ---

def ensure_base_path():
    if not os.path.exists(BASE_PROJECT_PATH):
        try:
            os.makedirs(BASE_PROJECT_PATH)
            print("Created base directory: {}".format(BASE_PROJECT_PATH))
        except Exception as e:
            cmds.warning("Could not create base path: {}. Error: {}".format(BASE_PROJECT_PATH, str(e)))

def get_temp_file_path():
    return os.path.join(tempfile.gettempdir(), "maya_joint_export.json")

def remove_namespace(object_name):
    if ":" in object_name:
        return object_name.split(":")[-1]
    return object_name

def unlock_attribute(attribute):
    if cmds.attributeQuery(attribute.split('.')[-1], node=attribute.split('.')[0], exists=True):
        if cmds.getAttr(attribute, lock=True):
            cmds.setAttr(attribute, lock=False)

def get_namespace_from_root():
    if cmds.textField("root_text_field", exists=True):
        root_text = cmds.textField("root_text_field", query=True, text=True)
        if root_text and root_text != ":ROOT":
            if ":" in root_text:
                return root_text.rsplit(":", 1)[0] + ":"
            else:
                return ""
    return ""

# --- ЛОГИКА AUTO ROTATION ---

def setup_auto_rotation(*args):
    ns = get_namespace_from_root()
    print("Setting up auto rotation for namespace: '{}'".format(ns))
    
    connection_groups = [
        [('ARM1L', 'ARMupL', -1), ('l_shoulder', 'l_shoulder_twist_01', -1)],
        [('ARM1R', 'ARMupR', -1), ('r_shoulder', 'r_shoulder_twist_01', -1)],
        [('HANDL', 'forearm_L', 1), ('l_forearm', 'l_forearm_twist_01', 1)],
        [('HANDR', 'forearm_R', 1), ('r_forearm', 'r_forearm_twist_01', 1)],
        [('LEG1L', 'HIP_L', -1), ('l_hip', 'l_hip_twist_01', -1)],
        [('LEG1R', 'HIP_R', -1), ('r_hip', 'r_hip_twist_01', -1)]
    ]

    for group in connection_groups:
        connected = False
        for src, tgt, mult in group:
            full_src = '{}{}'.format(ns, src)
            full_tgt = '{}{}'.format(ns, tgt)
            node_name = '{}{}_mdl'.format(ns, tgt)

            if cmds.objExists(full_src) and cmds.objExists(full_tgt):
                if cmds.listConnections('{}.rotateX'.format(full_tgt), d=False, s=True):
                    inputs = cmds.listConnections('{}.rotateX'.format(full_tgt), d=False, s=True)
                    if inputs and cmds.nodeType(inputs[0]) == 'multDoubleLinear':
                        cmds.delete(inputs[0])

                try:
                    if not cmds.objExists(node_name):
                        cmds.createNode('multDoubleLinear', n=node_name)
                    cmds.connectAttr('{}.rotateX'.format(full_src), '{}.input1'.format(node_name), force=True)
                    cmds.setAttr('{}.input2'.format(node_name), mult)
                    cmds.connectAttr('{}.output'.format(node_name), '{}.rotateX'.format(full_tgt), force=True)
                    print("Connected: {} -> {}".format(full_src, full_tgt))
                    connected = True
                    break 
                except Exception as e:
                    print("Error: {}".format(str(e)))
            
        if not connected:
            print("Warning: Skipping group for '{}'".format(group[0][1]))

def break_auto_rotation(*args):
    ns = get_namespace_from_root()
    print("Breaking auto rotation for namespace: '{}'".format(ns))

    targets = [
        'ARMupL', 'ARMupR', 'forearm_L', 'forearm_R', 'HIP_L', 'HIP_R',
        'l_shoulder_twist_01', 'r_shoulder_twist_01', 'l_forearm_twist_01', 'r_forearm_twist_01', 'l_hip_twist_01', 'r_hip_twist_01'
    ]
    
    for tgt in targets:
        full_tgt = '{}{}'.format(ns, tgt)
        if not cmds.objExists(full_tgt): continue
        attr = '{}.rotateX'.format(full_tgt)
        connections = cmds.listConnections(attr, source=True, destination=False, plugs=True)
        if connections:
            source_node = connections[0].split('.')[0]
            if cmds.nodeType(source_node) == 'multDoubleLinear':
                cmds.delete(source_node)
                print("Deleted MDL node for '{}'".format(tgt))
            else:
                cmds.disconnectAttr(connections[0], attr)
                print("Disconnected '{}'".format(tgt))

# --- ЛОГИКА ПОИСКА (SMART SELECT) ---

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

# --- ОБЕРТКИ ДЛЯ КНОПОК ---

def on_copy_click_wrapper():
    if smart_select_hierarchy(): export_temp_joint_transformations()

def on_paste_click_wrapper():
    if smart_select_hierarchy(): apply_temp_joint_transformations()

# --- ОСНОВНАЯ ЛОГИКА ---

def export_joint_transformations(): _core_export(get_file_dialog=True)
def export_temp_joint_transformations(): _core_export(get_file_dialog=False)

def _core_export(get_file_dialog):
    selected_joints = cmds.ls(selection=True, type='joint')
    if not selected_joints: cmds.error("Selection is empty.")
    
    joint_data = {}
    for joint in selected_joints:
        joint_name = remove_namespace(joint)
        try:
            t = cmds.getAttr("{}.translate".format(joint))[0]
            r = cmds.getAttr("{}.rotate".format(joint))[0]
            joint_data[joint_name] = {"translation": {"x": t[0], "y": t[1], "z": t[2]}, "rotation": {"x": r[0], "y": r[1], "z": r[2]}}
        except: pass 

    if get_file_dialog:
        file_path = cmds.fileDialog2(fileFilter="JSON Files (*.json)", dialogStyle=2, fileMode=0)
        if file_path:
            with open(file_path[0], 'w') as f: json.dump(joint_data, f, indent=4)
            cmds.confirmDialog(title="Success", message="Export saved: %s" % file_path[0], button="OK")
    else:
        output_path = get_temp_file_path()
        try:
            with open(output_path, 'w') as f: json.dump(joint_data, f, indent=4)
            print("Temp Export saved.")
        except Exception as e: cmds.error("Error: {}".format(str(e)))

def apply_joint_transformations(): _core_import(use_temp_file=False)
def apply_temp_joint_transformations(): _core_import(use_temp_file=True)

def _core_import(use_temp_file):
    if use_temp_file:
        file_path = get_temp_file_path()
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
        joint_name = remove_namespace(joint)
        if joint_name in joint_data:
            t = joint_data[joint_name]["translation"]
            r = joint_data[joint_name]["rotation"]
            for axis in "XYZ":
                unlock_attribute("{}.translate{}".format(joint, axis))
                unlock_attribute("{}.rotate{}".format(joint, axis))
            try: cmds.setAttr("{}.translate".format(joint), t["x"], t["y"], t["z"])
            except: pass 
            try: cmds.setAttr("{}.rotate".format(joint), r["x"], r["y"], r["z"])
            except: pass 
            
    try: cmds.keyTangent(ott='step', animation='objects', g=True)
    except: pass 

def key_all_keyable():
    selected = cmds.ls(selection=True)
    if not selected: cmds.error("Select objects.")
    for obj in selected:
        attrs = cmds.listAttr(obj, keyable=True)
        if attrs: cmds.setKeyframe(obj, attribute=attrs)

# --- UI LOGIC ---

def on_plus_button_click(*args):
    selection = cmds.ls(selection=True)
    if selection and cmds.textField("root_text_field", exists=True):
        cmds.textField("root_text_field", edit=True, text=selection[0])
        print("Root set to: " + selection[0])

def on_clear_button_click(*args):
    if cmds.textField("root_text_field", exists=True):
        cmds.textField("root_text_field", edit=True, text="")

# --- PROJECT MANAGER LOGIC ---

def get_current_project():
    if cmds.optionMenu("om_projects", exists=True):
        items = cmds.optionMenu("om_projects", query=True, itemListLong=True)
        if items:
            return cmds.optionMenu("om_projects", query=True, value=True)
    return None

def get_current_character():
    if cmds.textScrollList("tsl_characters", exists=True):
        sel = cmds.textScrollList("tsl_characters", query=True, selectItem=True)
        if sel:
            return sel[0]
    return None

def proj_ref(*args):
    ensure_base_path()
    items = cmds.optionMenu("om_projects", query=True, itemListLong=True)
    if items:
        cmds.deleteUI(items)
    if os.path.exists(BASE_PROJECT_PATH):
        folders = [f for f in os.listdir(BASE_PROJECT_PATH) if os.path.isdir(os.path.join(BASE_PROJECT_PATH, f))]
        for folder in folders:
            cmds.menuItem(label=folder, parent="om_projects")
    char_ref()

def proj_add(*args):
    result = cmds.promptDialog(title='New Project', message='Enter Project Name:', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
    if result == 'OK':
        text = cmds.promptDialog(query=True, text=True)
        if text:
            new_path = os.path.join(BASE_PROJECT_PATH, text)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
                proj_ref()
            else:
                cmds.warning("Project already exists!")

def proj_rem(*args):
    current = get_current_project()
    if current:
        path = os.path.join(BASE_PROJECT_PATH, current)
        confirm = cmds.confirmDialog(title='Confirm', message='Delete Project and ALL contents?\n' + current, button=['Yes','No'], defaultButton='No', cancelButton='No', dismissString='No')
        if confirm == 'Yes':
            try:
                shutil.rmtree(path)
                proj_ref()
            except Exception as e:
                cmds.error("Could not delete: " + str(e))

def char_ref(*args):
    current_proj = get_current_project()
    cmds.textScrollList("tsl_characters", edit=True, removeAll=True)
    if current_proj:
        proj_path = os.path.join(BASE_PROJECT_PATH, current_proj)
        if os.path.exists(proj_path):
            folders = [f for f in os.listdir(proj_path) if os.path.isdir(os.path.join(proj_path, f))]
            for folder in folders:
                cmds.textScrollList("tsl_characters", edit=True, append=folder)

def char_add(*args):
    current_proj = get_current_project()
    if not current_proj:
        cmds.warning("No project selected!")
        return
    result = cmds.promptDialog(title='New Character', message='Enter Character Name:', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
    if result == 'OK':
        text = cmds.promptDialog(query=True, text=True)
        if text:
            new_path = os.path.join(BASE_PROJECT_PATH, current_proj, text)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
                char_ref()
            else:
                cmds.warning("Character already exists!")

def char_rem(*args):
    current_proj = get_current_project()
    current_char = get_current_character()
    if current_proj and current_char:
        path = os.path.join(BASE_PROJECT_PATH, current_proj, current_char)
        confirm = cmds.confirmDialog(title='Confirm', message='Delete Character folder?\n' + current_char, button=['Yes','No'], defaultButton='No', cancelButton='No', dismissString='No')
        if confirm == 'Yes':
            try:
                shutil.rmtree(path)
                char_ref()
            except Exception as e:
                cmds.error("Could not delete: " + str(e))

def anim_ref(*args):
    current_proj = get_current_project()
    current_char = get_current_character()
    cmds.textScrollList("tsl_animations", edit=True, removeAll=True)
    if current_proj and current_char:
        char_path = os.path.join(BASE_PROJECT_PATH, current_proj, current_char)
        if os.path.exists(char_path):
            files = [f for f in os.listdir(char_path) if os.path.isfile(os.path.join(char_path, f))]
            for f in files:
                cmds.textScrollList("tsl_animations", edit=True, append=f)

def anim_rem(*args):
    print("Animation Remove clicked (Logic pending)")


# --- ИНТЕРФЕЙС ---

def create_joint_transforms_window():
    window_name = "jointTransformsWindow"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name, window=True)

    # Увеличил ширину до 340 для комфортного размещения кнопок
    window = cmds.window(window_name, title="jsp_TransformTool", widthHeight=(340, 750), sizeable=True)
    
    main_layout = cmds.columnLayout(adjustableColumn=True)
    
    # 1. ROOT SELECTOR
    cmds.separator(height=5, style='none')
    cmds.rowLayout(numberOfColumns=3, adjustableColumn=1, 
                   columnWidth3=(180, 30, 50), 
                   columnAttach=[(1, 'both', 5), (2, 'both', 2), (3, 'both', 5)])
    cmds.textField("root_text_field", placeholderText=":ROOT", editable=False)
    cmds.button(label="+", width=30, height=25, command=on_plus_button_click)
    cmds.button(label="Clear", width=50, height=25, command=on_clear_button_click)
    cmds.setParent('..') 
    
    cmds.separator(height=10, style='in')

    # 2. PROJECT MANAGER
    cmds.frameLayout(label="Project Manager", collapsable=False, marginHeight=5, marginWidth=5)
    cmds.columnLayout(adjustableColumn=True)
    
    # Projects Header
    cmds.text(label="Projects", align='left', font='boldLabelFont')
    cmds.rowLayout(numberOfColumns=4, adjustableColumn=1, 
                   columnWidth4=(150, 30, 30, 60), 
                   columnAttach=[(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2)])
    cmds.optionMenu("om_projects", changeCommand=char_ref) 
    cmds.button(label="+", height=25, command=proj_add)
    cmds.button(label="-", height=25, command=proj_rem)
    cmds.button(label="Refresh", height=25, command=proj_ref)
    cmds.setParent('..') 
    cmds.separator(h=10, style='none')

    # --- CHARACTERS & ANIMATIONS (Идеальное выравнивание через FormLayout) ---
    form = cmds.formLayout()
    
    # Левая колонка (Characters)
    left_col = cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Characters", align='left', font='boldLabelFont')
    cmds.textScrollList("tsl_characters", numberOfRows=10, allowMultiSelection=False, selectCommand=anim_ref) 
    
    # Кнопки для Characters (3 кнопки, равномерное распределение)
    # Используем gridLayout для кнопок, чтобы они были одинаковыми
    cmds.gridLayout(numberOfColumns=3, cellWidth=54, cellHeight=25)
    cmds.button(label="Add", command=char_add)
    cmds.button(label="Rem", command=char_rem)
    cmds.button(label="Ref", command=char_ref)
    cmds.setParent('..') 
    cmds.setParent('..') # End Left Column

    # Правая колонка (Animations)
    right_col = cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Animations", align='left', font='boldLabelFont')
    cmds.textScrollList("tsl_animations", numberOfRows=10, allowMultiSelection=False)
    
    # Кнопки для Animations (2 кнопки, равномерное распределение)
    cmds.gridLayout(numberOfColumns=2, cellWidth=81, cellHeight=25)
    cmds.button(label="Refresh", command=anim_ref) 
    cmds.button(label="Remove", command=anim_rem)
    cmds.setParent('..') 
    cmds.setParent('..') # End Right Column

    # Настройка FormLayout: делим экран пополам с отступом 2 пикселя
    cmds.formLayout(form, edit=True,
        attachForm=[(left_col, 'top', 0), (left_col, 'left', 0), (left_col, 'bottom', 0),
                    (right_col, 'top', 0), (right_col, 'right', 0), (right_col, 'bottom', 0)],
        attachPosition=[(left_col, 'right', 2, 50), (right_col, 'left', 2, 50)]) # Разделение на 50%
    
    cmds.setParent('..') # End Form
    # --------------------------------------------------------------------------
    
    cmds.setParent('..') # Back to Project Manager Column
    cmds.setParent('..') # Back to FrameLayout

    # 3. JOINT TOOLS BUTTONS
    cmds.separator(height=10, style='none')
    cmds.text(label="Joint Actions", align='center', font='boldLabelFont')
    
    cmds.button(label="Copy to temp file", height=25, command=lambda x: on_copy_click_wrapper())
    cmds.button(label="Paste to temp file", height=25, command=lambda x: on_paste_click_wrapper())
    cmds.separator(height=5, style='none')
    cmds.button(label="Export transform to file", height=25, command=lambda x: export_joint_transformations())
    cmds.button(label="Import transform to file", height=25, command=lambda x: apply_joint_transformations())
    cmds.separator(height=5, style='none')
    cmds.button(label="Key All Keyable", height=25, command=lambda x: key_all_keyable())

    # 4. AUTO ROTATION
    cmds.separator(height=15, style='in')
    cmds.text(label="Auto Rotation Setup", align='left', font='boldLabelFont')
    cmds.button(label="Setup auto rotation", height=25, command=setup_auto_rotation)
    cmds.button(label="Break auto rotation", height=25, command=break_auto_rotation)
    
    cmds.showWindow(window)
    
    ensure_base_path()
    proj_ref()

create_joint_transforms_window()