import maya.cmds as cmds
import maya.mel as mel

# --- Toggle, reset ---

def reset_rotate(*args):
    selection = cmds.ls(selection=True, type='joint')
    if not selection:
        cmds.warning("Select =>1 jnt.")
        return
    for joint in selection:
        cmds.setAttr(joint + ".rotateX", 0)
        cmds.setAttr(joint + ".rotateY", 0)
        cmds.setAttr(joint + ".rotateZ", 0)
    for axis in ['X', 'Y', 'Z']:
        slider = 'q{}Slider'.format(axis)
        if cmds.control(slider, exists=True):
            cmds.intSlider(slider, edit=True, value=0)

def toggle_selection_display(*args):
    model_panels = cmds.getPanel(type='modelPanel')
    for panel in model_panels:
        current_state = cmds.modelEditor(panel, query=True, sel=True)
        cmds.modelEditor(panel, edit=True, sel=not current_state)

def hide_jnts(*args):
    model_panels = cmds.getPanel(type='modelPanel')
    for panel in model_panels:
        current_state = cmds.modelEditor(panel, query=True, joints=True)
        cmds.modelEditor(panel, edit=True, joints=not current_state)

def toggle_color_feedback(*args):
    ctx = mel.eval('currentCtx')
    if not ctx.startswith('artAttrSkin'):
        cmds.warning("Open Paint Skin Weights Tool!")
        return
    current_state = mel.eval('artAttrSkinPaintCtx -q -colorfeedback {}'.format(ctx))
    new_state = not current_state
    mel.eval('artAttrSkinPaintCtx -e -colorfeedback {} {}'.format(str(new_state).lower(), ctx))
    mel.eval('toolPropertyShow;')

def set_skin_weight_value(value):
    try:
        ctx = mel.eval('currentCtx')
        if ctx.startswith('artAttrSkin'):
            mel.eval('artAttrSkinPaintCtx -e -value {} {}'.format(value, ctx))
            mel.eval('toolPropertyShow;')
        else:
            cmds.warning("Open Paint Skin Weights Tool first.")
    except:
        cmds.warning("Failed to set value. Make sure Paint Skin Weights Tool is active.")

def launch_paint_skin_weights(*args):
    mel.eval('ArtPaintSkinWeightsToolOptions;')

# --- Rotator ---

def dflt(*args):
    for axis in ['X', 'Y', 'Z']:
        reset_axis(axis)

def reset_axis(axis, *args):
    try:
        selJnt = mel.eval('artAttrSkinPaintCtx -query -inf `currentCtx -query`')
        cmds.setAttr(selJnt + '.rotate' + axis, 0)
        cmds.intSlider('q{}Slider'.format(axis), edit=True, value=0)
    except:
        cmds.warning("Paint Skin Weights Tool is active and joint is selected.")

def RotX(value):
    try:
        selJnt = mel.eval('artAttrSkinPaintCtx -query -inf `currentCtx -query`')
        cmds.setAttr(selJnt + '.rotateX', value)
    except:
        cmds.warning("Invalid joint")

def RotY(value):
    try:
        selJnt = mel.eval('artAttrSkinPaintCtx -query -inf `currentCtx -query`')
        cmds.setAttr(selJnt + '.rotateY', value)
    except:
        cmds.warning("Invalid joint")

def RotZ(value):
    try:
        selJnt = mel.eval('artAttrSkinPaintCtx -query -inf `currentCtx -query`')
        cmds.setAttr(selJnt + '.rotateZ', value)
    except:
        cmds.warning("Invalid joint")

# --- Vis toggles ---

def toggle_visibility(pattern):
    geo_list = cmds.ls(pattern, long=True)
    if not geo_list:
        cmds.warning("None found matching pattern: {}".format(pattern))
        return
    any_hidden = any(not cmds.getAttr(obj + ".visibility") for obj in geo_list if cmds.objExists(obj + ".visibility"))
    if any_hidden:
        cmds.showHidden(geo_list)
    else:
        cmds.hide(geo_list)

def toggle_cdt_objects(*args):
    all_objects = cmds.ls(type="transform", long=True)
    cdt_objects = [obj for obj in all_objects if 'cdt' in obj.lower()]
    if not cdt_objects:
        cmds.warning("No objects with 'cdt' found.")
        return
    any_visible = any(cmds.getAttr(obj + ".visibility") for obj in cdt_objects if cmds.objExists(obj + ".visibility"))
    if any_visible:
        cmds.hide(cdt_objects)
    else:
        cmds.showHidden(cdt_objects)

