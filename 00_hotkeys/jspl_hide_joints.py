# Hotkey Alt+X

import maya.cmds as cmds

def jspl_hide_joints():
    """
    Toggle the visibility of joints across multiple model panels.
    The function iterates through a predefined list of model panel indices,
    checks whether each panel exists, retrieves the current joint visibility state,
    and flips it.
    """
    #_____________PANEL_LOOKUP
    model_panels = cmds.getPanel(type='modelPanel')
    if not model_panels:
        cmds.warning("No model panels found")
        return

    #_____________INDICES
    indices_to_toggle = [1, 2, 3, 4, 5, 6, 7, 8]

    #_____________TOGGLE
    for index in indices_to_toggle:
        if index < len(model_panels):
            panel = model_panels[index]
            current_state = cmds.modelEditor(panel, query=True, joints=True)
            cmds.modelEditor(panel, edit=True, joints=not current_state)


#_____________EXECUTE
jspl_hide_joints()
