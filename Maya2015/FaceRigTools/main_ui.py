# -*- coding: utf-8 -*-
import maya.cmds as cmds
import config
# Импортируем логику (перезагружаем на случай правок без перезапуска Maya)
import logic_locators
reload(logic_locators)
import logic_blendshapes
reload(logic_blendshapes)
import logic_skinning
reload(logic_skinning)

class LocatorsTool(object):
    def __init__(self):
        self.prepare_environment()
        self.show_ui()

    def prepare_environment(self):
        if not cmds.pluginInfo("closestPointOnMesh", q=True, loaded=True):
            try:
                cmds.loadPlugin("closestPointOnMesh")
            except:
                print "Warning: closestPointOnMesh could not be loaded."

    def show_ui(self):
        if cmds.window(config.WINDOW_NAME, exists=True):
            cmds.deleteUI(config.WINDOW_NAME)

        self.window = cmds.window(config.WINDOW_NAME, title="Face Rig Pipeline Modular", widthHeight=(360, 850), sizeable=True)
        main_layout = cmds.columnLayout(adj=True, rowSpacing=5)

        # === BLOCK 1: Locators ===
        cmds.frameLayout(label="1. Blendshapes & Locators Setup", borderStyle="etchedIn", marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
        self.mesh_field = cmds.textField(placeholderText="Add Base Mesh...")
        
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=30, c=lambda x: self.fill_field(self.mesh_field, update_toggle=True))
        cmds.button(label="Clear", height=30, c=lambda x: self.clear_field(self.mesh_field, update_toggle=True))
        cmds.setParent("..")
        
        self.warp_field = cmds.textField(placeholderText="Add Warp Mesh...")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=30, c=lambda x: self.fill_field(self.warp_field))
        cmds.button(label="Clear", height=30, c=lambda x: self.clear_field(self.warp_field))
        cmds.setParent("..")
        
        cmds.button(label="Create Warp BlendShape", height=30, command=self.ui_create_warp)
        cmds.separator(h=10, style="in")
        
        # Кнопка Fix Locators вызывает логику из logic_locators
        cmds.button(label="RUN FIX LOCATORS", height=30, command=lambda x: logic_locators.run_fix(self.get_val(self.mesh_field)))
        
        self.toggle_btn = cmds.button(label="Toggle BlendShape: ---", height=30, c=self.ui_toggle_bs, backgroundColor=[0.35, 0.35, 0.35])
        self.update_toggle_button_ui() # Check init status
        
        cmds.separator(h=10, style="none")
        cmds.button(label="Del. Constraints", height=30, c=lambda x: logic_locators.delete_constraints())
        cmds.button(label="Del. Fixed Locs", height=30, c=lambda x: logic_locators.delete_fixed_locators())
        
        # EXPORT / IMPORT
        cmds.separator(h=5, style="none")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[175, 175])
        cmds.button(label="Export Pos Data", height=30, command=lambda x: logic_locators.export_loc_data(), backgroundColor=[0.3, 0.4, 0.4])
        cmds.button(label="Import Pos Data", height=30, command=lambda x: logic_locators.import_loc_data(), backgroundColor=[0.4, 0.4, 0.3])
        cmds.setParent("..")
        cmds.setParent("..")
        cmds.setParent("..")

        # === BLOCK 2: Generator ===
        cmds.frameLayout(label="2. Final Skin & Face BS Generator", borderStyle="etchedIn", marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
        self.skinned_mesh_field = cmds.textField(placeholderText="Add Skinned Head...")
        cmds.rowLayout(nc=2, adj=1, columnWidth2=[210, 50])
        cmds.button(label="Add Selected", height=30, c=lambda x: self.fill_field(self.skinned_mesh_field))
        cmds.button(label="Clear", height=30, c=lambda x: self.clear_field(self.skinned_mesh_field))
        cmds.setParent("..")
        
        cmds.button(label="GENERATE BLENDSHAPES", height=40, command=lambda x: logic_blendshapes.run_gen_blendshapes(self.get_val(self.skinned_mesh_field)))
        cmds.button(label="Select Generated", height=30, command=lambda x: logic_blendshapes.select_bs_geo())
        cmds.button(label="Show All Generated BlendShape", height=30, command=lambda x: logic_blendshapes.BSListWindow())
        cmds.setParent("..")
        cmds.setParent("..")

        # === BLOCK 3: Skin Cleanup ===
        cmds.frameLayout(label="3. Clean Skin (Max 4 Inf)", borderStyle="etchedIn", marginWidth=5, marginHeight=5)
        cmds.columnLayout(adj=True, rowSpacing=5)
        cmds.button(label="Reset All Controller", height=30, command=lambda x: logic_skinning.run_zero_controllers())
        cmds.button(label="Check Scene (Max 4)", height=30, command=lambda x: logic_skinning.run_scene_check(config.DEFAULT_MAX_INF))
        cmds.separator(h=5, style="in")
        cmds.button(label="STEP 1: Check Selected Mesh", height=30, command=lambda x: logic_skinning.check_mesh_inf(config.DEFAULT_MAX_INF))
        cmds.button(label="STEP 2: FULL AUTO CLEANUP", height=40, command=lambda x: logic_skinning.run_cleanup_loop(config.DEFAULT_MAX_INF))
        cmds.button(label="STEP 3: Prune (0.001)", height=30, command=lambda x: logic_skinning.run_prune())
        cmds.button(label="STEP 4: Set Max Influence (4)", height=30, command=lambda x: logic_skinning.set_max_inf(config.DEFAULT_MAX_INF))
        cmds.setParent("..")
        cmds.setParent("..")

        cmds.showWindow(self.window)

    # --- UI Helpers methods (local) ---
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
        # Вызываем логику и обновляем UI
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
             cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShape: 1", backgroundColor=[0.3, 0.6, 0.3])
        else:
             cmds.button(self.toggle_btn, edit=True, label="Toggle BlendShape: 0", backgroundColor=[0.6, 0.3, 0.3])

# Запуск
if __name__ == "__main__":
    LocatorsTool()