# --- Vis Lock ---

def vis_lock(*args):
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("Nothing selected.")
        return

    for obj in selection:
        attr = obj + ".visibility"
        try:
            is_locked = cmds.getAttr(attr, lock=True)
            is_visible = cmds.getAttr(attr)

            if not is_visible and is_locked:
                cmds.setAttr(attr, lock=False)
                cmds.setAttr(attr, 1)
            else:
                cmds.setAttr(attr, lock=False)
                cmds.setAttr(attr, 0)
                cmds.setAttr(attr, lock=True)
        except:
            pass  

# --- UI ---

def jspl_multitools_ui_v3():
    window_name = "jspl_multitools_ui_v3"
    ctrl_name   = window_name + "WorkspaceControl"

    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    if cmds.workspaceControl(ctrl_name, exists=True):
        cmds.deleteUI(ctrl_name)


    cmds.window(window_name, title="jspl_multitools", widthHeight=(300, 500), sizeable=True)
    cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnAlign="center")

    # --- Layout ---
    cmds.separator(style='in', height=10)
    cmds.rowLayout(numberOfColumns=3, adjustableColumn=1, columnAttach=(1, 'both', 5))
    cmds.button(label="Toggle LODs", command=lambda x: toggle_visibility("*LOD*"))
    cmds.button(label="Toggle CDT", command=toggle_cdt_objects)
    cmds.button(label="Toggle Vis", command=vis_lock)
    cmds.setParent('..')

    cmds.separator(style='in', height=10)
    cmds.text(label="Reset rotation for selected joints")
    cmds.button(label="Reset selected jnt (X/Y/Z)", command=reset_rotate)

    cmds.separator(style='in', height=10)
    cmds.button(label="Toggle Joints Display", command=hide_jnts)
    cmds.button(label="Toggle Selection Display", command=toggle_selection_display)

    cmds.separator(style='in', height=10)
    cmds.text(label="Paint Skin Weights Tool")
    cmds.button(label="Color", command=launch_paint_skin_weights, height=30)

    cmds.rowColumnLayout(numberOfColumns=7, columnSpacing=[(i, 5) for i in range(1, 8)], rowSpacing=(1, 5))
    for val in [1.0, 0.95, 0.75, 0.5, 0.25, 0.05, 0.0]:
        cmds.button(label=str(val), width=40, height=25, command=lambda x, v=val: set_skin_weight_value(v))
    cmds.setParent('..')

    cmds.button(label="Toggle Color Feedback", command=toggle_color_feedback)

    cmds.separator(style='in', height=10)
    cmds.text(label="Rotator")

    # --- X ---
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(20, 180, 50), adjustableColumn=2, columnAlign3=("right", "left", "left"))
    cmds.text(label="    X:  ")
    cmds.intSlider('qXSlider', min=-100, max=100, value=0, step=1, dc=RotX)
    cmds.button(label="    0    ", command=lambda *args: reset_axis('X'))
    cmds.setParent('..')

    # --- Y ---
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(20, 180, 50), adjustableColumn=2, columnAlign3=("right", "left", "left"))
    cmds.text(label="    Y:  ")
    cmds.intSlider('qYSlider', min=-100, max=100, value=0, step=1, dc=RotY)
    cmds.button(label="    0    ", command=lambda *args: reset_axis('Y'))
    cmds.setParent('..')

    # --- Z ---
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(20, 180, 50), adjustableColumn=2, columnAlign3=("right", "left", "left"))
    cmds.text(label="    Z:  ")
    cmds.intSlider('qZSlider', min=-100, max=100, value=0, step=1, dc=RotZ)
    cmds.button(label="    0    ", command=lambda *args: reset_axis('Z'))
    cmds.setParent('..')

    cmds.button(label="Reset (X/Y/Z)", command=dflt)
    cmds.separator(style='in', height=10)

    # --- Dock ---
    cmds.workspaceControl(
        ctrl_name,
        label="jspl_multitools",
        retain=True,
        initialWidth=300,
        initialHeight=500,
        dockToMainWindow=("left", 1),   
        uiScript="cmds.control('{}', e=True, p='{}')".format(window_name, ctrl_name)
    )



jspl_multitools_ui_v3()
