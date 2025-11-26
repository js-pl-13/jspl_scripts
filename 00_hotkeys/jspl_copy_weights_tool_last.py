# Hotkey Alt+2

import maya.cmds as cmds
import cStringIO

#_____________FUNCTION
def jspl_copy_weights_from_last_selected_vertex():
    """
    Copy skin weights from the last selected vertex to all other selected vertices.
    The last vertex is treated as the source; all others receive its weights.
    """

    #_____________SELECTION
    selection = cmds.ls(orderedSelection=True, flatten=True)

    #_____________VERTEX_FILTER
    verts = [v for v in selection if '.vtx[' in v]

    if len(verts) < 2:
        cmds.error("Please select at least 2 vertices!")

    #_____________SOURCE_TARGET
    source_vert = verts[-1]
    target_verts = verts[:-1]

    base_mesh = source_vert.split('.')[0]

    #_____________SKINCLUSTER_FIND
    history = cmds.listHistory(base_mesh)
    skinClusters = cmds.ls(history, type='skinCluster')
    if not skinClusters:
        cmds.error("No skinCluster found on mesh: {}".format(base_mesh))
    skinClusterName = skinClusters[0]

    #_____________READ_WEIGHTS
    influences = cmds.skinCluster(skinClusterName, q=True, inf=True)
    weights = cmds.skinPercent(skinClusterName, source_vert, query=True, value=True)

    #_____________BUILD_COMMAND
    cmds.select(target_verts)
    command = cStringIO.StringIO()
    command.write('cmds.skinPercent("{}", transformValue=['.format(skinClusterName))

    for i, (inf, w) in enumerate(zip(influences, weights)):
        command.write('("{}", {})'.format(inf, w))
        if i != len(influences) - 1:
            command.write(', ')

    command.write('], normalize=False, zeroRemainingInfluences=True)')

    #_____________EXECUTE_UNDO
    cmds.undoInfo(openChunk=True)
    try:
        eval(command.getvalue())
    finally:
        cmds.undoInfo(closeChunk=True)

    print("Copied weights from {} to {} vertices.".format(source_vert, len(target_verts)))


#_____________RUN
jspl_copy_weights_from_last_selected_vertex()
