# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------------------

This script is used to automatically configure or delete
multiplyDivide utility nodes that invert the X-axis rotation between paired joints.

Этот скрипт используется для автоматической настройки или удаления
узлов утилиты multiplyDivide, которые инвертируют поворот по оси X между парными джоинтами
------------------------------------------------------------------------------------------


Author: js.pl
Compatible with: Autodesk Maya 2019, Python 2.7
"""

# --- Connection settings ---
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

# ---Create MultiplyDivide node ---
def create_multiply_divide(source, target):
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

# --- Delete MultiplyDivide node ---
def delete_multiply_divide(source, target):
    md_name = "{}_to_{}_md".format(source, target)
    if cmds.objExists(md_name):
        cmds.delete(md_name)
        print("Deleted multiplyDivide:", md_name)
    else:
        cmds.warning("Node {} not found.".format(md_name))

# --- UI functions ---
def select_all(checkboxes, state=True):
    for cb in checkboxes:
        cmds.checkBox(cb, e=True, v=state)

def apply_connections(checkboxes):
    for cb, (src, dst) in zip(checkboxes, CONNECTIONS):
        if cmds.checkBox(cb, q=True, v=True):
            create_multiply_divide(src, dst)

def remove_connections(checkboxes):
    for cb, (src, dst) in zip(checkboxes, CONNECTIONS):
        if cmds.checkBox(cb, q=True, v=True):
            delete_multiply_divide(src, dst)

# --- Main UI ---
def run_md_tool():
    if cmds.window("mdToolWin", exists=True):
        cmds.deleteUI("mdToolWin")
    window = cmds.window("mdToolWin", title="jspl_MD_X-axis", widthHeight=(210, 500), sizeable=True)
    cmds.scrollLayout(hst=0)
    cmds.columnLayout(adjustableColumn=True, rowSpacing=8)

    # --- Create connections ---
    cmds.frameLayout(label="Create bone connections", collapsable=True, collapse=False)
    create_checkboxes = []
    for src, dst in CONNECTIONS:
        cb = cmds.checkBox(label="{} → {}".format(src, dst), v=True)
        create_checkboxes.append(cb)
    cmds.rowLayout(nc=2, adjustableColumn=2)
    cmds.button(label="Select All", c=lambda x: select_all(create_checkboxes, True))
    cmds.button(label="Deselect All", c=lambda x: select_all(create_checkboxes, False))
    cmds.setParent("..")
    cmds.button(label="Create Connections", bgc=(0.4, 0.7, 0.4), c=lambda x: apply_connections(create_checkboxes))
    cmds.setParent("..")

    # --- Delete connections ---
    cmds.frameLayout(label="Remove bone connections", collapsable=True, collapse=False)
    delete_checkboxes = []
    for src, dst in CONNECTIONS:
        cb = cmds.checkBox(label="{} → {}".format(src, dst), v=True)
        delete_checkboxes.append(cb)
    cmds.rowLayout(nc=2, adjustableColumn=2)
    cmds.button(label="Select All", c=lambda x: select_all(delete_checkboxes, True))
    cmds.button(label="Deselect All", c=lambda x: select_all(delete_checkboxes, False))
    cmds.setParent("..")
    cmds.button(label="Remove Connections", bgc=(0.7, 0.4, 0.4), c=lambda x: remove_connections(delete_checkboxes))
    cmds.setParent("..")

    cmds.showWindow(window)


if __name__ == "__main__":
    run_md_tool()
