# -*- coding: utf-8 -*-
# project_manager.py
import maya.cmds as cmds
import os
import shutil
import json
import io
from . import config, utils, data_handler

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
    utils.ensure_base_path()
    items = cmds.optionMenu("om_projects", query=True, itemListLong=True)
    if items:
        cmds.deleteUI(items)
    if os.path.exists(config.BASE_PROJECT_PATH):
        folders = [f for f in os.listdir(config.BASE_PROJECT_PATH) if os.path.isdir(os.path.join(config.BASE_PROJECT_PATH, f))]
        for folder in folders:
            cmds.menuItem(label=folder, parent="om_projects")
    char_ref()

def proj_add(*args):
    result = cmds.promptDialog(title='New Project', message='Enter Project Name:', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
    if result == 'OK':
        text = cmds.promptDialog(query=True, text=True)
        if text:
            new_path = os.path.join(config.BASE_PROJECT_PATH, text)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
                proj_ref()
            else:
                cmds.warning("Project already exists!")

def proj_rem(*args):
    current = get_current_project()
    if current:
        path = os.path.join(config.BASE_PROJECT_PATH, current)
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
        proj_path = os.path.join(config.BASE_PROJECT_PATH, current_proj)
        if os.path.exists(proj_path):
            folders = [f for f in os.listdir(proj_path) if os.path.isdir(os.path.join(proj_path, f))]
            for folder in folders:
                cmds.textScrollList("tsl_characters", edit=True, append=folder)
    anim_ref()

def char_add(*args):
    current_proj = get_current_project()
    if not current_proj:
        cmds.warning("No project selected!")
        return
    result = cmds.promptDialog(title='New Character', message='Enter Character Name:', button=['OK', 'Cancel'], defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
    if result == 'OK':
        text = cmds.promptDialog(query=True, text=True)
        if text:
            new_path = os.path.join(config.BASE_PROJECT_PATH, current_proj, text)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
                char_ref()
            else:
                cmds.warning("Character already exists!")

def char_rem(*args):
    current_proj = get_current_project()
    current_char = get_current_character()
    if current_proj and current_char:
        path = os.path.join(config.BASE_PROJECT_PATH, current_proj, current_char)
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
        char_path = os.path.join(config.BASE_PROJECT_PATH, current_proj, current_char)
        if os.path.exists(char_path):
            files = [f for f in os.listdir(char_path) if os.path.isfile(os.path.join(char_path, f))]
            for f in files:
                cmds.textScrollList("tsl_animations", edit=True, append=f)

def anim_save(*args):
    current_proj = get_current_project()
    current_char = get_current_character()
    
    if not current_proj or not current_char:
        cmds.warning("Please select a Project and a Character first.")
        return

    data = data_handler.get_joint_data_from_selection()
    if not data:
        return

    result = cmds.promptDialog(title='Save Animation', message='Enter Animation Name:', button=['Save', 'Cancel'], defaultButton='Save', cancelButton='Cancel', dismissString='Cancel')
    
    if result == 'Save':
        filename = cmds.promptDialog(query=True, text=True)
        if not filename: return
        
        if not filename.endswith('.json'):
            filename += ".json"

        file_path = os.path.join(config.BASE_PROJECT_PATH, current_proj, current_char, filename)
        
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
            print("Saved animation: " + file_path)
            anim_ref()
        except Exception as e:
            cmds.error("Error saving file: " + str(e))

def anim_rem(*args):
    current_proj = get_current_project()
    current_char = get_current_character()
    if cmds.textScrollList("tsl_animations", exists=True):
        sel = cmds.textScrollList("tsl_animations", query=True, selectItem=True)
        if sel and current_proj and current_char:
            filename = sel[0]
            file_path = os.path.join(config.BASE_PROJECT_PATH, current_proj, current_char, filename)
            
            confirm = cmds.confirmDialog(title='Confirm', message='Delete Animation file?\n' + filename, button=['Yes','No'], defaultButton='No', cancelButton='No', dismissString='No')
            if confirm == 'Yes':
                try:
                    os.remove(file_path)
                    anim_ref()
                except Exception as e:
                    cmds.error("Could not delete file: " + str(e))

# ========================================================
# МАССОВЫЙ ИМПОРТ (КЛЮЧИ ТОЛЬКО НА TRANSLATE И ROTATE)
# ========================================================
def import_all_animations(*args):
    current_proj = get_current_project()
    current_char = get_current_character()
    
    if not current_proj or not current_char:
        cmds.warning("Please select a Project and a Character first.")
        return
        
    if not cmds.textScrollList("tsl_animations", exists=True): 
        return
        
    all_anims = cmds.textScrollList("tsl_animations", query=True, allItems=True)
    
    if not all_anims:
        cmds.warning("No animations in the list to import.")
        return

    use_hierarchy = True
    if cmds.checkBox("cb_hierarchy", exists=True):
        use_hierarchy = cmds.checkBox("cb_hierarchy", query=True, value=True)
    
    if use_hierarchy:
        if not data_handler.smart_select_hierarchy():
            return
    else:
        if not cmds.ls(selection=True, type='joint'):
            cmds.warning("Hierarchy checkbox is OFF. Please select joints manually before importing.")
            return

    joints_only = cmds.ls(selection=True, type='joint')
    if not joints_only:
        cmds.warning("No joints found in selection. Meshes and Locators are ignored.")
        return
    
    cmds.select(joints_only, replace=True)

    bind_pose_frame = cmds.intField("if_key_all", query=True, value=True) 
    start_frame = cmds.intField("if_start_frame", query=True, value=True)
    step_frame = cmds.intField("if_frame_step", query=True, value=True)
    
    end_frame = start_frame + (len(all_anims) - 1) * step_frame + 20
    min_frame = min(bind_pose_frame, start_frame) 
    
    cmds.playbackOptions(minTime=min_frame, animationStartTime=min_frame, maxTime=end_frame, animationEndTime=end_frame)
    
    # Сохраняем "Бинд-позу" только на Translate и Rotate
    cmds.currentTime(bind_pose_frame, edit=True)
    cmds.setKeyframe(joints_only, attribute=['translate', 'rotate']) 
    
    success_count = 0
    current_frame = start_frame
    
    for anim_file in all_anims:
        file_path = os.path.join(config.BASE_PROJECT_PATH, current_proj, current_char, anim_file)
        
        if os.path.exists(file_path):
            try:
                with io.open(file_path, 'r', encoding='utf-8') as f:
                    joint_data = json.load(f)
                
                cmds.currentTime(current_frame, edit=True)
                data_handler._apply_data_logic(joint_data)
                
                # Ставим ключи только на трансформации
                cmds.setKeyframe(joints_only, attribute=['translate', 'rotate'])
                
                current_frame += step_frame
                success_count += 1
                
            except Exception as e:
                cmds.warning("Failed to import {}: {}".format(anim_file, str(e)))
                
    print("Successfully imported {} animations! Bind pose set at frame {}. Timeline extended to {}.".format(success_count, bind_pose_frame, end_frame))


# ========================================================
# УДАЛЕНИЕ КЛЮЧЕЙ (ТОЛЬКО TRANSLATE И ROTATE)
# ========================================================
def delete_imported_animations(*args):
    use_hierarchy = True
    if cmds.checkBox("cb_hierarchy", exists=True):
        use_hierarchy = cmds.checkBox("cb_hierarchy", query=True, value=True)
    
    if use_hierarchy:
        if not data_handler.smart_select_hierarchy():
            return
    else:
        if not cmds.ls(selection=True, type='joint'):
            cmds.warning("Hierarchy checkbox is OFF. Please select joints manually to delete animations.")
            return

    joints_only = cmds.ls(selection=True, type='joint')
    if not joints_only:
        cmds.warning("No joints found to delete animations from.")
        return

    if not cmds.textScrollList("tsl_animations", exists=True): 
        return
        
    all_anims = cmds.textScrollList("tsl_animations", query=True, allItems=True)
    if not all_anims:
        cmds.warning("No animations in the list to calculate frames.")
        return

    bind_pose_frame = cmds.intField("if_key_all", query=True, value=True)
    start_frame = cmds.intField("if_start_frame", query=True, value=True)
    step_frame = cmds.intField("if_frame_step", query=True, value=True)

    # ВАЖНО: Перемещаем таймлайн на кадр бинд-позы ПЕРЕД удалением ключей, 
    # чтобы после очистки кривых персонаж остался стоять в этой позе, а не в нулях.
    cmds.currentTime(bind_pose_frame, edit=True)

    deleted_count = 0
    
    # Удаляем ключ бинд-позы (только с Translate и Rotate)
    try:
        cmds.cutKey(joints_only, time=(bind_pose_frame, bind_pose_frame), attribute=['translate', 'rotate'], clear=True)
        deleted_count += 1
    except:
        pass

    # Удаляем ключи самих анимаций (только с Translate и Rotate)
    for i in range(len(all_anims)):
        target_frame = start_frame + (i * step_frame)
        try:
            cmds.cutKey(joints_only, time=(target_frame, target_frame), attribute=['translate', 'rotate'], clear=True)
            deleted_count += 1
        except Exception as e:
            pass

    print("Deleted translate/rotate keys on {} specific frames (including bind pose).".format(deleted_count))

# ========================================================
# ИМПОРТ ОДНОЙ АНИМАЦИИ (ПО ДВОЙНОМУ КЛИКУ)
# ========================================================
def import_single_animation(*args):
    current_proj = get_current_project()
    current_char = get_current_character()
    
    if not current_proj or not current_char:
        cmds.warning("Please select a Project and a Character first.")
        return
        
    if not cmds.textScrollList("tsl_animations", exists=True): 
        return
        
    sel_anim = cmds.textScrollList("tsl_animations", query=True, selectItem=True)
    if not sel_anim:
        return
        
    anim_file = sel_anim[0]
    
    use_hierarchy = True
    if cmds.checkBox("cb_hierarchy", exists=True):
        use_hierarchy = cmds.checkBox("cb_hierarchy", query=True, value=True)
    
    if use_hierarchy:
        if not data_handler.smart_select_hierarchy():
            return
    else:
        if not cmds.ls(selection=True, type='joint'):
            cmds.warning("Hierarchy checkbox is OFF. Please select joints manually before importing.")
            return

    joints_only = cmds.ls(selection=True, type='joint')
    if not joints_only:
        cmds.warning("No joints found in selection.")
        return
    
    cmds.select(joints_only, replace=True)
    
    file_path = os.path.join(config.BASE_PROJECT_PATH, current_proj, current_char, anim_file)
    
    if os.path.exists(file_path):
        try:
            with io.open(file_path, 'r', encoding='utf-8') as f:
                joint_data = json.load(f)
            
            current_frame = cmds.currentTime(query=True)
            data_handler._apply_data_logic(joint_data)
            
            # Ставим ключи только на трансформации
            cmds.setKeyframe(joints_only, attribute=['translate', 'rotate'])
            
            print("Successfully imported {} to frame {}.".format(anim_file, current_frame))
        except Exception as e:
            cmds.warning("Failed to import {}: {}".format(anim_file, str(e)))