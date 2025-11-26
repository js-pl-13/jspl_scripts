# HotKey Alt+W

import maya.cmds as cmds
import cStringIO

def jspl_copy_weights_from_first_selected_vertex():
    #_____________UI  Get ordered vertex selection
    selection = cmds.ls(orderedSelection=True, flatten=True)

    #_____________UI  Filter only vertices
    verts = [v for v in selection if '.vtx[' in v]

    if len(verts) < 2:
        cmds.error("Please select at least 2 vertices!")

    #_____________UI  Use FIRST selected vertex as source
    source_vert = verts[0]

    #_____________UI  All others are targets
    target_verts = verts[1:]

    #_____________UI  Detect mesh
    base_mesh = source_vert.split('.')[0]

    #_____________UI  Find skinCluster
    history = cmds.listHistory(base_mesh)
    skinClusters = cmds.ls(history, type='skinCluster')
    if not skinClusters:
        cmds.error("No skinCluster found on mesh: {}".format(base_mesh))
    skinClusterName = skinClusters[0]

    #_____________UI  Query influences and weights from source vertex
    influences = cmds.skinCluster(skinClusterName, q=True, inf=True)
    weights = cmds.skinPercent(skinClusterName, source_vert, query=True, value=True)

    #_____________UI  Build skinPercent command
    cmds.select(target_verts)
    command = cStringIO.StringIO()
    command.write('cmds.skinPercent("{}", transformValue=['.format(skinClusterName))

    for i, (inf, w) in enumerate(zip(influences, weights)):
        command.write('("{}", {})'.format(inf, w))
        if i != len(influences) - 1:
            command.write(', ')

    command.write('], normalize=False, zeroRemainingInfluences=True)')

    #_____________UI  Execute with Undo chunk
    cmds.undoInfo(openChunk=True)
    try:
        eval(command.getvalue())
    finally:
        cmds.undoInfo(closeChunk=True)

    print("Copied weights from {} to {} vertices.".format(source_vert, len(target_verts)))

#_____________RUN
jspl_copy_weights_from_first_selected_vertex()

