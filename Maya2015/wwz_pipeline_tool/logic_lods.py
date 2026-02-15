# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
import os
import config

# _________________________________________________________________________________________

def ensure_fbx_plugin():
    if not cmds.pluginInfo("fbxmaya", query=True, loaded=True):
        try:
            cmds.loadPlugin("fbxmaya")
        except:
            print "Error: Could not load fbxmaya plugin"

def ensure_export_folder():
    if not os.path.exists(config.LOD_EXPORT_PATH):
        os.makedirs(config.LOD_EXPORT_PATH)

def get_mesh_shape(obj):
    shapes = cmds.listRelatives(obj, shapes=True, fullPath=True) or []
    for s in shapes:
        if cmds.objectType(s) == "mesh":
            return s
    return None

def get_shading_engine(obj):
    shape = get_mesh_shape(obj)
    if not shape:
        return None
    sgs = cmds.listConnections(shape, type="shadingEngine") or []
    return sgs[0] if sgs else None

def assign_material_from_source(source_obj, target_obj):
    sg = get_shading_engine(source_obj)
    if not sg:
        return
    shape = get_mesh_shape(target_obj)
    if not shape:
        return
    try:
        cmds.sets(shape, e=True, forceElement=sg)
    except:
        pass

def get_all_display_layers(obj):
    layers = cmds.listConnections(obj, type="displayLayer") or []
    return [l for l in layers if l != "defaultLayer"]

def remove_from_all_layers(obj):
    layers = get_all_display_layers(obj)
    for layer in layers:
        try:
            cmds.editDisplayLayerMembers(layer, obj, remove=True)
        except:
            pass
    return layers

def restore_layers(obj, layers):
    for layer in layers:
        if cmds.objExists(layer):
            try:
                cmds.editDisplayLayerMembers(layer, obj)
            except:
                pass

def get_meshes_from_layer(layer_name):
    if not cmds.objExists(layer_name):
        return []

    members = cmds.editDisplayLayerMembers(layer_name, query=True) or []
    meshes = []

    for obj in members:
        if cmds.objectType(obj) == "transform":
            if get_mesh_shape(obj):
                meshes.append(obj)

    return list(set(meshes))

# _____________

# _____________ Export _____________

def export_layer(layer_name):
    meshes = get_meshes_from_layer(layer_name)
    if not meshes:
        print "Layer empty or not found:", layer_name
        return

    ensure_export_folder()
    ensure_fbx_plugin()

    export_file = os.path.join(config.LOD_EXPORT_PATH, "%s.dae" % layer_name)
    export_file = export_file.replace("\\", "/")

    layer_data = {}

    # Подготовка: удаляем историю и отвязываем от слоев
    for obj in meshes:
        cmds.delete(obj, constructionHistory=True)
        layer_data[obj] = remove_from_all_layers(obj)

    cmds.select(meshes, replace=True)

    # Экспорт
    mel.eval('FBXExportShowUI -v false;')
    mel.eval('FBXExport -f "%s" -s;' % export_file)
    print "Exported:", export_file

    cmds.select(clear=True)

    # Восстановление слоев
    for obj, layers in layer_data.items():
        restore_layers(obj, layers)

def export_all_lods(*args):
    print ">>> Starting LOD Export..."
    for layer in config.EXPORT_LAYERS_LIST:
        export_layer(layer)
    print ">>> LOD Export Done."

# _____________

# _____________ Import + mat _____________

def create_lod_layers():
    for layer in config.LOD_LAYER_NAMES_FULL:
        if not cmds.objExists(layer):
            cmds.createDisplayLayer(name=layer, empty=True)

def assign_object_to_layer(obj, layer):
    if cmds.objExists(obj) and cmds.objExists(layer):
        try:
            cmds.editDisplayLayerMembers(layer, obj, noRecurse=True)
        except:
            pass

def rebuild_lod_layers_and_materials():
    create_lod_layers()

    all_transforms = cmds.ls(transforms=True) or []

    for obj in all_transforms:
        short_name = obj.split("|")[-1]

        # LOD1-5
        for i in range(1, 6):
            if short_name.endswith("_LOD%d" % i):
                assign_object_to_layer(obj, "layer_LOD%d" % i)

        # game_LOD1-5
        for i in range(1, 6):
            game_suffix = "_game_LOD%d" % i
            if short_name.endswith(game_suffix):
                base_name = short_name.replace(game_suffix, "")
                if cmds.objExists(base_name):
                    # Базовый объект в LOD0
                    assign_object_to_layer(base_name, "layer_LOD0")
                    # Копируем материал
                    assign_material_from_source(base_name, obj)

