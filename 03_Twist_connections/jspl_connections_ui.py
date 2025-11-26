# -*- coding: utf-8 -*-
import maya.cmds as cmds

#_____________CONNECTIONS
CONNECTIONS = [
    ("l_shoulder", "l_shoulder_twist_01"),
    ("r_shoulder", "r_shoulder_twist_01"),
    ("l_forearm", "l_forearm_twist_01"),
    ("r_forearm", "r_forearm_twist_01"),
    ("l_hip", "l_hip_twist_01"),
    ("r_hip", "r_hip_twist_01"),
    ("l_leg", "l_leg_twist_01"),
    ("r_leg", "r_leg_twist_01"),
]


#_____________FUNCTION
def jspl_create_multiply_divide(source, target):
    """
    Create a multiplyDivide node that connects source.rotateX
    to target.rotateX with a multiplier of -1.
    """
    md_name = "{}_to_{}_md".format(source, target)

    if cmds.objExists(md_name):
        cmds.warning("Node {} already exists.".format(md_name))
        return

    if not cmds.objExists(source) or not cmds.objExists(target):
        cmds.warning("Objects {} or {} do not exist.".format(source, target))
        return

    md_node = cmds.createNode("multiplyDivide", name=md_name)
    cmds.setAttr(md_node + ".input2X", -1)

    cmds.connectAttr(source + ".rotateX", md_node + ".input1X", force=True)
    cmds.connectAttr(md_node + ".outputX", target + ".rotateX", force=True)

    print("Created multiplyDivide:", md_name)


#_____________FUNCTION
def jspl_delete_multiply_divide(source, target):
    """
    Delete the multiplyDivide node created between
    the given source and target.
    """
    md_name = "{}_to_{}_md".format(source, target)

    if cmds.objExists(md_name):
        cmds.delete(md_name)
        print("Deleted multiplyDivide:", md_name)
    else:
        cmds.warning("Node {} not found.".format(md_name))


#_____________FUNCTION
def jspl_select_all(checkboxes, state=True):
    """
    Set all checkboxes to the given state (True/False).
    """
    for cb in checkboxes:
        cmds.checkBox(cb, e=True, v=state)


#_____________FUNCTION
def jspl_apply_connections(checkboxes):
    """
    Create multiplyDivide nodes for all pairs where
    the corresponding checkbox is enabled.
    """
    for cb, (src, dst) in zip(checkboxes, CONNECTIONS):
        if cmds.checkBox(cb, q=True, v=True):
            jspl_create_multiply_divide(src, dst)


#_____________FUNCTION
def jspl_remove_connections(checkboxes):
    """
    Remove multiplyDivide nodes for all pairs where
    the corresponding checkbox is enabled.
    """
    for cb, (src, dst) in zip(checkboxes, CONNECTIONS):
        if cmds.checkBox(cb, q=True, v=True):
            jspl_delete_multiply_divide(src, dst)


#_____________UI
def jspl_connections_ui():
    if cmds.window("jspl_mdToolWin", exists=True):
        cmds.deleteUI("jspl_mdToolWin")

    window = cmds.window("jspl_mdToolWin", title="jspl_twist_connections", widthHeight=(210, 510), sizeable=True)
    cmds.scrollLayout(hst=0)
    cmds.columnLayout(adjustableColumn=True, rowSpacing=8)

    #_____________UI Create connections
    cmds.frameLayout(label="Create bone connections", collapsable=True, collapse=False)
    create_checkboxes = []
    for src, dst in CONNECTIONS:
        cb = cmds.checkBox(label="{} > {}".format(src, dst), v=True)
        create_checkboxes.append(cb)

    cmds.rowLayout(nc=2, adjustableColumn=2)
    cmds.button(label="Select All", c=lambda x: jspl_select_all(create_checkboxes, True))
    cmds.button(label="Deselect All", c=lambda x: jspl_select_all(create_checkboxes, False))
    cmds.setParent("..")

    cmds.button(label="Create Connections", bgc=(0.4, 0.7, 0.4),
                c=lambda x: jspl_apply_connections(create_checkboxes))
    cmds.setParent("..")

    #_____________UI Delete connections
    cmds.frameLayout(label="Remove bone connections", collapsable=True, collapse=False)
    delete_checkboxes = []
    for src, dst in CONNECTIONS:
        cb = cmds.checkBox(label="{} > {}".format(src, dst), v=True)
        delete_checkboxes.append(cb)

    cmds.rowLayout(nc=2, adjustableColumn=2)
    cmds.button(label="Select All", c=lambda x: jspl_select_all(delete_checkboxes, True))
    cmds.button(label="Deselect All", c=lambda x: jspl_select_all(delete_checkboxes, False))
    cmds.setParent("..")

    cmds.button(label="Remove Connections", bgc=(0.7, 0.4, 0.4),
                c=lambda x: jspl_remove_connections(delete_checkboxes))
    cmds.setParent("..")

    cmds.showWindow(window)


#_____________RUN
jspl_connections_ui()
