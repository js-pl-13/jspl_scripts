# -*- coding: utf-8 -*-
import maya.cmds as cmds
import config

def run_gen_blendshapes(skinned_head):
    if not skinned_head or not cmds.objExists(skinned_head):
        return
    for bs in config.ORDERED_NAMES:
        if bs not in config.BS_DICT: continue
        ctrl = bs.split('_')[0] + "_CT" if '_' in bs else bs + "_CT"
        if not cmds.objExists(ctrl): continue
        at = ".translateX" if ('_IN' in bs or '_OU' in bs) else ".translateY"
        cmds.setAttr(ctrl + at, config.BS_DICT[bs])
        cmds.duplicate(skinned_head, n=bs)
        cmds.setAttr(ctrl + at, 0)

def select_bs_geo():
    to_select = [n for n in config.ORDERED_NAMES if cmds.objExists(n)]
    if to_select:
        cmds.select(to_select)

# _____________ Class "List BS Windows" _____________
class BSListWindow(object):
    def __init__(self):
        self.window_name = config.LIST_WINDOW_NAME
        self.show()

    def show(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)
        
        ex = [n for n in config.ORDERED_NAMES if cmds.objExists(n)]
        if not ex: return

        win = cmds.window(self.window_name, title="BS List", wh=(250, 480))
        cmds.columnLayout(adj=True, rs=2)
        cmds.text(label="Double-Click to Mesh = Isolate", height=25)
        
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
                mps = cmds.getPanel(type="modelPanel")
                if mps: pan = mps[0]
            
            if pan:
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