#Hotkey Alt+4

import maya.cmds as cmds

if cmds.selectType(q=True, joint=True):
    cmds.selectType(joint=False)
else:
    cmds.selectType(joint=True)
	