# -*- coding: utf-8 -*-
# utils.py
import maya.cmds as cmds
import os
from . import config

def ensure_base_path():
    """Создает базовую папку проектов, если её нет."""
    if not os.path.exists(config.BASE_PROJECT_PATH):
        try:
            os.makedirs(config.BASE_PROJECT_PATH)
            print("Created base data directory: {}".format(config.BASE_PROJECT_PATH))
        except Exception as e:
            cmds.warning("Could not create base path: {}. Error: {}".format(config.BASE_PROJECT_PATH, str(e)))

def remove_namespace(object_name):
    if ":" in object_name:
        return object_name.split(":")[-1]
    return object_name

def unlock_attribute(attribute):
    if cmds.attributeQuery(attribute.split('.')[-1], node=attribute.split('.')[0], exists=True):
        if cmds.getAttr(attribute, lock=True):
            cmds.setAttr(attribute, lock=False)

def get_namespace_from_root():
    if cmds.textField("root_text_field", exists=True):
        root_text = cmds.textField("root_text_field", query=True, text=True)
        if root_text and root_text != ":ROOT":
            if ":" in root_text:
                return root_text.rsplit(":", 1)[0] + ":"
            else:
                return ""
    return ""