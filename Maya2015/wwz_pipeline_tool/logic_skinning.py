# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om
import config

def get_skin_cluster(node):
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

def run_zero_controllers():
    for ctrl in config.CONTROLLERS_LIST:
        finds = cmds.ls("*:" + ctrl) or cmds.ls(ctrl)
        for c in finds:
            for ax in ['translateX', 'translateY']:
                if not cmds.getAttr(c + '.' + ax, lock=True):
                    cmds.setAttr(c + '.' + ax, 0)
    print "Controllers Reset"

def check_mesh_inf(max_inf):
    sel = cmds.ls(sl=True, ap=True)
    if not sel: return []
    cl = get_skin_cluster(sel[0])
    if not cl: return []
    vrt = cmds.filterExpand(cmds.polyListComponentConversion(sel[0], tv=True), sm=31)
    res = [v for v in vrt if len(cmds.skinPercent(cl, v, q=True, ib=1e-6, t=None)) > max_inf]
    
    if res:
        cmds.select(res)
        om.MGlobal.displayWarning("Found %d Bad Vertices." % len(res))
    else:
        om.MGlobal.displayInfo("No vertices > %d influences found" % max_inf)
        cmds.inViewMessage(amg='<hl>Mesh is Clean!</hl>', pos='midCenter', fade=True)
    return res

def run_cleanup_loop(max_inf):
    sel = cmds.ls(sl=True)
    if not sel:
        cmds.warning("Please Select a Skinned Mesh")
        return
    cl = get_skin_cluster(sel[0])
    if not cl: return
        
    all_inf = cmds.skinCluster(cl, q=True, inf=True)
    
    # --- AUTO UNLOCK SECTION (No Dialog) ---
    locked_count = 0
    for inf in all_inf:
        if cmds.getAttr(inf + ".liw"):
            cmds.setAttr(inf + ".liw", 0) # Сразу разблокируем
            locked_count += 1
    
    if locked_count > 0:
        print "Auto-unlocked %d influences." % locked_count
    # ---------------------------------------
    
    geo = cmds.skinCluster(cl, q=True, g=True)
    obj = geo[0]
    it = 1
    bad_count = 1
    
    cmds.progressWindow(title='Auto Cleanup Loop', progress=0, isInterruptable=True)
    
    try:
        while bad_count > 0:
            cmds.select(obj, r=True)
            bad_list = check_mesh_inf(max_inf)
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
                if len(inf_l) > max_inf:
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

def run_prune():
    sel = cmds.ls(sl=True)
    if sel:
        cl = get_skin_cluster(sel[0])
        if cl:
            cmds.skinPercent(cl, sel[0].rsplit('.', 1)[0], pruneWeights=0.001)

def set_max_inf(max_inf):
    sel = cmds.ls(sl=True)
    if sel:
        cl = get_skin_cluster(sel[0])
        if cl:
            cmds.setAttr(cl + ".maintainMaxInfluences", 1)
            cmds.setAttr(cl + ".maxInfluences", max_inf)

def run_scene_check(max_inf):
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
        om.MGlobal.displayInfo(">> SUCCESS: Scene is clean.")
        cmds.inViewMessage(amg='<hl>Scene is Clean!</hl>', pos='midCenter', fade=True)

#_____________ Class "Skin Checker Windows" _____________
class SkinMethodChecker(object):
    def __init__(self):
        self.window_name = "checkerSkinMethodUI"
        self.build_ui()
        self.refresh_list()

    def get_meshes_with_wrong_skin_method(self):
        result = []
        skin_clusters = cmds.ls(type='skinCluster') or []
        for sc in skin_clusters:
            try:
                # 2 = Weight Blended
                if cmds.getAttr(sc + ".skinningMethod") != 2: 
                    geometries = cmds.skinCluster(sc, q=True, g=True) or []
                    for geo in geometries:
                        transform = cmds.listRelatives(geo, parent=True, fullPath=True)
                        if transform:
                            result.append((transform[0], sc))
            except:
                pass
        return result

    def refresh_list(self, *args):
        if not cmds.textScrollList(self.tsl, exists=True): return
        
        cmds.textScrollList(self.tsl, e=True, removeAll=True)
        data = self.get_meshes_with_wrong_skin_method()

        for mesh, sc in data:
            label = "{}   [{}]".format(mesh, sc)
            cmds.textScrollList(self.tsl, e=True, append=label)

    def select_mesh(self, *args):
        sel = cmds.textScrollList(self.tsl, q=True, selectItem=True)
        if not sel: return

        to_select = []
        for item in sel:
            mesh = item.split("   ")[0]
            if cmds.objExists(mesh):
                to_select.append(mesh)
        
        if to_select:
            cmds.select(to_select, r=True)

    def fix_selected(self, *args):
        sel = cmds.textScrollList(self.tsl, q=True, selectItem=True)
        if not sel: return

        for item in sel:
            sc = item.split("[")[-1].replace("]", "")
            if cmds.objExists(sc):
                try:
                    cmds.setAttr(sc + ".skinningMethod", 2)
                    print "Fixed:", sc
                except:
                    pass
        self.refresh_list()

    def fix_all(self, *args):
        data = self.get_meshes_with_wrong_skin_method()
        fixed = set()

        for mesh, sc in data:
            if sc in fixed: continue
            if cmds.objExists(sc):
                try:
                    cmds.setAttr(sc + ".skinningMethod", 2)
                    fixed.add(sc)
                except:
                    pass
        
        print "Fixed %d skinClusters." % len(fixed)
        self.refresh_list()

    def build_ui(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)

        self.window = cmds.window(self.window_name, title="Skin Method Checker", widthHeight=(400, 300), sizeable=True)
        cmds.columnLayout(adj=True, rowSpacing=6)

        cmds.text(label="Meshes that don't have the Weight Blend method:", align="left", height=30)

        self.tsl = cmds.textScrollList(height=150, allowMultiSelection=True, selectCommand=self.select_mesh)

        cmds.separator(h=5, style="in")
        
        cmds.rowLayout(numberOfColumns=3, adj=1)
        cmds.button(label="Refresh List", command=self.refresh_list, height=30)
        cmds.button(label="Fix Selected", command=self.fix_selected, height=30)
        cmds.button(label="Fix ALL", command=self.fix_all, height=30)
        cmds.setParent("..")

        cmds.showWindow(self.window)