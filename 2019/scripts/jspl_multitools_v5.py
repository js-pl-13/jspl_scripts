import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import math

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

# --- Visibility toggles ---

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
# --- Create jnt tool ---
def get_selected_vertices():
    selection = cmds.ls(selection=True, flatten=True)
    if not selection:
        return []
    
    verts = []
    for obj in selection:
        if ".f[" in obj:  # face selected
            face_verts = cmds.polyListComponentConversion(obj, fromFace=True, toVertex=True)
            face_verts = cmds.ls(face_verts, flatten=True)
            verts.extend(face_verts)
        elif ".e[" in obj:  # edge selected
            edge_verts = cmds.polyListComponentConversion(obj, fromEdge=True, toVertex=True)
            edge_verts = cmds.ls(edge_verts, flatten=True)
            verts.extend(edge_verts)
        elif ".vtx[" in obj:  # vertex selected
            verts.append(obj)
    
    verts = list(set(verts))  # remove duplicates
    return verts


def joint_on_average_vertex():
    verts = get_selected_vertices()
    if len(verts) < 2:
        cmds.warning("You need to select at least 2 vertices/edges/faces for averaging.")
        return
    
    total_pos = [0.0, 0.0, 0.0]
    for vert in verts:
        pos = cmds.xform(vert, query=True, translation=True, worldSpace=True)
        total_pos[0] += pos[0]
        total_pos[1] += pos[1]
        total_pos[2] += pos[2]
    
    count = len(verts)
    avg_pos = [total_pos[0]/count, total_pos[1]/count, total_pos[2]/count]
    
    cmds.select(clear=True)
    cmds.joint(position=avg_pos)


def joint_on_each_vertex():
    verts = get_selected_vertices()
    if not verts:
        cmds.warning("Please select at least one vertex/edge/face.")
        return
    
    for vert in verts:
        pos = cmds.xform(vert, query=True, translation=True, worldSpace=True)
        cmds.select(clear=True)
        cmds.joint(position=pos)


def joint_on_transforms():
    """
    Creates joints for selected transform objects and snaps them to position.
    """
    selected = cmds.ls(selection=True, type='transform')
    if not selected:
        cmds.warning("No transform objects selected for joint creation.")
        return

    joints = []
    for obj in selected:
        joint = cmds.createNode('joint')
        constraint = cmds.parentConstraint(obj, joint, mo=False)[0]
        cmds.delete(constraint)
        joints.append(joint)

    cmds.select(joints)
# --- Create proxy ---
skip_rotation = False
add_extra_edges = False
place_in_group = False  

def get_selected_points():
    """Return list of MVector from selected components (verts/edges/faces)"""
    sel = cmds.ls(selection=True, flatten=True)
    if not sel:
        om.MGlobal.displayError("Please select vertices, edges or faces.")
        return None

    verts = []
    for s in sel:
        if ".vtx[" in s:  # already vertex
            verts.append(s)
        elif ".e[" in s:  # edge > convert to verts
            verts.extend(cmds.ls(cmds.polyListComponentConversion(s, toVertex=True), flatten=True))
        elif ".f[" in s:  # face > convert to verts
            verts.extend(cmds.ls(cmds.polyListComponentConversion(s, toVertex=True), flatten=True))
        else:
            # if object itself selected > take all verts
            verts.extend(cmds.ls(cmds.polyListComponentConversion(s, toVertex=True), flatten=True))

    verts = list(set(verts))
    if not verts:
        om.MGlobal.displayError("No vertices found from selection.")
        return None

    points = []
    for v in verts:
        pos = cmds.pointPosition(v, world=True)
        points.append(om.MVector(pos[0], pos[1], pos[2]))
    return points

