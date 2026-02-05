# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel

#__________________________________________________________________________________________
# Main Settings
WINDOW_NAME = "FaceRigPipelineWindow"
#__________________________________________________________________________________________

class LocatorsTool(object):
    def __init__(self):
        self.prepare_environment()
        self.show_ui()

    def prepare_environment(self):
        # Загружаем встроенный плагин для работы closestPointOnMesh
        if not cmds.pluginInfo("closestPointOnMesh", q=True, loaded=True):
            try:
                cmds.loadPlugin("closestPointOnMesh")
            except:
                print "Warning: closestPointOnMesh could not be loaded."

#___________________________________________________________________________________________
# UI BUILDER
    def show_ui(self):

        if cmds.window(WINDOW_NAME, exists=True):
            cmds.deleteUI(WINDOW_NAME)

        self.window = cmds.window(WINDOW_NAME, title="Face Rig Pipeline 2019", widthHeight=(320, 520), sizeable=True)

        main_layout = cmds.columnLayout(adj=True, rowSpacing=5)

        # ==========================================================================================
        # BLOCK 1: Work with Blendshapes & Locators
        # ==========================================================================================
        cmds.frameLayout(label="1. Blendshapes & Locators Setup", collapsable=False, borderStyle="etchedIn", marginWidth=5, marginHeight=5, parent=main_layout)
        self.block1_layout = cmds.columnLayout(adj=True, rowSpacing=5)
        
        # --- A. Target Mesh (Main Head) ---
        cmds.text(label="Target Mesh (Base Head):", align="left", font="boldLabelFont")
        # Поле с подсказкой вместо "danai"
        self.mesh_field = cmds.textField(placeholderText="Add Base Mesh...")
        
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=30, c=self.add_mesh_to_field)
        cmds.button(label="Clear", height=30, c=self.clear_mesh_field)
        cmds.setParent("..")

        cmds.separator(h=5, style="none")

        # --- B. Warp Mesh ---
        cmds.text(label="Warp Mesh (Driver):", align="left", font="boldLabelFont")
        # Поле с подсказкой
        self.warp_field = cmds.textField(placeholderText="Add Warp Mesh...")
        
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=30, c=self.add_warp_to_field)
        cmds.button(label="Clear", height=30, c=self.clear_warp_field)
        cmds.setParent("..")

        # --- C. Create Blendshape ---
        cmds.separator(h=5, style="none")
        cmds.button(
            label="Create Warp BlendShape", 
            height=30, 
            command=self.run_create_warp_bs
        )
        
        cmds.separator(h=15, style="in")

        # --- D. Run Fix Locators ---
        cmds.button(
            label="RUN FIX LOCATORS", 
            height=30, 
            command=self.run_fix
        )

        # --- E. Toggle BlendShapes (0/1 с твоей логикой) ---
        self.toggle_btn = cmds.button(
            label="Toggle BlendShapes: ---", 
            height=30, 
            c=self.run_blendshape_toggle,
            backgroundColor=[0.35, 0.35, 0.35]
        )
        
        # Обновляем статус кнопки сразу
        self.update_toggle_button_ui()

        cmds.separator(h=10, style="none")

        # --- F. Delete Utilities (Вертикально) ---
        cmds.button(
            label="Del. Constraints", 
            height=30, 
            c=self.delete_constraints
        )
        cmds.button(
            label="Del. Fixed Locs", 
            height=30, 
            c=self.delete_fixed_locators
        )
        
        cmds.setParent("..") # Column
        cmds.setParent("..") # Frame

        cmds.showWindow(self.window)

