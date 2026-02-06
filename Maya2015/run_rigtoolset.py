import maya.cmds as cmds
from sys import path

netpath = 'U:\\AssetStorage\\CharTools\\'

## set RigToolset path
path.append(netpath)
## importing modules
from RigToolset import skinToolset, skelToolset, outsToolset
## creating objects
skinningTools = skinToolset._skinToolset()
skeletonTools = skelToolset._skelToolset()
outsourceTools = outsToolset._outsToolset()

if not cmds.window( 'RigToolset', exists=True):
    dialog1 = cmds.loadUI(f=netpath+'RigToolset\\rigging_toolset.ui')
    cmds.showWindow(dialog1)
else:
    cmds.inViewMessage( amg='RigToolset <hl> allready run!</hl>', pos='midCenter', fade=True )
