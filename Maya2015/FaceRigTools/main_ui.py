# -*- coding: utf-8 -*-
import maya.cmds as cmds
import config
reload(config)
import logic_locators
reload(logic_locators)
import logic_blendshapes
reload(logic_blendshapes)
import logic_skinning
reload(logic_skinning)
import logic_lods
reload(logic_lods)

class LocatorsTool(object):
    def __init__(self):
        self.prepare_environment()
        self.show_ui()

    def prepare_environment(self):
        if not cmds.pluginInfo("closestPointOnMesh", q=True, loaded=True):
            try:
                cmds.loadPlugin("closestPointOnMesh")
            except:
                pass 

    def show_ui(self):
        if cmds.window(config.WINDOW_NAME, exists=True):
            cmds.deleteUI(config.WINDOW_NAME)

        self.window = cmds.window(config.WINDOW_NAME, title="WWZ Pipeline Modular", widthHeight=(360, 950), sizeable=True)
        main_layout = cmds.columnLayout(adj=True, rowSpacing=5)

        # _____________ BLOCK 1: Locators _____________
        cmds.frameLayout(label="1. Create BlendShapes | Locators Setup", collapsable=True, marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
        
        self.mesh_field = cmds.textField(placeholderText="Add Base Mesh...")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=25, c=lambda x: self.fill_field(self.mesh_field, update_toggle=True))
        cmds.button(label="Clear", height=25, c=lambda x: self.clear_field(self.mesh_field, update_toggle=True))
        cmds.setParent("..")
        
        self.warp_field = cmds.textField(placeholderText="Add Warp Mesh...")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=25, c=lambda x: self.fill_field(self.warp_field))
        cmds.button(label="Clear", height=25, c=lambda x: self.clear_field(self.warp_field))
        cmds.setParent("..")
        
        cmds.button(label="Create Warp BlendShape", height=25, command=self.ui_create_warp)
        cmds.separator(h=10, style="in")
        cmds.button(label="Run Fix Locators (only maya 2019)", ann="This Script Only Works In Maya 2019", height=25, c=lambda x: logic_locators.run_fix(self.get_val(self.mesh_field)))
        self.toggle_btn = cmds.button(label="Toggle BlendShape: ---", height=25, c=self.ui_toggle_bs, backgroundColor=[0.35, 0.35, 0.35])
        self.update_toggle_button_ui() 
        cmds.separator(h=10, style="in")
        cmds.button(label="Del. Constraints", height=25, c=lambda x: logic_locators.delete_constraints())
        cmds.button(label="Del. Fixed Locs", height=25, c=lambda x: logic_locators.delete_fixed_locators())
        cmds.separator(h=10, style="in")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[175, 175])
        cmds.button(label="Exporting new *locRot_pos", ann="Export New Locators Transformations From Maya 2019", height=25, c=lambda x: logic_locators.export_loc_data())
        cmds.button(label="Import new *locRot_pos", ann="Import New Locators Transformations To Maya 2015", height=25, c=lambda x: logic_locators.import_loc_data())
        cmds.setParent("..")
        cmds.setParent("..")
        cmds.setParent("..")

        # _____________ BLOCK 2: Face BS Generator _____________
        cmds.frameLayout(label="2. Face BS Generator", collapsable=True, marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
        self.skinned_mesh_field = cmds.textField(placeholderText="Add Skinned Head (8 Influences)...")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=25, c=lambda x: self.fill_field(self.skinned_mesh_field))
        cmds.button(label="Clear", height=25, c=lambda x: self.clear_field(self.skinned_mesh_field))
        cmds.setParent("..")
        cmds.button(label="Generate BlebdShapes", height=30, c=lambda x: logic_blendshapes.run_gen_blendshapes(self.get_val(self.skinned_mesh_field)))
        cmds.button(label="Select Generated", height=25, c=lambda x: logic_blendshapes.select_bs_geo())
        cmds.button(label="Show All Generated BlendShape", height=25, c=lambda x: logic_blendshapes.BSListWindow())
        cmds.setParent("..")
        cmds.setParent("..")

        # _____________ BLOCK 3: Clean Skin _____________
        cmds.frameLayout(label="3. Clean Skin (Max Influence = 4)", collapsable=True, marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
        cmds.button(label="Reset All Controller", height=25, c=lambda x: logic_skinning.run_zero_controllers())
        cmds.button(label="Check Scene (Max 4)", height=25, c=lambda x: logic_skinning.run_scene_check(config.DEFAULT_MAX_INF))
        cmds.separator(h=5, style="in")
        cmds.button(label="Step 1: Check Selected Mesh", height=25, c=lambda x: logic_skinning.check_mesh_inf(config.DEFAULT_MAX_INF))
        cmds.button(label="Step 2: Full Auto Cleanup", height=30, c=lambda x: logic_skinning.run_cleanup_loop(config.DEFAULT_MAX_INF))
        cmds.button(label="Step 3: Prune (0.001)", height=25, c=lambda x: logic_skinning.run_prune())
        cmds.button(label="Step 4: Set Max Influence = 4", height=25, c=lambda x: logic_skinning.set_max_inf(config.DEFAULT_MAX_INF))
        cmds.separator(h=5, style="in")
        cmds.button(label="Check Skin Method", height=25, c=lambda x: logic_skinning.SkinMethodChecker())
        cmds.setParent("..")
        cmds.setParent("..")

        # _____________ BLOCK 4: LOD Tools _____________
        cmds.frameLayout(label="4. Character LODs", collapsable=True, marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
                
        cmds.button(label="Export Layers LODs (LOD1 - LOD5)", ann="Exports layers in DAE to a folder 'D:/data_scripts/characters_lods'", height=25, c=lambda x: logic_lods.export_all_lods())
        
        cmds.button(label="Import Layers LODs (LOD1 - LOD5) + Materials", ann="Imports layers and copies material from the base mesh", height=25, c=lambda x: logic_lods.import_all_dae())
        
        cmds.separator(h=5, style="in")
        
        cmds.button(label="Copy Skin From Base Mesh to |*_game_LOD1..5|", ann="Copies the skin from the base mesh to the LODs", height=25, c=lambda x: logic_lods.copy_skin_to_game_lods(),)
        
        cmds.setParent("..")
        cmds.setParent("..")
        # _______________________________________________________________________________________________________________________________________________

        cmds.showWindow(self.window)

    # --- UI Helpers ---
    def get_val(self, field):
        return cmds.textField(field, q=True, text=True)

    def fill_field(self, field, update_toggle=False):
        sel = cmds.ls(sl=True)
        if sel:
            cmds.textField(field, e=1, text=sel[0])
            if update_toggle: self.update_toggle_button_ui()

    def clear_field(self, field, update_toggle=False):
        cmds.textField(field, e=1, text="")
        if update_toggle: self.update_toggle_button_ui()

    def ui_create_warp(self, *args):
        res = logic_locators.create_warp_bs(self.get_val(self.mesh_field), self.get_val(self.warp_field))
        if res: self.update_toggle_button_ui()

    def ui_toggle_bs(self, *args):
        logic_locators.toggle_blendshape(self.get_val(self.mesh_field))
        self.update_toggle_button_ui()

    def update_toggle_button_ui(self):
        status = logic_locators.check_bs_status(self.get_val(self.mesh_field))
        if status == "none":
             cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShape: NONE", backgroundColor=[0.35, 0.3, 0.3])
        elif status == "on":
             cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShape: 1",backgroundColor=[0.3, 0.6, 0.3])
        else:
             cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShape: 0", backgroundColor=[0.6, 0.3, 0.3])




if __name__ == "__main__":
    LocatorsTool()