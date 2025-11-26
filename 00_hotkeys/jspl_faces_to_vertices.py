#Hotkey Alt+3
import maya.cmds as cmds

#_____________FUNCTION
def jspl_faces_to_vertices():
    """
    Convert selected polygon faces to vertices and open Paint Skin Weights Tool.
    """

    #_____________UI  Get current selection
    sel = cmds.ls(sl=True, fl=True)
    if not sel:
        cmds.warning("Nothing is selected.")
        return

    #_____________UI  Convert selected polygon faces to vertices
    verts = cmds.polyListComponentConversion(sel, toVertex=True)
    verts = cmds.filterExpand(verts, sm=31)  # sm=31 means vertices
    if not verts:
        cmds.warning("Failed to convert faces to vertices.")
        return

    #_____________UI  Select vertices
    cmds.select(verts, r=True)

    #_____________UI  Launch Paint Skin Weights Tool
    cmds.ArtPaintSkinWeightsTool()

#_____________UI  Run function
jspl_faces_to_vertices()