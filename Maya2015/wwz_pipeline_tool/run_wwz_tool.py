# -*- coding: utf-8 -*-
import sys
import os
import maya.cmds as cmds

def run():
    try:
        import main_ui
        
        reload(main_ui)
        
        if hasattr(main_ui, 'LocatorsTool'):
            main_ui.LocatorsTool()
        else:
            cmds.warning("Class 'LocatorsTool' not found in main_ui.py")
            
    except ImportError as e:
        cmds.error(u"Import Error: Could not find main_ui.py in folder. Log: {}".format(e))
    except Exception as e:
        cmds.error(u"Critical Error executing WWZ Tool: {}".format(e))