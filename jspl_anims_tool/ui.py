# -*- coding: utf-8 -*-
# ui.py
import maya.cmds as cmds
from . import utils, project_manager, data_handler, auto_rotation

def on_plus_button_click(*args):
    selection = cmds.ls(selection=True)
    if selection and cmds.textField("root_text_field", exists=True):
        cmds.textField("root_text_field", edit=True, text=selection[0])
        print("Root set to: " + selection[0])

def on_clear_button_click(*args):
    if cmds.textField("root_text_field", exists=True):
        cmds.textField("root_text_field", edit=True, text="")

def create_window():
    window_name = "jointTransformsWindow"
    
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name, window=True)

    window = cmds.window(window_name, title="jsp_TransformTool", widthHeight=(380, 710), sizeable=True)
    
    main_layout = cmds.columnLayout(adjustableColumn=True)
    
    # ========================================================
    # 1. ROOT SELECTOR
    # ========================================================
    cmds.separator(height=5, style='none')
    
    cmds.rowLayout(numberOfColumns=4, adjustableColumn=1, 
                   columnWidth4=(170, 75, 30, 50), 
                   columnAttach=[(1, 'both', 2), (2, 'both', 0), (3, 'both', 0), (4, 'both', 2)])
                   
    cmds.textField("root_text_field", placeholderText=":ROOT", editable=False)
    cmds.checkBox("cb_hierarchy", label="Hierarchy", value=True)
    cmds.button(label="+", width=30, height=25, command=on_plus_button_click)
    cmds.button(label="Clear", width=50, height=25, command=on_clear_button_click)
    cmds.setParent('..') 
    
    cmds.separator(height=10, style='in')

    # ========================================================
    # 2. PROJECT MANAGER
    # ========================================================
    cmds.frameLayout(label="Project Manager", collapsable=False, marginHeight=5, marginWidth=5)
    cmds.columnLayout(adjustableColumn=True)
    
    # Projects Row
    cmds.text(label="Projects", align='left', font='boldLabelFont')
    
    cmds.rowLayout(numberOfColumns=4, adjustableColumn=1, 
                   columnWidth4=(200, 30, 30, 60),
                   columnAttach=[(1,'both',2), (2,'both',2), (3,'both',2), (4,'both',2)])
    cmds.optionMenu("om_projects", changeCommand=project_manager.char_ref) 
    cmds.button(label="+", width=30, height=25, command=project_manager.proj_add)
    cmds.button(label="-", width=30, height=25, command=project_manager.proj_rem)
    cmds.button(label="Refresh", width=60, height=25, command=project_manager.proj_ref)
    cmds.setParent('..') 
    
    cmds.separator(h=10, style='none')

    # CHARACTERS & ANIMATIONS (50/50 Split)
    main_split = cmds.formLayout()
    
    # --- Left: Characters ---
    left_form = cmds.formLayout()
    l_txt = cmds.text(label="Characters", align='left', font='boldLabelFont')
    l_list = cmds.textScrollList("tsl_characters", allowMultiSelection=False, selectCommand=project_manager.anim_ref) 
    
    btn_char_add = cmds.button(label="+", height=25, command=project_manager.char_add)
    btn_char_rem = cmds.button(label="-", height=25, command=project_manager.char_rem)
    btn_char_ref = cmds.button(label="Refresh", height=25, command=project_manager.char_ref)
    
    cmds.formLayout(left_form, edit=True,
        attachForm=[
            (l_txt, 'top', 0), (l_txt, 'left', 0), (l_txt, 'right', 0),
            (l_list, 'left', 0), (l_list, 'right', 0),
            (btn_char_add, 'left', 0), (btn_char_add, 'bottom', 0),
            (btn_char_rem, 'bottom', 0),
            (btn_char_ref, 'right', 0), (btn_char_ref, 'bottom', 0)
        ],
        attachControl=[(l_list, 'top', 2, l_txt), (l_list, 'bottom', 2, btn_char_add)],
        attachPosition=[
            (btn_char_add, 'right', 1, 33), 
            (btn_char_rem, 'left', 1, 33), (btn_char_rem, 'right', 1, 66),
            (btn_char_ref, 'left', 1, 66)
        ]
    )
    cmds.setParent('..') 

    # --- Right: Animations ---
    right_form = cmds.formLayout()
    r_txt = cmds.text(label="Animations", align='left', font='boldLabelFont')
    
    # ИЗМЕНЕНИЕ ЗДЕСЬ: Добавили doubleClickCommand
    r_list = cmds.textScrollList("tsl_animations", allowMultiSelection=False, doubleClickCommand=project_manager.import_single_animation)
    
    btn_anim_save = cmds.button(label="Save", height=25, command=project_manager.anim_save, bgc=(0.3, 0.5, 0.3))
    btn_anim_ref = cmds.button(label="Refresh", height=25, command=project_manager.anim_ref)
    btn_anim_rem = cmds.button(label="Remove", height=25, command=project_manager.anim_rem)
    
    cmds.formLayout(right_form, edit=True,
        attachForm=[
            (r_txt, 'top', 0), (r_txt, 'left', 0), (r_txt, 'right', 0),
            (r_list, 'left', 0), (r_list, 'right', 0),
            (btn_anim_save, 'left', 0), (btn_anim_save, 'bottom', 0),
            (btn_anim_ref, 'bottom', 0),
            (btn_anim_rem, 'right', 0), (btn_anim_rem, 'bottom', 0)
        ],
        attachControl=[(r_list, 'top', 2, r_txt), (r_list, 'bottom', 2, btn_anim_save)],
        attachPosition=[
            (btn_anim_save, 'right', 1, 33), 
            (btn_anim_ref, 'left', 1, 33), (btn_anim_ref, 'right', 1, 66),
            (btn_anim_rem, 'left', 1, 66)
        ]
    )
    cmds.setParent('..') 

    cmds.formLayout(main_split, edit=True,
        attachForm=[(left_form, 'top', 0), (left_form, 'left', 0), (left_form, 'bottom', 0),
                    (right_form, 'top', 0), (right_form, 'right', 0), (right_form, 'bottom', 0)],
        attachPosition=[(left_form, 'right', 2, 50), (right_form, 'left', 2, 50)])
    
    cmds.setParent('..') 
    
    # ========================================================
    # БЛОК МАССОВОГО ИМПОРТА И УДАЛЕНИЯ
    # ========================================================
    cmds.separator(height=10, style='none')
    
    cmds.rowLayout(numberOfColumns=6, adjustableColumn=6, 
                   columnWidth6=(95, 45, 35, 45, 35, 45),
                   columnAttach=[(1, 'right', 2), (2, 'both', 0), (3, 'right', 2), (4, 'both', 0), (5, 'right', 2), (6, 'both', 0)])
    
    cmds.text(label="Key All Keyable:")
    cmds.intField("if_key_all", value=-1) 
    
    cmds.text(label="Start:")
    cmds.intField("if_start_frame", value=5) 
    
    cmds.text(label="Step:")
    cmds.intField("if_frame_step", value=10) 
    
    cmds.setParent('..') 
    
    cmds.separator(height=5, style='none')
    cmds.button(label="Import all animations from list", height=30, bgc=(0.2, 0.4, 0.6), command=project_manager.import_all_animations)
    
    cmds.separator(height=2, style='none')
    cmds.button(label="Delete imported animations", height=25, bgc=(0.6, 0.2, 0.2), command=project_manager.delete_imported_animations)
    
    cmds.setParent('..') # End Project Manager Column
    cmds.setParent('..') # End FrameLayout

    # ========================================================
    # 3. JOINT ACTIONS
    # ========================================================
    cmds.separator(height=10, style='none')
    cmds.text(label="Joint Actions", align='center', font='boldLabelFont')
    
    cmds.button(label="Copy to temp file", height=25, command=lambda x: data_handler.on_copy_click_wrapper())
    cmds.button(label="Paste to temp file", height=25, command=lambda x: data_handler.on_paste_click_wrapper())
    cmds.separator(height=5, style='none')
    cmds.button(label="Export transform to file", height=25, command=lambda x: data_handler.export_joint_transformations())
    cmds.button(label="Import transform to file", height=25, command=lambda x: data_handler.apply_joint_transformations())
    cmds.separator(height=5, style='none')
    cmds.button(label="Key All Keyable", height=25, command=lambda x: data_handler.key_all_keyable())

    # ========================================================
    # 4. AUTO ROTATION
    # ========================================================
    cmds.separator(height=15, style='in')
    cmds.text(label="Auto Rotation Setup", align='left', font='boldLabelFont')
    cmds.button(label="Setup auto rotation", height=25, command=auto_rotation.setup_auto_rotation)
    cmds.button(label="Break auto rotation", height=25, command=auto_rotation.break_auto_rotation)
    
    cmds.showWindow(window)
    
    utils.ensure_base_path()
    project_manager.proj_ref()