import xml.etree.ElementTree as ET
from xml.dom.minidom import Document
import maya.cmds as cmds
import shutil
import re
import os

axis = ['X','Y','Z']

nameSpaces = ['base_skeleton:','base_anarki_skeleton:','base_reptile_skeleton:','base_slash_skeleton:',
              'base_beastmaster_skeleton:','base_BJ_Blazkovicz_skeleton:','base_engineer_skeleton:',
              'base_hell_knight_skeleton:','base_doom_marine_skeleton:','base_woman_skeleton:',
              'base_keel_skeleton:','base_paladin_skeleton:','base_strogg_skeleton:','base_xaero_skeleton:', 'base_raine_skeleton:']

class _skelToolset:
    def __init__(self):
        print('skelToolset initialized.')

    def querySkel(arg):
        skeleton = cmds.ls(sl=True)
        skeleton_name = skeleton[0].split(':')[0]
        cmds.textField('lineEdit_namespace', edit=True, tx=skeleton_name+':')

    def re_skeleton(arg):
        textField_namespace = cmds.textField('lineEdit_namespace', query = True, text = True)
        if textField_namespace:
            current_namespace = textField_namespace.split(':')[0]
            if cmds.namespace(exists='new_'+current_namespace):
                cmds.namespace(removeNamespace='new_'+current_namespace, mergeNamespaceWithRoot=True)
            cmds.namespace(add='new_' + current_namespace)
            cmds.SelectHierarchy()
            selection = cmds.ls(sl=True, type='joint')
            for each in selection:
                cmds.select(each)
                cmds.joint(n='new_'+each)
                cmds.parent(w=True)
            cmds.spaceLocator(n='ROOT')
            cmds.rename( 'ROOT', 'new_' + current_namespace+ ':ROOT' )
            for each in selection:
                cmds.select(each)
                prnt = cmds.listRelatives(p=True)
                strng = ''.join(prnt)
                cmds.parent('new_'+each, 'new_'+strng)
            for each in selection:
                kbl = cmds.getAttr(each+'.visibility', k=True)
                cmds.setAttr('new_'+each+'.visibility', k=kbl)
                vis = cmds.getAttr(each+'.visibility')
                cmds.setAttr('new_'+each+'.visibility', vis)
                for i in axis:
                    kbl = cmds.getAttr(each+'.translate'+i, k=True)
                    cmds.setAttr('new_'+each+'.translate'+i, k=kbl)
                    lock = cmds.getAttr(each+'.translate'+i, l=True)
                    cmds.setAttr('new_'+each+'.translate'+i, l=lock)
                for i in axis:
                    kbl = cmds.getAttr(each+'.rotate'+i, k=True)
                    cmds.setAttr('new_'+each+'.rotate'+i, k=kbl)
                    lock = cmds.getAttr(each+'.rotate'+i, l=True)
                    cmds.setAttr('new_'+each+'.rotate'+i, l=lock)
                for i in axis:
                    kbl = cmds.getAttr(each+'.scale'+i, k=True)
                    cmds.setAttr('new_'+each+'.scale'+i, k=kbl)
                    lock = cmds.getAttr(each+'.scale'+i, l=True)
                    cmds.setAttr('new_'+each+'.scale'+i, l=lock)
        else:
            cmds.inViewMessage(amg='Skeleton not selected!', pos='midCenter', fade=True)

    def copyPose(arg):
        confirm = cmds.confirmDialog( title='Confirm', message='Save to xml this pose?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )

        if confirm == 'Yes':
            textField_namespace = cmds.textField('lineEdit_namespace', query = True, text = True)
            doc = Document()
            root_node = doc.createElement("root")
            doc.appendChild(root_node)
            cmds.select('%sCENTRE' % textField_namespace, hi = True)
            selection = cmds.ls(sl=True, type='joint')

            for object in selection:
                if ":" in object:
                    nice_name = object.split(':')[-1]
                    object_node = doc.createElement(str(nice_name))
                    root_node.appendChild(object_node)
                else:
                    object_node = doc.createElement(str(object))
                    root_node.appendChild(object_node)

                object_rotate = cmds.getAttr(object + ".rotate")
                object_node.setAttribute("rotateX", str(object_rotate[0][0]))
                object_node.setAttribute("rotateY", str(object_rotate[0][1]))
                object_node.setAttribute("rotateZ", str(object_rotate[0][2]))

            if not os.path.exists("C:\ProgramData\MayaPoser"):
                os.makedirs("C:\ProgramData\MayaPoser")

                if selection[0].index(":"):
                    file_name = selection[0].rsplit(':', 1)[0]
                    xml_file = open("C:\ProgramData\MayaPoser\\"+file_name+".xml", "w")
                    xml_file.write(doc.toprettyxml())
                    xml_file.close()
                else:
                    xml_file = open("C:\ProgramData\MayaPoser\\"+selection[0]+".xml", "w")
                    xml_file.write(doc.toprettyxml())
                    xml_file.close()
            else:
                if selection[0].index(":"):
                    file_name = selection[0].rsplit(':', 1)[0]
                    xml_file = open("C:\ProgramData\MayaPoser\\"+file_name+".xml", "w")
                    xml_file.write(doc.toprettyxml())
                    xml_file.close()
                else:
                    xml_file = open("C:\ProgramData\MayaPoser\\"+selection[0]+".xml", "w")
                    xml_file.write(doc.toprettyxml())
                    xml_file.close()
        else:
            print "pose not copied!"

    def pastePose(arg):
        textField_namespace = cmds.textField('lineEdit_namespace', query = True, text = True)

        if textField_namespace.index(":"):
            pthStr = textField_namespace[:-1]
            p = r'C:\ProgramData\MayaPoser\%s.xml' % pthStr

        tree = ET.parse(p)
        root = tree.getroot()
        root.get
        x = root.getchildren()

        for i in x:
            a = str(i).split("'")[1]
            elem = root.find(a)
            attr = elem.attrib
            for ax in axis:
                if not(cmds.getAttr("%s%s.rotate" % (textField_namespace, a) + ax, l=True)):
                    rot = float(attr['rotate' + ax])
                    cmds.setAttr("%s%s.rotate" % (textField_namespace, a) + ax, rot)

    def jntHid(*args):
        textField_namespace = cmds.textField('lineEdit_namespace', query = True, text = True)
        cmds.hide( cmds.ls( type='joint' ) )

    def jntShw(*args):
        textField_namespace = cmds.textField('lineEdit_namespace', query = True, text = True)
        cmds.showHidden( cmds.ls( type='joint' ) )

    def jntSet(*args):
        textField_namespace = cmds.textField('lineEdit_namespace', query = True, text = True)
        ## ARMupL
        cmds.createNode('multDoubleLinear', n='%sARMupL' % textField_namespace + '_mdl')
        cmds.connectAttr('%sARM1L' % textField_namespace + '.rotateX', '%sARMupL' % textField_namespace + '_mdl' + '.input1', force=True)
        cmds.setAttr('%sARMupL' % textField_namespace + '_mdl' + '.input2', -1)
        cmds.connectAttr('%sARMupL' % textField_namespace + '_mdl' + '.output', '%sARMupL' % textField_namespace+ '.rotateX', force=True)
        ## ARMupR
        cmds.createNode('multDoubleLinear', n='%sARMupR' % textField_namespace + '_mdl')
        cmds.connectAttr('%sARM1R' % textField_namespace + '.rotateX', '%sARMupR' % textField_namespace + '_mdl' + '.input1', force=True)
        cmds.setAttr('%sARMupR' % textField_namespace + '_mdl' + '.input2', -1)
        cmds.connectAttr('%sARMupR' % textField_namespace + '_mdl' + '.output', '%sARMupR' % textField_namespace+ '.rotateX', force=True)
        ## forearm_L
        cmds.createNode('multDoubleLinear', n='%sforearm_L' % textField_namespace + '_mdl')
        cmds.connectAttr('%sHANDL' % textField_namespace + '.rotateX', '%sforearm_L' % textField_namespace + '_mdl' + '.input1', force=True)
        cmds.setAttr('%sforearm_L' % textField_namespace + '_mdl' + '.input2', 1)
        cmds.connectAttr('%sforearm_L' % textField_namespace + '_mdl' + '.output', '%sforearm_L' % textField_namespace+ '.rotateX', force=True)
        ## forearm_R
        cmds.createNode('multDoubleLinear', n='%sforearm_R' % textField_namespace + '_mdl')
        cmds.connectAttr('%sHANDR' % textField_namespace + '.rotateX', '%sforearm_R' % textField_namespace + '_mdl' + '.input1', force=True)
        cmds.setAttr('%sforearm_R' % textField_namespace + '_mdl' + '.input2', 1)
        cmds.connectAttr('%sforearm_R' % textField_namespace + '_mdl' + '.output', '%sforearm_R' % textField_namespace+ '.rotateX', force=True)
        ## HIP_L
        cmds.createNode('multDoubleLinear', n='%sHIP_L' % textField_namespace + '_mdl')
        cmds.connectAttr('%sLEG1L' % textField_namespace + '.rotateX', '%sHIP_L' % textField_namespace + '_mdl' + '.input1', force=True)
        cmds.setAttr('%sHIP_L' % textField_namespace + '_mdl' + '.input2', -1)
        cmds.connectAttr('%sHIP_L' % textField_namespace + '_mdl' + '.output', '%sHIP_L' % textField_namespace+ '.rotateX', force=True)
        ## HIP_R
        cmds.createNode('multDoubleLinear', n='%sHIP_R' % textField_namespace + '_mdl')
        cmds.connectAttr('%sLEG1R' % textField_namespace + '.rotateX', '%sHIP_R' % textField_namespace + '_mdl' + '.input1', force=True)
        cmds.setAttr('%sHIP_R' % textField_namespace + '_mdl' + '.input2', -1)
        cmds.connectAttr('%sHIP_R' % textField_namespace + '_mdl' + '.output', '%sHIP_R' % textField_namespace+ '.rotateX', force=True)

    def jntBrk(*args):
        textField_namespace = cmds.textField('lineEdit_namespace', query = True, text = True)
        cmds.delete('%sARMupL' % textField_namespace + '_mdl')
        cmds.delete('%sARMupR' % textField_namespace + '_mdl')
        cmds.delete('%sforearm_L' % textField_namespace + '_mdl')
        cmds.delete('%sforearm_R' % textField_namespace + '_mdl')
        cmds.delete('%sHIP_L' % textField_namespace + '_mdl')
        cmds.delete('%sHIP_R' % textField_namespace + '_mdl')

    def jntZero(*args):
        textField_namespace = cmds.textField('lineEdit_namespace', query = True, text = True)
        cmds.select('%sCENTRE' % textField_namespace, hi = True)

        selection = cmds.ls(sl=True, type='joint')
        for object in selection:
            if ":" in object:
                for ax in axis:
                    if not(cmds.getAttr(object + ".rotate" + ax, l=True)):
                        cmds.setAttr(object + ".rotate" + ax, 0)