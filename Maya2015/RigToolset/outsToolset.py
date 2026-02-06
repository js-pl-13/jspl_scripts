import maya.cmds as cmds
import shutil
import re
import os
import maya.mel as mel
import maya.OpenMaya as om

axis = ['X','Y','Z']
max = 4

class _outsToolset:	
    def __init__(self):
        print('outsToolset initialized.')


    def list_geometry(self):
        shapes = cmds.ls(sl=True, s=1, dag=1)
        for shape in shapes:
            if not shape.find('ShapeOrig')!= -1:
                shading_nodes_list = cmds.listConnections(shape, type='shadingEngine')
                return shading_nodes_list


    def copy_textures(arg):
        TZ_folder = cmds.file(sn=True, expandName=True, q=True)
        file_path = TZ_folder.rsplit('/', 1)[0]+'/'
        if os.path.exists(r'D:\Projects\Husky\branches\WWZ\WWZ_Main\WWZ_Alpha\source\textures\characters'):
            wwz_texture_path = r'D:\Projects\Husky\branches\WWZ\WWZ_Main\WWZ_Alpha\source\textures\characters'
            print 'WWZ textures at ' + wwz_texture_path
        elif os.path.exists(r'C:\Projects\Husky\branches\WWZ\WWZ_Main\WWZ_Alpha\source\textures\characters'):
            wwz_texture_path = r'C:\Projects\Husky\branches\WWZ\WWZ_Main\WWZ_Alpha\source\textures\characters'
            print 'WWZ textures at ' + wwz_texture_path
        saber_shader_nodes_list = cmds.ls('saberShaderDxNode*')

        if not (TZ_folder.split('/')[-1] == 'untitled'):
            ## saber scene ##
            if not len(saber_shader_nodes_list) == 0:
                if not os.path.exists(wwz_texture_path):
                    print '!! no wwz texture path found ' + wwz_texture_path
                else:
                    for node in saber_shader_nodes_list:
                        # check if attribute exists
                        if cmds.objExists(node+'.s3dShaderPs'):
                            s3dShader_string = cmds.getAttr(node+'.s3dShaderPs')
                            withquots_list = re.findall(r'"(.*)"', s3dShader_string)
                            for quots in withquots_list:
                                textures_files_folder = os.listdir(wwz_texture_path)
                                if (quots.find('ch_') != -1):
                                    for files in textures_files_folder:
                                        if files.find(str(quots))!= -1:
                                            if not os.path.isfile(file_path+'/'+files):
                                                shutil.copy2(wwz_texture_path+'\\'+files, file_path)
                                            else:
                                                print 'file already copied!'
                        else:
                            print node+'.s3dShaderPs' + 'has no such attribute!'

            ## simple scene ##
            else:
                shading_engine_list = self.list_geometry()

                for shading_node in shading_engine_list:
                    material_list = cmds.listConnections(shading_node + '.surfaceShader')
                    if isinstance(material_list, list):
                        material_node = material_list[0]
                    else:
                        material_node = material_list

                    ## color file
                    color_texture_node = cmds.listConnections(material_node+'.TEX_color_map')
                    color_file_path = cmds.getAttr(color_texture_node[0]+'.fileTextureName')
                    if os.path.isfile(color_file_path):
                        if not os.path.isfile(file_path+'/'+color_file_path.split('/')[-1]):
                            shutil.copy2(color_file_path, file_path)
                        else:
                            print 'such file exist! ' + color_file_path
                    else:
                        print 'material has no color! ' + color_file_path
                    ## normal file
                    normal_texture_node = cmds.listConnections(material_node+'.TEX_normal_map')
                    normal_file_path = cmds.getAttr(normal_texture_node[0]+'.fileTextureName')
                    if os.path.isfile(normal_file_path):
                        if not os.path.isfile(file_path+'/'+normal_file_path.split('/')[-1]):
                            shutil.copy2(normal_file_path, file_path)
                        else:
                            print 'such file exist! ' + normal_file_path
                    else:
                        print 'material has no normal! ' + normal_file_path
        else:
            cmds.error( "save scene befor copying textures!" )
			

    def scene_check_maximum_influence(self):
		scene_res = []
		cmds.select(clear=True)
		skin_clusters = cmds.ls(type="skinCluster")
		for clstr in skin_clusters:
			for mesh in cmds.skinCluster(clstr, q=True, geometry=True):
				scene_res += self.scene_check_mesh(max, clstr, mesh)
		print("{0} vertices exceeds {1} maximal".format(len(scene_res), max))
		cmds.select(scene_res)
		return scene_res
		
		
    def scene_check_mesh(self, max, clstr, mesh):
		vertices = cmds.polyListComponentConversion(mesh, toVertex=True)
		vertices = cmds.filterExpand(vertices, selectionMask=31)  # polygon vertex
		scene_res = []
		for vert in vertices:
			joints = cmds.skinPercent(clstr, vert, query=True, ignoreBelow=0.000001, transform=None)
			if joints:
				if len(joints) > max:
					scene_res.append(vert)
			else:
				print "mesh has skinCluster with no joints in it ---> " + str(mesh)
				break
		return scene_res
	
	
    def check_maximum_influence(arg):
		skin_clusters = []
		shape = []
		res = [] 
		selected = cmds.ls(sl=True, ap=True) 
		if selected:
			obj = selected[0].rsplit('.', 1)[0]    
		shape = cmds.ls(obj, dag=True, type="shape")
		if shape:
			cmds.select(shape[0])
			skin_clusters = cmds.listConnections(t="skinCluster")
			for clstr in skin_clusters:
				for mesh in cmds.skinCluster(clstr, q=True, geometry=True):
					res += check_mesh(max, clstr, mesh)
			print("{0} vertices exceeds {1} maximal".format(len(res), max))
			cmds.select(res)
		return res, skin_clusters
		
		
    def check_mesh(max, clstr, mesh):
		vertices = cmds.polyListComponentConversion(mesh, toVertex=True)
		vertices = cmds.filterExpand(vertices, selectionMask=31)  # polygon vertex
		res = []
		for vert in vertices:
			joints = cmds.skinPercent(clstr, vert, query=True, ignoreBelow=0.000001, transform=None)
			if len(joints) > max:
				res.append(vert)
		return res


    def percentage(part, whole):
		return 100 * float(part)/float(whole)


    def cleanup(arg):    
		# input vertex list with bad weights
		incorr_vrtx_weights_list = []
		incorr_vrtx_weights_list, skin_cluster = check_maximum_influence()
			
		#skin_cluster = cmds.ls(type="skinCluster")
		if skin_cluster:
			skin_cluster = skin_cluster[0]        
			count = 0        
			for bad in incorr_vrtx_weights_list:
				count += 1
				om.MGlobal.displayInfo(str('%.1f' % percentage(count, len(incorr_vrtx_weights_list)) + '%'))
				# per vertex
				infl_list = cmds.skinPercent(skin_cluster, bad, ignoreBelow=0.000001, query=True, transform=None)
				val_list = cmds.skinPercent(skin_cluster, bad, ignoreBelow=0.000001, query=True, value=True )
				smallest_value = min(val_list)
				smallest_index = val_list.index(min(val_list))
				middle_val = smallest_value / (len(infl_list)-1)
				#
				infl_list_iterator = [i for i, s in enumerate(infl_list)]
				i = 0
				cmds.skinPercent(skin_cluster, bad, transformValue=(infl_list[infl_list_iterator[smallest_index]], 0))
				
				for infl in infl_list:    
					infl_list_iterator[i]
					infl_current_val = val_list[infl_list_iterator[i]]
					if infl != infl_list[smallest_index]:
						cmds.skinPercent(skin_cluster, bad, transformValue=(infl_list[infl_list_iterator[i]], infl_current_val + middle_val))
					i = i + 1
		else:
			print 'error'
			
			
    def set_max_influence(arg):
		incorr_vrtx_weights_list, skin_cluster = check_maximum_influence()
		mesh = cmds.skinCluster(skin_cluster[0], q=True, geometry=True)
		cmds.setAttr(skin_cluster[0]+".maintainMaxInfluences", 1)
		cmds.setAttr(skin_cluster[0]+".maxInfluences", 4)
		print "'maintain max influences' set to " + str(cmds.getAttr(skin_cluster[0]+".maintainMaxInfluences")) + ' on ' + str(mesh[0])
		print "'max influences' set to " + str(cmds.getAttr(skin_cluster[0]+".maxInfluences")) + ' on ' + str(mesh[0])