def compute_center_and_normal(points):
    """Compute center and approximate normal from selected points"""
    center = om.MVector(0, 0, 0)
    for p in points:
        center += p
    center /= len(points)

    v1 = points[0] - center
    v2 = points[len(points)//2] - center
    normal = (v1 ^ v2).normal()

    if normal.length() < 1e-6:
        normal = om.MVector(0, 1, 0)

    return center, normal

def align_object_to_normal(obj, normal):
    """Rotate object so that its Y axis aligns with given normal"""
    global skip_rotation
    if skip_rotation:
        return

    up = om.MVector(0, 1, 0)
    axis = up ^ normal
    dot = max(-1, min(1, up * normal))
    angle = math.degrees(math.acos(dot))
    if axis.length() > 1e-6:
        cmds.rotate(angle*axis.x, angle*axis.y, angle*axis.z, obj,
                    relative=True, os=True, fo=True)

def scale_object_to_points(obj, points):
    """Scale object to cover bounding box of points"""
    bbox_min = [min(p.x for p in points), min(p.y for p in points), min(p.z for p in points)]
    bbox_max = [max(p.x for p in points), max(p.y for p in points), max(p.z for p in points)]
    size_x = bbox_max[0] - bbox_min[0]
    size_y = bbox_max[1] - bbox_min[1]
    size_z = bbox_max[2] - bbox_min[2]
    cmds.scale(size_x, size_y, size_z, obj)

def move_to_proxy_grp(obj):
    """Move created object under proxy_grp if enabled"""
    global place_in_group
    if not place_in_group:
        return 

    if cmds.objExists("proxy_grp"):
        try:
            cmds.parent(obj, "proxy_grp")
        except:
            om.MGlobal.displayWarning("Could not parent to proxy_grp.")
    else:
        om.MGlobal.displayWarning("proxy_grp does not exist.")

def create_plane_from_vertices(*args):
    points = get_selected_points()
    if not points: return
    center, normal = compute_center_and_normal(points)

    if add_extra_edges:
        obj = cmds.polyPlane(w=1, h=1, sx=4, sy=4, name="fittedPlane#")[0]
    else:
        obj = cmds.polyPlane(w=1, h=1, sx=1, sy=1, name="fittedPlane#")[0]

    align_object_to_normal(obj, normal)
    cmds.xform(obj, ws=True, t=(center.x, center.y, center.z))
    scale_object_to_points(obj, points)
    move_to_proxy_grp(obj)

    om.MGlobal.displayInfo("Plane created.")

def create_box_from_vertices(*args):
    points = get_selected_points()
    if not points: return
    center, normal = compute_center_and_normal(points)

    if add_extra_edges:
        obj = cmds.polyCube(w=1, h=1, d=1, sx=2, sy=2, sz=2, name="fittedBox#")[0]
    else:
        obj = cmds.polyCube(w=1, h=1, d=1, name="fittedBox#")[0]

    align_object_to_normal(obj, normal)
    cmds.xform(obj, ws=True, t=(center.x, center.y, center.z))
    scale_object_to_points(obj, points)
    move_to_proxy_grp(obj)

    om.MGlobal.displayInfo("Box created.")

def create_cylinder_from_vertices(*args):
    points = get_selected_points()
    if not points: return
    center, normal = compute_center_and_normal(points)

    if add_extra_edges:
        obj = cmds.polyCylinder(r=0.5, h=1, sx=32, sy=4, name="fittedCylinder#")[0]
    else:
        obj = cmds.polyCylinder(r=0.5, h=1, sx=20, sy=1, name="fittedCylinder#")[0]

    align_object_to_normal(obj, normal)
    cmds.xform(obj, ws=True, t=(center.x, center.y, center.z))
    scale_object_to_points(obj, points)
    move_to_proxy_grp(obj)

    om.MGlobal.displayInfo("Cylinder created (bbox fit).")

def create_cylinder_fit_radius(*args):
    """Cylinder with radius estimated from average distance of points"""
    points = get_selected_points()
    if not points: return
    center, normal = compute_center_and_normal(points)

    # Compute average radius in plane perpendicular to normal
    radius_sum = 0.0
    for p in points:
        vec = p - center
        proj = vec - normal * (vec * normal)  # project onto plane
        radius_sum += proj.length()
    avg_radius = radius_sum / len(points)

    # Height from bounding box
    bbox_min = [min(p.x for p in points), min(p.y for p in points), min(p.z for p in points)]
    bbox_max = [max(p.x for p in points), max(p.y for p in points), max(p.z for p in points)]
    height = max(bbox_max[0]-bbox_min[0], bbox_max[1]-bbox_min[1], bbox_max[2]-bbox_min[2])

    if add_extra_edges:
        obj = cmds.polyCylinder(r=avg_radius, h=height, sx=48, sy=4, name="fittedCylinderRadius#")[0]
    else:
        obj = cmds.polyCylinder(r=avg_radius, h=height, sx=32, sy=1, name="fittedCylinderRadius#")[0]

    align_object_to_normal(obj, normal)
    cmds.xform(obj, ws=True, t=(center.x, center.y, center.z))
    move_to_proxy_grp(obj)

    om.MGlobal.displayInfo("Cylinder created (fit radius).")

def toggle_skip_rotation(state):
    global skip_rotation
    skip_rotation = state

def toggle_extra_edges(state):
    global add_extra_edges
    add_extra_edges = state

def toggle_place_in_group(state):
    global place_in_group
    place_in_group = state

# --- UI ---

def jspl_multitools_ui_v5():
    window_name = "jspl_multitools_ui_v5"
    ctrl_name   = window_name + "WorkspaceControl"

    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    if cmds.workspaceControl(ctrl_name, exists=True):
        cmds.deleteUI(ctrl_name)

    # окно
    cmds.window(window_name, title="jspl_multitools", widthHeight=(300, 500), sizeable=True)
    cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnAlign="center")

    # --- Layout ---
    ###cmds.separator(style='in', height=1)
    cmds.rowLayout(numberOfColumns=3, adjustableColumn=1, columnAttach=(1, 'both', 5))
    cmds.button(label="Toggle LODs", command=lambda x: toggle_visibility("*LOD*"))
    cmds.button(label="Toggle CDT", command=toggle_cdt_objects)
    cmds.button(label="Toggle Vis", command=vis_lock)
    cmds.setParent('..')

    cmds.separator(style='in', height=1)
    cmds.text(label="Reset rotation for selected joints")
    cmds.button(label="Reset selected jnt (X/Y/Z)", command=reset_rotate)

    cmds.separator(style='in', height=1)
    cmds.button(label="Toggle Joints Display", command=hide_jnts)
    cmds.button(label="Toggle Selection Display", command=toggle_selection_display)

    cmds.separator(style='in', height=1)
    cmds.text(label="Paint Skin Weights Tool")
    cmds.button(label="Color", command=launch_paint_skin_weights)

    cmds.rowColumnLayout(numberOfColumns=7, columnSpacing=[(i, 5) for i in range(1, 8)], rowSpacing=(1, 5))
    for val in [1.0, 0.95, 0.75, 0.5, 0.25, 0.05, 0.0]:
        cmds.button(label=str(val), width=40, height=25, command=lambda x, v=val: set_skin_weight_value(v))
    cmds.setParent('..')

    cmds.button(label="Toggle Color Feedback", command=toggle_color_feedback)

    cmds.separator(style='in', height=1)
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
    cmds.separator(style='in', height=1)
    # --- Vertex tool --
    cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnAlign='center')
    cmds.text(label="Create jnt")
    cmds.button(label="Average create joint", command=lambda x: joint_on_average_vertex())
    cmds.button(label="Create joint(s)", command=lambda x: joint_on_each_vertex())
    cmds.button(label="Create joint on transform(s)", command=lambda x: joint_on_transforms())
    cmds.setParent('..')
    #--- Proxy tool ---
    cmds.columnLayout(adjustableColumn=True, rowSpacing=8)
    cmds.separator(h=1, style='in')
    cmds.button(label="Create Plane", command=create_plane_from_vertices)
    cmds.button(label="Create Box", command=create_box_from_vertices)
    cmds.button(label="Create Cylinder (bbox fit)", command=create_cylinder_from_vertices)
    cmds.button(label="Create Cylinder (fit radius)", command=create_cylinder_fit_radius)

    cmds.separator(h=1, style='in')

    cmds.checkBox(label="Skip rotation", value=False,
                  changeCommand=lambda state: toggle_skip_rotation(state))
    cmds.checkBox(label="Add extra edges", value=False,
                  changeCommand=lambda state: toggle_extra_edges(state))
    cmds.checkBox(label="Place in grp (proxy_grp)", value=False,
                  changeCommand=lambda state: toggle_place_in_group(state))
    cmds.setParent('..')              
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


jspl_multitools_ui_v5()