def import_all_dae(*args):
    ensure_fbx_plugin()

    if not os.path.exists(config.LOD_EXPORT_PATH):
        print "Export path not found:", config.LOD_EXPORT_PATH
        return

    files = [f for f in os.listdir(config.LOD_EXPORT_PATH) if f.lower().endswith(".dae")]
    if not files:
        print "No .dae files found."
        return

    existing_layers = set(cmds.ls(type="displayLayer") or [])

    mel.eval('FBXImportShowUI -v false;')

    for f in files:
        full_path = os.path.join(config.LOD_EXPORT_PATH, f).replace("\\", "/")
        before_objs = set(cmds.ls(transforms=True))
        
        mel.eval('FBXImport -f "%s";' % full_path)
        print "Imported:", f

        after_objs = set(cmds.ls(transforms=True))
        new_objects = list(after_objs - before_objs)

        for obj in new_objects:
            layers = cmds.listConnections(obj, type="displayLayer") or []
            for layer in layers:
                if layer != "defaultLayer":
                    try:
                        cmds.editDisplayLayerMembers(layer, obj, remove=True)
                    except:
                        pass

    current_layers = set(cmds.ls(type="displayLayer") or [])
    new_layers = current_layers - existing_layers
    for layer in new_layers:
        if layer != "defaultLayer" and cmds.objExists(layer):
            try:
                cmds.delete(layer)
            except:
                pass

    # Сортировка и материалы
    rebuild_lod_layers_and_materials()
    print "Import Done"

# _____________

# _____________ Copy Skinning _____________

def copy_skin_to_game_lods(*args):
    all_transforms = cmds.ls(transforms=True) or []
    count = 0

    for obj in all_transforms:
        short_name = obj.split("|")[-1]

        for i in range(1, 6):
            game_suffix = "_game_LOD%d" % i
            if short_name.endswith(game_suffix):
                base_name = short_name.replace(game_suffix, "")
                if not cmds.objExists(base_name):
                    continue

                # skinCluster 
                hist = cmds.listHistory(base_name, pruneDagObjects=True) or []
                skins = cmds.ls(hist, type="skinCluster")
                if not skins:
                    continue
                source_skin = skins[0]

                #Method и Components
                useComp = cmds.getAttr(source_skin + '.useComponents')
                skin_method = cmds.getAttr(source_skin + '.skinningMethod')

                dest_hist = cmds.listHistory(obj, pruneDagObjects=True) or []
                dest_skins = cmds.ls(dest_hist, type="skinCluster")
                if dest_skins:
                    cmds.skinCluster(dest_skins[0], e=True, unbind=True)

                influences = cmds.skinCluster(source_skin, q=True, influence=True)
                joints = cmds.ls(influences, type='joint')
                nurbs = list(set(influences) - set(joints))

                tempJoint = None
                if not joints:
                    cmds.select(clear=True)
                    tempJoint = cmds.joint()
                    joints = [tempJoint]
                
                if not isinstance(joints, list):
                    joints = [joints]

                dest_skin = cmds.skinCluster(obj, joints, 
                                             toSelectedBones=True, 
                                             useGeometry=True,
                                             dropoffRate=4,
                                             polySmoothness=False, 
                                             nurbsSamples=25, 
                                             rui=False, 
                                             mi=5, 
                                             omi=False,
                                             normalizeWeights=True)[0]

                if nurbs:
                    cmds.skinCluster(dest_skin, e=True,
                                     useGeometry=True,
                                     dropoffRate=4, 
                                     polySmoothness=False,
                                     nurbsSamples=25,
                                     lockWeights=False, 
                                     weight=0,
                                     addInfluence=nurbs)
                
                cmds.setAttr((dest_skin + '.useComponents'), useComp)
                cmds.setAttr((dest_skin + '.skinningMethod'), skin_method)

                # Copy
                cmds.copySkinWeights(sourceSkin=source_skin,
                                     destinationSkin=dest_skin,
                                     noMirror=True,
                                     surfaceAssociation='closestPoint',
                                     influenceAssociation='oneToOne',
                                     normalize=True)

                if tempJoint:
                    cmds.delete(tempJoint)
                
                if cmds.attributeQuery('deformUserNormals', node=dest_skin, exists=True):
                     if cmds.getAttr('%s.deformUserNormals' % dest_skin):
                        cmds.setAttr('%s.deformUserNormals' % dest_skin, 0)

                count += 1
                print("Skin copied: %s -> %s (Method: %s)" % (base_name, obj, skin_method))
    
    if count == 0:
        print "No matching *_game_LOD meshes found."
    else:
        print "Skin Copy Finished. Processed %d meshes."