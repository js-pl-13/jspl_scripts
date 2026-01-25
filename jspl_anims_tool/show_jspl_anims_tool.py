# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide2 import QtCore, QtWidgets, QtUiTools
from shiboken2 import wrapInstance
import os
import shutil
import json
import datetime
from collections import OrderedDict 

# -------------------------------------------------
# Config
# -------------------------------------------------
UI_FILE = r"D:\!MyScripts\jspl_transform_anims\jsp_transform_tool.ui"
PROJECTS_DIR = r"D:\!MyScripts\jspl_transform_anims\projects"
TEMP_FILES_DIR = r"D:\!MyScripts\jspl_transform_anims\temp_files"
WINDOW_NAME = "jspl_transform_tool_win"
TEMP_FILENAME = "temp_transform_data.json" 

# -------------------------------------------------
# Compatibility
# -------------------------------------------------
try:
    long
    unicode
except NameError:
    long = int
    unicode = str

# -------------------------------------------------
def maya_main_window():
    ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QtWidgets.QWidget)

# -------------------------------------------------
class JSPLTransformTool(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(JSPLTransformTool, self).__init__(parent)
        
        self.setWindowTitle("jspl Anims tool")
        self.setObjectName(WINDOW_NAME)
        self.setFixedSize(375, 725)
        
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(2, 2, 2, 2)
        self.setLayout(self.main_layout)
        
        self.load_ui()
        self.connect_signals()
        self.refresh_projects()
    
    def load_ui(self):
        if not os.path.exists(UI_FILE):
            cmds.warning("UI file not found: {}".format(UI_FILE))
            return
            
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile(UI_FILE)
        
        if not ui_file.open(QtCore.QFile.ReadOnly):
            cmds.warning("Cannot open UI file: {}".format(UI_FILE))
            return
            
        try:
            self.ui = loader.load(ui_file)
            self.main_layout.addWidget(self.ui)
        except Exception as e:
            cmds.warning("Error loading UI: {}".format(e))
        finally:
            ui_file.close()
    
    def current_project_path(self):
        if not hasattr(self, 'ui'):
            return None
        project = self.ui.cmbProjects.currentText()
        if not project:
            return None
        return os.path.join(PROJECTS_DIR, unicode(project))
    
    def characters_root(self):
        path = self.current_project_path()
        if not path:
            return None
        return os.path.join(path, "characters")
    
    def refresh_projects(self):
        if not hasattr(self, 'ui'):
            return
            
        if not os.path.exists(PROJECTS_DIR):
            try:
                os.makedirs(PROJECTS_DIR)
            except:
                cmds.warning("Cannot create projects dir")
                return

        projects = [unicode(name) for name in os.listdir(PROJECTS_DIR)
                    if os.path.isdir(os.path.join(PROJECTS_DIR, name))]
        
        self.ui.cmbProjects.blockSignals(True)
        self.ui.cmbProjects.clear()
        self.ui.cmbProjects.addItems(sorted(projects))
        self.ui.cmbProjects.blockSignals(False)
        self.refresh_characters()
    
    def refresh_characters(self):
        if not hasattr(self, 'ui'):
            return
        self.ui.listCharacters.clear()
        root = self.characters_root()
        if not root or not os.path.exists(root):
            return
        chars = [unicode(name) for name in os.listdir(root)
                 if os.path.isdir(os.path.join(root, name))]
        self.ui.listCharacters.addItems(sorted(chars))
    
    def create_project(self):
        name, ok = QtWidgets.QInputDialog.getText(self, "New Project", "Project name:")
        if not ok or not name.strip():
            return
        name = unicode(name).strip()
        path = os.path.join(PROJECTS_DIR, name)
        if os.path.exists(path):
            cmds.warning("Project already exists")
            return
        os.makedirs(path)
        self.refresh_projects()
        index = self.ui.cmbProjects.findText(name)
        if index != -1:
            self.ui.cmbProjects.setCurrentIndex(index)
    
    def delete_project(self):
        name = self.ui.cmbProjects.currentText()
        if not name:
            return
        name = unicode(name)
        path = os.path.join(PROJECTS_DIR, name)
        reply = QtWidgets.QMessageBox.question(
            self, "Delete Project",
            "Delete project '{}'?\nThis action cannot be undone!".format(name),
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
        )
        if reply != QtWidgets.QMessageBox.Yes:
            return
        try:
            shutil.rmtree(path)
        except Exception as e:
            cmds.warning("Error deleting project: {}".format(e))
        self.refresh_projects()
    
    def add_character(self):
        project_path = self.current_project_path()
        if not project_path:
            cmds.warning("Select a project first!")
            return
        name, ok = QtWidgets.QInputDialog.getText(self, "New Character", "Character name:")
        if not ok or not name.strip():
            return
        name = unicode(name).strip()
        root = self.characters_root()
        path = os.path.join(root, name)
        if not os.path.exists(root):
            os.makedirs(root)
        if os.path.exists(path):
            cmds.warning("Character already exists")
            return
        os.makedirs(path)
        self.refresh_characters()
    
    def remove_character(self):
        item = self.ui.listCharacters.currentItem()
        if not item:
            return
        name = unicode(item.text())
        path = os.path.join(self.characters_root(), name)
        reply = QtWidgets.QMessageBox.question(
            self, "Delete Character",
            "Delete character '{}'?\nThis action cannot be undone!".format(name),
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
        )
        if reply != QtWidgets.QMessageBox.Yes:
            return
        try:
            shutil.rmtree(path)
        except Exception as e:
            cmds.warning("Error deleting character: {}".format(e))
        self.refresh_characters()
    
    def add_root(self):
        sel = cmds.ls(selection=True, type="transform")
        if not sel:
            cmds.warning("No transform selected")
            return
        self.ui.lineRoot.setText(" ".join(sel))
    
    def remove_root(self):
        sel = cmds.ls(selection=True, type="transform")
        if not sel:
            cmds.warning("No transform selected")
            return
        current = self.ui.lineRoot.text().strip()
        if not current:
            return
        roots = current.split()
        roots = [r for r in roots if r not in sel]
        self.ui.lineRoot.setText(" ".join(roots))
    
    def find_skeleton_root(self):
        roots = self.ui.lineRoot.text().strip().split()
        if not roots:
            return None
        for root in roots:
            if not cmds.objExists(root):
                continue
            all_descendants = cmds.listRelatives(root, children=True, allDescendents=True, type="joint") or []
            if cmds.objectType(root) == "joint":
                all_descendants = [root] + all_descendants
            for joint in all_descendants:
                if joint.endswith(":pelvis") or joint.endswith(":CENTRE"):
                    return joint
        possible_joints = []
        all_joints = cmds.ls(type="joint")
        for joint in all_joints:
            if joint.endswith(":pelvis") or joint.endswith(":CENTRE"):
                possible_joints.append(joint)
        if possible_joints:
            return possible_joints[0]
        return None
    
    def get_joint_hierarchy(self, joint):
        if not joint or not cmds.objExists(joint):
            return []
        def get_all_children(parent_joint, children_list):
            direct_children = cmds.listRelatives(parent_joint, children=True, type="joint") or []
            for child in direct_children:
                children_list.append(child)
                get_all_children(child, children_list)
        all_joints = [joint]
        get_all_children(joint, all_joints)
        return all_joints
    
    def get_transform_data(self, joint):
        if not cmds.objExists(joint):
            return None
            
        save_translate = self.ui.chkRootTranslate.isChecked()
        save_rotate = self.ui.chkRootRotate.isChecked()
        
        def fmt(val):
            return round(val, 3)
        
        try:
            data = OrderedDict()
            clean_name = unicode(joint).split(":")[-1]
            data["name"] = clean_name
            
            if save_translate:
                data["translate"] = OrderedDict([
                    ("x", fmt(cmds.getAttr(joint + ".translateX"))),
                    ("y", fmt(cmds.getAttr(joint + ".translateY"))),
                    ("z", fmt(cmds.getAttr(joint + ".translateZ")))
                ])
                
            if save_rotate:
                data["rotate"] = OrderedDict([
                    ("x", fmt(cmds.getAttr(joint + ".rotateX"))),
                    ("y", fmt(cmds.getAttr(joint + ".rotateY"))),
                    ("z", fmt(cmds.getAttr(joint + ".rotateZ")))
                ])
            
            return data
        except:
            return None
    
    def copy_transform_data(self):
        if not self.ui.chkRootTranslate.isChecked() and not self.ui.chkRootRotate.isChecked():
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select Translate and/or Rotate!")
            return

        root_joint = self.find_skeleton_root()
        if not root_joint:
            cmds.warning("Joint 'pelvis' or 'CENTRE' not found in ROOT hierarchy.")
            QtWidgets.QMessageBox.warning(self, "Copy Failed", "Joint 'pelvis' or 'CENTRE' not found.")
            return
        
        joint_hierarchy = self.get_joint_hierarchy(root_joint)
        if not joint_hierarchy:
            QtWidgets.QMessageBox.warning(self, "Copy Failed", "Joint hierarchy not found.")
            return
        
        transform_data = []
        for joint in joint_hierarchy:
            data = self.get_transform_data(joint)
            if data:
                transform_data.append(data)
        
        if not transform_data:
            cmds.warning("Failed to retrieve transform data.")
            return
        
        if not os.path.exists(TEMP_FILES_DIR):
            try:
                os.makedirs(TEMP_FILES_DIR)
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Copy Failed", str(e))
                return
        
        filepath = os.path.join(TEMP_FILES_DIR, TEMP_FILENAME)
        
        try:
            with open(filepath, 'w') as f:
                json.dump(transform_data, f, indent=4, ensure_ascii=False)
            
            print("Data saved to: {}".format(filepath))
            
        except Exception as e:
            cmds.warning("Error saving JSON: {}".format(e))
            QtWidgets.QMessageBox.critical(self, "Copy Failed", str(e))

    # --- NEW FUNCTION: Paste Data ---
    def paste_transform_data(self):
        # 1. Check if file exists
        filepath = os.path.join(TEMP_FILES_DIR, TEMP_FILENAME)
        if not os.path.exists(filepath):
            QtWidgets.QMessageBox.warning(self, "Paste Failed", "Temporary file not found!")
            return

        # 2. Check Checkboxes
        apply_translate = self.ui.chkRootTranslate.isChecked()
        apply_rotate = self.ui.chkRootRotate.isChecked()

        if not apply_translate and not apply_rotate:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select Translate and/or Rotate!")
            return

        # 3. Find target hierarchy (same logic as copy)
        root_joint = self.find_skeleton_root()
        if not root_joint:
            cmds.warning("Joint 'pelvis' or 'CENTRE' not found in ROOT hierarchy.")
            QtWidgets.QMessageBox.warning(self, "Paste Failed", "Joint 'pelvis' or 'CENTRE' not found.")
            return

        joint_hierarchy = self.get_joint_hierarchy(root_joint)
        if not joint_hierarchy:
            QtWidgets.QMessageBox.warning(self, "Paste Failed", "Joint hierarchy not found.")
            return

        # 4. Load Data
        try:
            with open(filepath, 'r') as f:
                json_data = json.load(f)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Paste Failed", "Error loading JSON: {}".format(e))
            return

        # Convert list to dict for faster lookup: {"pelvis": {...data...}, "spine": ...}
        data_map = {}
        for item in json_data:
            if "name" in item:
                data_map[item["name"]] = item

        # 5. Apply Data
        count = 0
        cmds.undoInfo(openChunk=True)
        try:
            for joint in joint_hierarchy:
                # Remove namespace for matching: "char:pelvis" -> "pelvis"
                clean_name = unicode(joint).split(":")[-1]

                if clean_name in data_map:
                    joint_data = data_map[clean_name]
                    
                    # Apply Translate
                    if apply_translate and "translate" in joint_data:
                        t = joint_data["translate"]
                        try:
                            cmds.setAttr("{}.translate".format(joint), t["x"], t["y"], t["z"])
                        except:
                            print("Skipped translate for {}".format(joint))

                    # Apply Rotate
                    if apply_rotate and "rotate" in joint_data:
                        r = joint_data["rotate"]
                        try:
                            cmds.setAttr("{}.rotate".format(joint), r["x"], r["y"], r["z"])
                        except:
                            print("Skipped rotate for {}".format(joint))
                    
                    count += 1
        except Exception as e:
             cmds.warning("Error applying data: {}".format(e))
        finally:
            cmds.undoInfo(closeChunk=True)

        print("Applied transform data to {} joints.".format(count))

    def connect_signals(self):
        if not hasattr(self, 'ui'):
            return
            
        self.ui.btnRefreshProjects.clicked.connect(self.refresh_projects)
        self.ui.btnAddProject.clicked.connect(self.create_project)
        self.ui.btnRemoveProject.clicked.connect(self.delete_project)
        self.ui.cmbProjects.currentIndexChanged.connect(self.refresh_characters)

        self.ui.btnAddCharacter.clicked.connect(self.add_character)
        self.ui.btnRemoveCharacter.clicked.connect(self.remove_character)
        if hasattr(self.ui, "btnRefreshCharacters"):
            self.ui.btnRefreshCharacters.clicked.connect(self.refresh_characters)

        self.ui.btnAddRoot.clicked.connect(self.add_root)
        self.ui.btnRemoveRoot.clicked.connect(self.remove_root)

        self.ui.btnCopyTemp.clicked.connect(self.copy_transform_data)
        # --- Connect Paste Button ---
        self.ui.btnPasteTemp.clicked.connect(self.paste_transform_data)

        self.ui.btnChangeTangents.clicked.connect(lambda: cmds.warning("Change tangents clicked"))
        self.ui.btnKeyAll.clicked.connect(lambda: cmds.warning("Key All Keyable clicked"))

# -------------------------------------------------
def show_jspl_anims_tool():
    if cmds.window(WINDOW_NAME, exists=True):
        cmds.deleteUI(WINDOW_NAME)

    parent = maya_main_window()
    window = JSPLTransformTool(parent)
    window.show()
    return window

# -------------------------------------------------
# EXECUTE
show_jspl_anims_tool()
