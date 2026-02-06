import maya.mel as mel
import maya.cmds as cmds

class _skinToolset:
    def __init__(self):
        print('skinToolset initialized.')
        
    def getCurrentPanel(self, list):
        for iter_panel in list:
            if 'modelPanel' in iter_panel:
                return iter_panel
                break

    def setJointXray(self):
        currentModelPanel = cmds.getPanel(withFocus=True)
        currentPanel = ''
        
        if "modelPanel" not in currentModelPanel:
            currentModelPanel = cmds.getPanel(vis=True)
            currentPanel = self.getCurrentPanel(currentModelPanel)
        	
        currentPanel = self.getCurrentPanel(currentModelPanel)
        print(currentPanel)
        if not (cmds.modelEditor(currentPanel, q=True, jointXray=True)):
            print(cmds.modelEditor(currentPanel, q=True, jointXray=True))
            cmds.modelEditor(currentPanel, edit=True, jointXray=True)
        else:
            print(cmds.modelEditor(currentPanel, q=True, jointXray=True))
            cmds.modelEditor(currentPanel, edit=True, jointXray=False)	
	

    def color_paint(arg):
        mel.eval("ArtPaintSkinWeightsToolOptions; artAttrSkinPaintCtx -e -colorfeedback true `currentCtx`;")
    def mesh_paint(self):
        ##self.setJointXray()
        mel.eval("ArtPaintSkinWeightsToolOptions; artAttrSkinPaintCtx -e -colorfeedback false `currentCtx`;")
    def selection_on(arg):
        mel.eval("modelEditor -e -sel true modelPanel4;")
    def selection_off(arg):
        mel.eval("modelEditor -e -sel false modelPanel4;")    
    def skin_value_1(arg):
        mel.eval("artSkinSetSelectionValue 1 false artAttrSkinPaintCtx artAttrSkin;")
    def skin_value_095(arg):
        mel.eval("artSkinSetSelectionValue 0.95 false artAttrSkinPaintCtx artAttrSkin;")
    def skin_value_075(arg):
        mel.eval("artSkinSetSelectionValue 0.75 false artAttrSkinPaintCtx artAttrSkin;")
    def skin_value_05(arg):
        mel.eval("artSkinSetSelectionValue 0.5 false artAttrSkinPaintCtx artAttrSkin;")
    def skin_value_025(arg):
        mel.eval("artSkinSetSelectionValue 0.25 false artAttrSkinPaintCtx artAttrSkin;")
    def skin_value_005(arg):
        mel.eval("artSkinSetSelectionValue 0.05 false artAttrSkinPaintCtx artAttrSkin;")
    def skin_value_0(arg):
        mel.eval("artSkinSetSelectionValue 0 false artAttrSkinPaintCtx artAttrSkin;")
        
    def hammer_value(arg):
        mel.eval("weightHammerVerts;")
    def skin_weight_copy(arg):
        mel.eval("artAttrSkinWeightCopy;")
    def skin_weight_paste(arg):
        mel.eval("artAttrSkinWeightPaste;")