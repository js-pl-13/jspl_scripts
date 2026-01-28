import maya.cmds as cmds
import maya.mel as mel

WINDOW_NAME = "locators_on_mesh_ui"


def fix_locators_on_mesh(target_mesh):
    """
    Create fixed locators for *_pos transforms and attach them
    to the closest polygon faces on the given mesh.
    """
    if not target_mesh or not cmds.objExists(target_mesh):
        cmds.error("Invalid mesh")

    mesh_shapes = cmds.listRelatives(target_mesh, shapes=True, path=True)
    if not mesh_shapes:
        cmds.error("Mesh has no shape")

    mesh_shape = mesh_shapes[0]
    bad_loc_list = cmds.ls("*_pos", type="transform")

    if not bad_loc_list:
        cmds.warning("No *_pos locators found")
        return

    cpm_node = cmds.createNode("closestPointOnMesh")
    cmds.connectAttr(mesh_shape + ".outMesh", cpm_node + ".inMesh", force=True)

    created_locs = []

    for bad_loc in bad_loc_list:
        fixed_loc = cmds.spaceLocator(n=bad_loc + "_fixed")[0]

        constraint = cmds.parentConstraint(bad_loc, fixed_loc, mo=False)[0]
        cmds.delete(constraint)

        pos = cmds.xform(fixed_loc, q=True, ws=True, t=True)
        cmds.setAttr(cpm_node + ".inPosition", pos[0], pos[1], pos[2], type="double3")

        face_index = cmds.getAttr(cpm_node + ".closestFaceIndex")
        face = "{0}.f[{1}]".format(target_mesh, face_index)

        cmds.pointOnPolyConstraint(face, fixed_loc, mo=True)

        created_locs.append(fixed_loc)

    cmds.delete(cpm_node)

    if created_locs:
        cmds.select(created_locs)


def set_blendshapes_to_zero(target_mesh):
    """
    Set all blendShape weights connected to the mesh to zero.
    """
    if not target_mesh or not cmds.objExists(target_mesh):
        cmds.error("Invalid mesh")

    history = cmds.listHistory(target_mesh, pruneDagObjects=True) or []
    blendshapes = cmds.ls(history, type="blendShape")

    if not blendshapes:
        cmds.warning("No blendShape nodes found")
        return

    for bs in blendshapes:
        weights = cmds.listAttr(bs + ".weight", m=True) or []
        for w in weights:
            cmds.setAttr(bs + "." + w, 0)



def delete_constraints_on_fixed_locs():
    """
    Find *_pos_fixed* transforms, select their hierarchies
    and delete constraints using MEL.
    """
    roots = cmds.ls("*_pos_fixed*", type="transform")

    if not roots:
        cmds.warning("No *_pos_fixed* objects found")
        return

    cmds.select(clear=True)

    for root in roots:
        cmds.select(root, add=True)
        mel.eval("select -hi;")

    mel.eval("delete -constraints;")


def add_mesh_to_field(field):
    """
    Put selected transform name into the text field.
    """
    sel = cmds.ls(sl=True, transforms=True)
    if sel:
        cmds.textField(field, e=True, text=sel[0])
    else:
        cmds.warning("Nothing selected")


def clear_field(field):
    """
    Clear text field.
    """
    cmds.textField(field, e=True, text="")


def run_fix(field):
    """
    Run locator fixing using mesh from UI.
    """
    mesh = cmds.textField(field, q=True, text=True)
    fix_locators_on_mesh(mesh)


def run_blendshape_zero(field):
    """
    Set blendShape weights to zero using mesh from UI.
    """
    mesh = cmds.textField(field, q=True, text=True)
    set_blendshapes_to_zero(mesh)


def locators_on_mesh_ui():
    if cmds.window(WINDOW_NAME, exists=True):
        cmds.deleteUI(WINDOW_NAME)

    cmds.window(WINDOW_NAME, title="Locators On Mesh", sizeable=True)
    cmds.columnLayout(adj=True, rowSpacing=6)

    cmds.text(label="Target Mesh")
    mesh_field = cmds.textField()

    cmds.rowLayout(nc=2, adj=1)
    cmds.button(label="Add", c=lambda *_: add_mesh_to_field(mesh_field))
    cmds.button(label="Remove", c=lambda *_: clear_field(mesh_field))
    cmds.setParent("..")

    cmds.separator(h=8, style="in")
    cmds.button(label="Run", c=lambda *_: run_fix(mesh_field))
    cmds.separator(h=8, style="in")    
    cmds.button(
        label="Set BlendShapes To Zero",
        c=lambda *_: run_blendshape_zero(mesh_field)
    )
    cmds.separator(h=8, style="in")
    cmds.button(
        label="Delete constraints on _pos_fixed locators",
        c=lambda *_: delete_constraints_on_fixed_locs()
    )
    cmds.separator(h=8, style="in")
    cmds.showWindow(WINDOW_NAME)


locators_on_mesh_ui()
