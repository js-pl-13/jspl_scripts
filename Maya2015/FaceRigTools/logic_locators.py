# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.OpenMaya as om
import json
import os
import config 

def export_loc_data():
    if not os.path.exists(config.EXPORT_PATH):
        try:
            os.makedirs(config.EXPORT_PATH)
        except OSError as e:
            cmds.error("Could not create path: " + str(e))
            return

    locators = cmds.ls("*locRot_pos", type="transform")
    if not locators:
        cmds.warning("No '*locRot_pos' objects found to export")
        return

    data = {}
    for loc in locators:
        trans = cmds.getAttr(loc + ".translate")[0] 
        rot = cmds.getAttr(loc + ".rotate")[0]      
        data[loc] = {"t": trans, "r": rot}

    full_path = os.path.join(config.EXPORT_PATH, config.EXPORT_FILE)
    try:
        with open(full_path, 'w') as f:
            json.dump(data, f, indent=4)
        om.MGlobal.displayInfo("Export: Data saved to " + full_path)
    except IOError as e:
        cmds.error("Failed to save file: " + str(e))

def import_loc_data():
    full_path = os.path.join(config.EXPORT_PATH, config.EXPORT_FILE)
    if not os.path.exists(full_path):
        cmds.warning("File not found: " + full_path)
        return

    try:
        with open(full_path, 'r') as f:
            data = json.load(f)
    except ValueError:
        cmds.error("Invalid json")
        return

    count = 0
    for loc_name, attributes in data.items():
        if cmds.objExists(loc_name):
            try:
                cmds.setAttr(loc_name + ".translate", attributes["t"][0], attributes["t"][1], attributes["t"][2])
                cmds.setAttr(loc_name + ".rotate", attributes["r"][0], attributes["r"][1], attributes["r"][2])
                count += 1
            except:
                print "Warning: Could not set attrs on " + loc_name
        else:
            print "Skipped: " + loc_name + " (not found in scene)"
    om.MGlobal.displayInfo("Import new locators: Updated %d locators" % count)

def run_fix(mesh):
    if not mesh or not cmds.objExists(mesh):
        cmds.error("Mesh not found! Add Base Mesh")
        return

    cmds.select('*_pos')
    bad_loc_list = cmds.ls(sl=True)
    trans_loc_list = []

    for bad_loc in bad_loc_list:
        fixed_loc = cmds.spaceLocator(n=bad_loc + '_fixed')[0]
        prntCnstrn_align = cmds.parentConstraint(bad_loc, fixed_loc, mo=False)
        cmds.delete(prntCnstrn_align)
        cmds.parentConstraint(fixed_loc, bad_loc, mo=True)
        trans_loc_list.append(fixed_loc)

    for fix_loc in trans_loc_list:    
        cpmNode = cmds.createNode("closestPointOnMesh")
        mesh_attr = mesh + ".outMesh"
        if not cmds.objExists(mesh_attr):
            shapes = cmds.listRelatives(mesh, s=True)
            if shapes:
                mesh_attr = shapes[0] + ".worldMesh[0]"

        cmds.connectAttr(mesh_attr, cpmNode + ".inMesh")
        locPos = cmds.xform(fix_loc, q=1, t=1, ws=1)
        cmds.setAttr(cpmNode + ".inPosition", locPos[0], locPos[1], locPos[2], type="double3")
        faceIndx = cmds.getAttr(cpmNode + ".closestFaceIndex")
        faceFound = "{0}.f[{1}]".format(mesh, faceIndx)

        cmds.select(faceFound, fix_loc)
        cmds.pointOnPolyConstraint(mo=True, weight=1)
        cmds.delete(cpmNode)
    
    print "Fix Locators Done"

def create_warp_bs(target, warp_mesh):
    if cmds.objExists(target) and cmds.objExists(warp_mesh):
        bs = cmds.blendShape(warp_mesh, target, n=target+"_WBS")[0]
        cmds.setAttr(bs + "." + warp_mesh, 1.0)
        return True
    return False

def check_bs_status(mesh):
    if not mesh or not cmds.objExists(mesh): return "none"
    h = cmds.listHistory(mesh)
    bs = cmds.ls(h, type='blendShape')
    if not bs: return "none"
    w = cmds.listAttr(bs[0] + ".w", multi=True)
    if w:
        val = cmds.getAttr(bs[0] + "." + w[0])
        return "on" if val > 0.5 else "off"
    return "none"

def toggle_blendshape(mesh):
    if not mesh or not cmds.objExists(mesh): return
    h = cmds.listHistory(mesh); bs = cmds.ls(h, type='blendShape')
    if not bs: return
    for b in bs:
        w = cmds.listAttr(b + ".w", multi=True)
        if not w: continue
        nv = 1.0 if cmds.getAttr(b + "." + w[0]) <= 0.5 else 0.0
        for i in w:
            cmds.setAttr(b + "." + i, nv)

def delete_fixed_locators():
    t = cmds.ls("*_fixed", type="transform")
    if t: cmds.delete(t)

def delete_constraints():
    f = cmds.ls("*_pos", type="transform")
    if f:
        children = cmds.listRelatives(f, type="constraint", fullPath=True)
        if children:
            cmds.delete(children)
            print "Constraints deleted"
        else:
            print "No constraints found"
        
        cmds.select(cl=True)