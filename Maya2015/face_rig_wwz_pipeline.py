# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import json
import os

#__________________________________________________________________________________________
# Main Settings
WINDOW_NAME = "FaceRigPipelineWindow"
LIST_WINDOW_NAME = "GeneratedBSListWindow"
DEFAULT_MAX_INF = 4
EXPORT_PATH = "D:/data_scripts/face_rig/"
EXPORT_FILE = "locators_data.json"
#__________________________________________________________________________________________

class face_rig_wwz_pipeline(object):
    def __init__(self):
        # Настройки Блока 2
        self.bs_dict = {
            'lBrow_UP': 1, 'lBrow_DW': -1, 'rBrow_UP': 1, 'rBrow_DW': -1,
            'lBrowEvel_UP': 1, 'lBrowEvel_DW': -1, 'rBrowEvel_UP': 1,
            'rBrowEvel_DW': -1, 'lSuspect': 1, 'rSuspect': 1, 'lEyelid_UP': 1,
            'lEyelid_DW': -1, 'rEyelid_UP': 1, 'rEyelid_DW': -1, 'nose': 1,
            'lSquint': 1, 'rSquint': 1, 'lDogUp': 1, 'rDogUp': 1, 'lDogDw': 1,
            'rDogDw': 1, 'LipLowerUp': 1, 'LipLowerDw': 1, 'LipLowerDw_UP': -1,
            'LipLowerUp_UP': -1, 'lLip_OU': 0.7, 'lLip_IN': -1, 'lLip_UP': 1,
            'lLip_DW': -1, 'rLip_OU': 0.7, 'rLip_IN': -1, 'rLip_UP': 1, 'rLip_DW': -1,
            'cLip_UP': 1, 'cLip_DW': -1, 'Chin': -1, 'NeckApple': 1, 'NeckMuscle': -1,
            'lKiss_OU': 1, 'rKiss_OU': 1
        }
        
        self.ordered_names = [
            "rBrowEvel_UP", "lBrowEvel_DW", "rSuspect", "lSuspect", "rBrow_UP", 
            "rLip_DW", "rBrowEvel_DW", "lEyelid_DW", "rLip_IN", "LipLowerDw_UP", 
            "rSquint", "LipLowerUp", "lEyelid_UP", "NeckApple", "LipLowerUp_UP", 
            "rEyelid_UP", "rDogUp", "lDogDw", "lLip_DW", "LipLowerDw", 
            "lLip_IN", "lBrow_UP", "cLip_DW", "cLip_UP", "rLip_OU", 
            "lBrowEvel_UP", "rDogDw", "lLip_UP", "Chin", "nose", 
            "lDogUp", "rLip_UP", "lBrow_DW", "lSquint", "rBrow_DW", 
            "rEyelid_DW", "NeckMuscle", "lLip_OU", "lKiss_OU", "rKiss_OU"
        ]
        
        self.controllers_list = [ 
            'cLip_CT', 'LipLowerUp_CT', 'LipLowerDw_CT', 'nose_CT', 
            'Chin_CT', 'NeckApple_CT', 'NeckMuscle_CT', 'lBrowEvel_CT', 
            'lBrow_CT', 'lSuspect_CT', 'lLip_CT', 'lDogUp_CT', 
            'lDogDw_CT', 'lEyelid_CT', 'lSquint_CT', 'rBrowEvel_CT', 
            'rBrow_CT', 'rSuspect_CT', 'rLip_CT', 'rDogDw_CT', 
            'rDogUp_CT', 'rEyelid_CT', 'rSquint_CT', 'lKiss_CT', 'rKiss_CT' 
        ]

        self.prepare_environment()
        self.show_ui()

    def prepare_environment(self):
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

        self.window = cmds.window(WINDOW_NAME, title="Face Rig Pipeline", widthHeight=(360, 850), sizeable=True)
        main_layout = cmds.columnLayout(adj=True, rowSpacing=5)

        # BLOCK 1
        cmds.frameLayout(label="1. Blendshapes & Locators Setup", borderStyle="etchedIn", marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
        self.mesh_field = cmds.textField(placeholderText="Add Base Mesh...")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=30, c=self.add_mesh_to_field)
        cmds.button(label="Clear", height=30, c=self.clear_mesh_field)
        cmds.setParent("..")
        self.warp_field = cmds.textField(placeholderText="Add Warp Mesh...")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=30, c=self.add_warp_to_field)
        cmds.button(label="Clear", height=30, c=self.clear_warp_field)
        cmds.setParent("..")
        cmds.button(label="Create Warp BlendShape", height=30, command=self.run_create_warp_bs)
        cmds.separator(h=10, style="in")
        cmds.button(label="RUN FIX LOCATORS", height=30, command=self.run_fix)
        self.toggle_btn = cmds.button(label="Toggle BlendShape: ---", height=30, c=self.run_blendshape_toggle, backgroundColor=[0.35, 0.35, 0.35])
        self.update_toggle_button_ui()
        cmds.separator(h=10, style="none")
        cmds.button(label="Del. Constraints", height=30, c=self.delete_constraints)
        cmds.button(label="Del. Fixed Locs", height=30, c=self.delete_fixed_locators)
        
        # КНОПКИ EXPORT/IMPORT (без inViewMessage)
        cmds.separator(h=5, style="none")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[175, 175])
        cmds.button(label="Export Pos Data", height=30, command=self.export_loc_data, backgroundColor=[0.3, 0.4, 0.4])
        cmds.button(label="Import Pos Data", height=30, command=self.import_loc_data, backgroundColor=[0.4, 0.4, 0.3])
        cmds.setParent("..")
        
        cmds.setParent("..")
        cmds.setParent("..")

        # BLOCK 2
        cmds.frameLayout(label="2. Final Skin & Face BS Generator", borderStyle="etchedIn", marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
        self.skinned_mesh_field = cmds.textField(placeholderText="Add Skinned Head...")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=30, c=self.add_skinned_to_field)
        cmds.button(label="Clear", height=30, c=self.clear_skinned_field)
        cmds.setParent("..")
        cmds.button(label="GENERATE BLENDSHAPES", height=40, command=self.run_gen_blendshapes)
        cmds.button(label="Select Generated", height=30, command=self.select_bs_geo)
        cmds.button(label="Show All Generated BlendShape", height=30, command=self.show_generated_bs_list)
        cmds.setParent("..")
        cmds.setParent("..")

        # BLOCK 3
        cmds.frameLayout(label="3. Clean Skin (Max 4 Inf)", borderStyle="etchedIn", marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
        cmds.button(label="Reset All Controller", height=30, command=self.run_zero_controllers)
        cmds.button(label="Check Scene (Max 4)", height=30, command=lambda x: self.run_scene_check(DEFAULT_MAX_INF))
        cmds.separator(h=5, style="in")
        cmds.button(label="STEP 1: Check Selected Mesh", height=30, command=lambda x: self.run_check_mesh(DEFAULT_MAX_INF))
        cmds.button(label="STEP 2: FULL AUTO CLEANUP", height=40, command=self.run_cleanup_loop)
        cmds.button(label="STEP 3: Prune (0.001)", height=30, command=self.run_prune)
        cmds.button(label="STEP 4: Set Max Influence (4)", height=30, command=self.run_set_max_inf)
        cmds.setParent("..")
        cmds.setParent("..")

        cmds.showWindow(self.window)

#___________________________________________________________________________________________
# LOGIC BLOCK 1: EXPORT / IMPORT (CLEAN LOGS)

    def export_loc_data(self, *args):
        # 1. Проверяем/создаем директорию
        if not os.path.exists(EXPORT_PATH):
            try:
                os.makedirs(EXPORT_PATH)
            except OSError as e:
                cmds.error("Could not create directory: " + str(e))
                return

        # 2. Находим локаторы
        locators = cmds.ls("*locRot_pos", type="transform")
        if not locators:
            cmds.warning("No '*locRot_pos' objects found to export.")
            return

        data = {}
        for loc in locators:
            trans = cmds.getAttr(loc + ".translate")[0] 
            rot = cmds.getAttr(loc + ".rotate")[0]      
            data[loc] = {"t": trans, "r": rot}

        # 3. Сохраняем в JSON
        full_path = os.path.join(EXPORT_PATH, EXPORT_FILE)
        try:
            with open(full_path, 'w') as f:
                json.dump(data, f, indent=4)
            om.MGlobal.displayInfo(">> EXPORT SUCCESS: Data saved to " + full_path)
        except IOError as e:
            cmds.error("Failed to save file: " + str(e))

    def import_loc_data(self, *args):
        full_path = os.path.join(EXPORT_PATH, EXPORT_FILE)
        
        # 1. Проверяем файл
        if not os.path.exists(full_path):
            cmds.warning("File not found: " + full_path)
            return

        try:
            with open(full_path, 'r') as f:
                data = json.load(f)
        except ValueError:
            cmds.error("Invalid JSON format in file.")
            return

        # 2. Применяем данные
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

        om.MGlobal.displayInfo(">> IMPORT SUCCESS: Updated %d locators." % count)

#___________________________________________________________________________________________
# LOGIC BLOCK 1: FIX LOCATORS (ORIGINAL)

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
        
        print ">> Fix Locators Done."

#___________________________________________________________________________________________
# LOGIC BLOCK 3: CLEANUP

    def get_skin_cluster(self, node):
        if cmds.nodeType(node) == 'skinCluster':
            return node
        cl = mel.eval('findRelatedSkinCluster ' + node)
        if cl:
            return cl
        his = cmds.listHistory(node) or []
        cls = cmds.ls(his, type='skinCluster')
        if cls:
            return cls[0]
        return None

    def run_cleanup_loop(self, *args):
        sel = cmds.ls(sl=True)
        if not sel:
            cmds.warning("Please select a skinned mesh!")
            return
        cl = self.get_skin_cluster(sel[0])
        if not cl:
            return
            
        all_inf = cmds.skinCluster(cl, q=True, inf=True)
        locked = []
        for inf in all_inf:
            if cmds.getAttr(inf + ".liw"):
                locked.append(inf)
        
        if locked:
            confirm = cmds.confirmDialog(
                title='Locked Influences', 
                message='Found %d LOCKED influences. Unlock?' % len(locked), 
                button=['Unlock All', 'Abort'], 
                defaultButton='Unlock All', 
                cancelButton='Abort'
            )
            if confirm == 'Unlock All':
                for inf in locked:
                    cmds.setAttr(inf + ".liw", 0)
            else:
                return
        
        geo = cmds.skinCluster(cl, q=True, g=True)
        obj = geo[0]
        it = 1
        bad_count = 1
        
        cmds.progressWindow(title='Auto Cleanup Loop', progress=0, isInterruptable=True)
        
        try:
            while bad_count > 0:
                cmds.select(obj, r=True)
                bad_list = self.run_check_mesh(DEFAULT_MAX_INF)
                bad_count = len(bad_list)
                
                if bad_count == 0:
                    break
                
                status_msg = 'Iter %d: Fixing %d bad verts...' % (it, bad_count)
                cmds.progressWindow(edit=True, max=bad_count, status=status_msg, progress=0)
                
                for v in bad_list:
                    if cmds.progressWindow(query=True, isCancelled=True):
                        break
                    
                    inf_l = cmds.skinPercent(cl, v, ib=1e-6, q=True, t=None)
                    val_l = cmds.skinPercent(cl, v, ib=1e-6, q=True, v=True)
                    if len(inf_l) > DEFAULT_MAX_INF:
                        mv = min(val_l)
                        mi = val_l.index(mv)
                        dist = mv / (len(inf_l)-1)
                        cmds.skinPercent(cl, v, tv=(inf_l[mi], 0))
                        for idx, name in enumerate(inf_l):
                            if idx != mi:
                                cmds.skinPercent(cl, v, tv=(name, val_l[idx] + dist))
                    cmds.progressWindow(edit=True, step=1)
                
                it += 1
                if it > 40:
                    break
            cmds.progressWindow(endProgress=True)
            om.MGlobal.displayInfo(">> SUCCESS: Mesh is clean.")
        except Exception as e:
            cmds.progressWindow(endProgress=True)
            print "Error: " + str(e)
            
        cmds.select(obj, r=True)

#___________________________________________________________________________________________
# BS LIST (WITH SELECT COMMAND)

    def show_generated_bs_list(self, *args):
        if cmds.window(LIST_WINDOW_NAME, exists=True):
            cmds.deleteUI(LIST_WINDOW_NAME)
        ex = [n for n in self.ordered_names if cmds.objExists(n)]
        if not ex:
            return
        win = cmds.window(LIST_WINDOW_NAME, title="Generated BS List", wh=(250, 480))
        cmds.columnLayout(adj=True, rs=2)
        cmds.text(label="Double-click to Isolate", height=25)
        
        self.bs_scroll_list = cmds.textScrollList(
            append=ex, 
            h=340, 
            dcc=self.isolate_selected_bs,
            selectCommand=self.select_only_bs 
        )
        
        cmds.button(label="Toggle Selection Highlighting", h=30, c=self.toggle_selection_highlight)
        cmds.button(label="Turn OFF Isolate", h=30, c=self.disable_isolate)
        cmds.showWindow(win)

    def select_only_bs(self, *args):
        it = cmds.textScrollList(self.bs_scroll_list, q=True, si=True)
        if it:
            cmds.select(it[0], r=True)

    def isolate_selected_bs(self, *args):
        it = cmds.textScrollList(self.bs_scroll_list, q=True, si=True)
        if it:
            pan = cmds.getPanel(wf=True)
            if "modelPanel" not in pan:
                pan = cmds.getPanel(type="modelPanel")[0]
            cmds.isolateSelect(pan, state=False)
            cmds.select(it[0], r=True)
            cmds.isolateSelect(pan, state=True)
            cmds.isolateSelect(pan, addSelected=True)
            cmds.viewFit(f=0.8)

    def toggle_selection_highlight(self, *args):
        pan = cmds.getPanel(wf=True)
        if "modelPanel" in pan:
            st = cmds.modelEditor(pan, q=True, sel=True)
            cmds.modelEditor(pan, e=True, sel=not st)

    def disable_isolate(self, *args):
        pan = cmds.getPanel(wf=True)
        if "modelPanel" in pan:
            cmds.isolateSelect(pan, state=False)

#___________________________________________________________________________________________
# HELPERS

    def run_check_mesh(self, max_inf):
        sel = cmds.ls(sl=True, ap=True)
        if not sel: return []
        cl = self.get_skin_cluster(sel[0])
        if not cl: return []
        vrt = cmds.filterExpand(cmds.polyListComponentConversion(sel[0], tv=True), sm=31)
        res = [v for v in vrt if len(cmds.skinPercent(cl, v, q=True, ib=1e-6, t=None)) > max_inf]
        
        if res:
            cmds.select(res)
            om.MGlobal.displayWarning("Found %d bad vertices." % len(res))
        else:
            om.MGlobal.displayInfo(">> SUCCESS: No vertices > %d influences found!" % max_inf)
            cmds.inViewMessage(amg='<hl>Mesh is Clean!</hl>', pos='midCenter', fade=True)
            
        return res

    def run_zero_controllers(self, *args):
        for ctrl in self.controllers_list:
            finds = cmds.ls("*:" + ctrl) or cmds.ls(ctrl)
            for c in finds:
                for ax in ['translateX', 'translateY']:
                    if not cmds.getAttr(c + '.' + ax, lock=True):
                        cmds.setAttr(c + '.' + ax, 0)
        print ">> Controllers Reset."

    def run_scene_check(self, max_inf):
        res = []
        for cl in cmds.ls(type="skinCluster"):
            for m in cmds.skinCluster(cl, q=True, g=True):
                vs = cmds.filterExpand(cmds.polyListComponentConversion(m, tv=True), sm=31)
                for v in vs:
                    if len(cmds.skinPercent(cl, v, q=True, ib=1e-6, t=None)) > max_inf:
                        res.append(v)
        if res:
            cmds.select(res)
            om.MGlobal.displayWarning("Found %d vertices in scene with > %d influences." % (len(res), max_inf))
        else:
            om.MGlobal.displayInfo(">> SUCCESS: Scene is clean. No vertices > %d influences found." % max_inf)
            cmds.inViewMessage(amg='<hl>Scene is Clean!</hl>', pos='midCenter', fade=True)

    def run_prune(self, *args):
        sel = cmds.ls(sl=True)
        if sel:
            cl = self.get_skin_cluster(sel[0])
            if cl:
                cmds.skinPercent(cl, sel[0].rsplit('.', 1)[0], pruneWeights=0.001)

    def run_set_max_inf(self, *args):
        sel = cmds.ls(sl=True)
        if sel:
            cl = self.get_skin_cluster(sel[0])
            if cl:
                cmds.setAttr(cl + ".maintainMaxInfluences", 1)
                cmds.setAttr(cl + ".maxInfluences", DEFAULT_MAX_INF)

    def add_mesh_to_field(self, *args):
        sel = cmds.ls(sl=True)
        if sel:
            cmds.textField(self.mesh_field, e=1, text=sel[0])
            self.update_toggle_button_ui()

    def clear_mesh_field(self, *args):
        cmds.textField(self.mesh_field, e=1, text="")
        self.update_toggle_button_ui()

    def add_warp_to_field(self, *args):
        sel = cmds.ls(sl=True)
        if sel:
            cmds.textField(self.warp_field, e=1, text=sel[0])

    def clear_warp_field(self, *args):
        cmds.textField(self.warp_field, e=1, text="")

    def add_skinned_to_field(self, *args):
        sel = cmds.ls(sl=True)
        if sel:
            cmds.textField(self.skinned_mesh_field, e=1, text=sel[0])

    def clear_skinned_field(self, *args):
        cmds.textField(self.skinned_mesh_field, e=1, text="")

    def run_gen_blendshapes(self, *args):
        sk = cmds.textField(self.skinned_mesh_field, q=True, text=True)
        if not sk or not cmds.objExists(sk):
            return
        for bs in self.ordered_names:
            if bs not in self.bs_dict: continue
            ctrl = bs.split('_')[0] + "_CT" if '_' in bs else bs + "_CT"
            if not cmds.objExists(ctrl): continue
            at = ".translateX" if ('_IN' in bs or '_OU' in bs) else ".translateY"
            cmds.setAttr(ctrl + at, self.bs_dict[bs])
            cmds.duplicate(sk, n=bs)
            cmds.setAttr(ctrl + at, 0)

    def select_bs_geo(self, *args):
        to_select = [n for n in self.ordered_names if cmds.objExists(n)]
        if to_select:
            cmds.select(to_select)

    def run_create_warp_bs(self, *args):
        t = cmds.textField(self.mesh_field, q=True, text=True)
        w = cmds.textField(self.warp_field, q=True, text=True)
        if cmds.objExists(t) and cmds.objExists(w):
            bs = cmds.blendShape(w, t, n=t+"_WBS")[0]
            cmds.setAttr(bs + "." + w, 1.0)
            self.update_toggle_button_ui()

    def update_toggle_button_ui(self):
        m = cmds.textField(self.mesh_field, q=True, text=True)
        if not m or not cmds.objExists(m):
            cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShape: ---", backgroundColor=[0.3, 0.3, 0.3])
            return
        h = cmds.listHistory(m)
        bs = cmds.ls(h, type='blendShape')
        if not bs:
            cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShape: NONE", backgroundColor=[0.35, 0.3, 0.3])
            return
        w = cmds.listAttr(bs[0] + ".w", multi=True)
        if w:
            val = cmds.getAttr(bs[0] + "." + w[0])
            if val > 0.5:
                cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShape: 1", backgroundColor=[0.3, 0.6, 0.3])
            else:
                cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShape: 0", backgroundColor=[0.6, 0.3, 0.3])

    def run_blendshape_toggle(self, *args):
        m = cmds.textField(self.mesh_field, q=True, text=True)
        if not m or not cmds.objExists(m): return
        h = cmds.listHistory(m); bs = cmds.ls(h, type='blendShape')
        if not bs: return
        for b in bs:
            w = cmds.listAttr(b + ".w", multi=True)
            if not w: continue
            nv = 1.0 if cmds.getAttr(b + "." + w[0]) <= 0.5 else 0.0
            for i in w:
                cmds.setAttr(b + "." + i, nv)
        self.update_toggle_button_ui()

    def delete_fixed_locators(self, *args):
        t = cmds.ls("*_fixed", type="transform")
        if t: cmds.delete(t)

    def delete_constraints(self, *args):
        f = cmds.ls("*_pos", type="transform")
        if f:
            cmds.select(f)
            mel.eval("select -hi")
            c = cmds.ls(sl=True, type="constraint")
            if c:
                cmds.delete(c)
            cmds.select(cl=True)

face_rig_wwz_pipeline()