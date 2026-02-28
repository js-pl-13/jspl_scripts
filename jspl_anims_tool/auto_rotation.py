# -*- coding: utf-8 -*-
# auto_rotation.py
import maya.cmds as cmds
from . import utils

def setup_auto_rotation(*args):
    ns = utils.get_namespace_from_root()
    print("Setting up auto rotation for namespace: '{}'".format(ns))
    
    connection_groups = [
        [('ARM1L', 'ARMupL', -1), ('l_shoulder', 'l_shoulder_twist_01', -1)],
        [('ARM1R', 'ARMupR', -1), ('r_shoulder', 'r_shoulder_twist_01', -1)],
        [('HANDL', 'forearm_L', 1), ('l_forearm', 'l_forearm_twist_01', 1)],
        [('HANDR', 'forearm_R', 1), ('r_forearm', 'r_forearm_twist_01', 1)],
        [('LEG1L', 'HIP_L', -1), ('l_hip', 'l_hip_twist_01', -1)],
        [('LEG1R', 'HIP_R', -1), ('r_hip', 'r_hip_twist_01', -1)]
    ]

    for group in connection_groups:
        connected = False
        for src, tgt, mult in group:
            full_src = '{}{}'.format(ns, src)
            full_tgt = '{}{}'.format(ns, tgt)
            node_name = '{}{}_mdl'.format(ns, tgt)

            if cmds.objExists(full_src) and cmds.objExists(full_tgt):
                if cmds.listConnections('{}.rotateX'.format(full_tgt), d=False, s=True):
                    inputs = cmds.listConnections('{}.rotateX'.format(full_tgt), d=False, s=True)
                    if inputs and cmds.nodeType(inputs[0]) == 'multDoubleLinear':
                        cmds.delete(inputs[0])

                try:
                    if not cmds.objExists(node_name):
                        cmds.createNode('multDoubleLinear', n=node_name)
                    cmds.connectAttr('{}.rotateX'.format(full_src), '{}.input1'.format(node_name), force=True)
                    cmds.setAttr('{}.input2'.format(node_name), mult)
                    cmds.connectAttr('{}.output'.format(node_name), '{}.rotateX'.format(full_tgt), force=True)
                    print("Connected: {} -> {}".format(full_src, full_tgt))
                    connected = True
                    break 
                except Exception as e:
                    print("Error: {}".format(str(e)))
            
        if not connected:
            print("Warning: Skipping group for '{}'".format(group[0][1]))

def break_auto_rotation(*args):
    ns = utils.get_namespace_from_root()
    print("Breaking auto rotation for namespace: '{}'".format(ns))

    targets = [
        'ARMupL', 'ARMupR', 'forearm_L', 'forearm_R', 'HIP_L', 'HIP_R',
        'l_shoulder_twist_01', 'r_shoulder_twist_01', 'l_forearm_twist_01', 'r_forearm_twist_01', 'l_hip_twist_01', 'r_hip_twist_01'
    ]
    
    for tgt in targets:
        full_tgt = '{}{}'.format(ns, tgt)
        if not cmds.objExists(full_tgt): continue
        attr = '{}.rotateX'.format(full_tgt)
        connections = cmds.listConnections(attr, source=True, destination=False, plugs=True)
        if connections:
            source_node = connections[0].split('.')[0]
            if cmds.nodeType(source_node) == 'multDoubleLinear':
                cmds.delete(source_node)
                print("Deleted MDL node for '{}'".format(tgt))
            else:
                cmds.disconnectAttr(connections[0], attr)
                print("Disconnected '{}'".format(tgt))