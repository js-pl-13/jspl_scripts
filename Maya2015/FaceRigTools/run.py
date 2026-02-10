# -*- coding: utf-8 -*-
import sys
import os

# _______________________________________________________________________________________________________________________________________________
TOOL_PATH = r"D:\!GIT\jspl_scripts\Maya2015\FaceRigTools"

def run_face_rig_tool():

    if not os.path.exists(TOOL_PATH):
        import maya.cmds as cmds
        cmds.error(u"Path not found: {}. Check the connection to the disk".format(TOOL_PATH))
        return

    if TOOL_PATH not in sys.path:
        sys.path.append(TOOL_PATH)

    try:
        import main_ui
        reload(main_ui)
        
        if hasattr(main_ui, 'LocatorsTool'):
            main_ui.LocatorsTool()
            
    except ImportError as e:
        import maya.cmds as cmds
        cmds.error(u"Import error \nLog: {}".format(e))
    except Exception as e:
        import maya.cmds as cmds
        cmds.error(u"Critical error: {}".format(e))

run_face_rig_tool()
#_______________________________________________________________________________________________________________________________________________