#___________________________________________________________________________________________
# FUNCTIONS

    def add_mesh_to_field(self, *args):
        sel = cmds.ls(sl=True)
        if sel: 
            cmds.textField(self.mesh_field, edit=True, text=sel[0])
            self.update_toggle_button_ui()

    def clear_mesh_field(self, *args):
        cmds.textField(self.mesh_field, edit=True, text="")
        self.update_toggle_button_ui()

    def add_warp_to_field(self, *args):
        sel = cmds.ls(sl=True)
        if sel: cmds.textField(self.warp_field, edit=True, text=sel[0])

    def clear_warp_field(self, *args):
        cmds.textField(self.warp_field, edit=True, text="")

    def run_create_warp_bs(self, *args):
        target = cmds.textField(self.mesh_field, q=True, text=True)
        warp = cmds.textField(self.warp_field, q=True, text=True)
        if cmds.objExists(target) and cmds.objExists(warp):
            bs = cmds.blendShape(warp, target, n=target+"_WarpBS")[0]
            cmds.setAttr(bs + "." + warp, 1.0)
            self.update_toggle_button_ui()

    def run_fix(self, *args):
        mesh = cmds.textField(self.mesh_field, q=True, text=True)
        if not mesh or not cmds.objExists(mesh):
            cmds.error("Mesh not found! Please add Base Mesh.")
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
                if shapes: mesh_attr = shapes[0] + ".worldMesh[0]"

            cmds.connectAttr(mesh_attr, cpmNode + ".inMesh")
            locPos = cmds.xform(fix_loc, q=1, t=1, ws=1)
            cmds.setAttr(cpmNode + ".inPosition", locPos[0], locPos[1], locPos[2], type="double3")
            faceIndx = cmds.getAttr(cpmNode + ".closestFaceIndex")
            faceFound = "{0}.f[{1}]".format(mesh, faceIndx)
            cmds.select(faceFound, fix_loc)
            cmds.pointOnPolyConstraint(mo=True, weight=1)
            cmds.delete(cpmNode)
        
        print(">> Fix Locators Done.")

    def update_toggle_button_ui(self):
        """ Обновляет кнопку согласно твоей логике (0/1 и цвета) """
        mesh = cmds.textField(self.mesh_field, q=True, text=True)
        
        if not mesh or not cmds.objExists(mesh):
            cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShapes: ---", backgroundColor=[0.3, 0.3, 0.3])
            return

        history = cmds.listHistory(mesh)
        bs_nodes = cmds.ls(history, type='blendShape')
        
        if not bs_nodes:
            cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShapes: NONE", backgroundColor=[0.35, 0.3, 0.3])
            return

        weight_list = cmds.listAttr(bs_nodes[0] + ".w", multi=True)
        if weight_list:
            val = cmds.getAttr(bs_nodes[0] + "." + weight_list[0])
            # Логика из твоего запроса
            if val > 0.5:
                cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShapes: 1", backgroundColor=[0.3, 0.6, 0.3])
            else:
                cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShapes: 0", backgroundColor=[0.6, 0.3, 0.3])

    def run_blendshape_toggle(self, *args):
        mesh = cmds.textField(self.mesh_field, q=True, text=True)
        if not cmds.objExists(mesh): return

        history = cmds.listHistory(mesh)
        bs_nodes = cmds.ls(history, type='blendShape')
        if not bs_nodes: return

        for bs in bs_nodes:
            weight_list = cmds.listAttr(bs + ".w", multi=True)
            if not weight_list: continue
            
            current_val = cmds.getAttr(bs + "." + weight_list[0])
            new_val = 1.0 if current_val <= 0.5 else 0.0
            
            for w in weight_list:
                cmds.setAttr(bs + "." + w, new_val)
        
        self.update_toggle_button_ui()

    def delete_fixed_locators(self, *args):
        targets = cmds.ls("*_fixed", type="transform")
        if targets:
            cmds.delete(targets)
            print(">> Deleted %d _fixed objects." % len(targets))

    def delete_constraints(self, *args):
        fixed_locs = cmds.ls("*_pos", type="transform")
        if not fixed_locs: return
        cmds.select(fixed_locs)
        mel.eval("select -hi")
        constraints = cmds.ls(sl=True, type="constraint")
        if constraints:
            cmds.delete(constraints)
            print(">> Deleted %d constraints." % len(constraints))

    def run_final_skin(self, *args): print("Block 2: Placeholder")
    def run_clean_skin(self, *args): print("Block 3: Placeholder")

LocatorsTool()