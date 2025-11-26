#Hotkey Alt+R
import maya.cmds as cmds

#_____________FUNCTION
def jspl_reset_joint_rotate(*args):
    """
    Reset rotation of selected joints to zero on X, Y, Z axes.
    """

    #_____________UI  Get selected joints
    selection = cmds.ls(selection=True, type='joint')
    if not selection:
        cmds.warning("Select at least one joint.")
        return

    #_____________UI  Reset rotation for each joint
    for joint in selection:
        for axis in ("X", "Y", "Z"):
            attr = joint + ".rotate" + axis
            if not cmds.getAttr(attr, lock=True):
                try:
                    cmds.setAttr(attr, 0)
                except Exception as e:
                    cmds.warning("Failed to reset {}: {}".format(attr, e))

#_____________UI  Run function
jspl_reset_joint_rotate()
