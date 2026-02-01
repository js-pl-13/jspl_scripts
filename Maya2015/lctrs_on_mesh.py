# -*- coding: utf-8 -*-
import maya.cmds as cmds
import os

# ----------------- НАСТРОЙКИ -----------------
PLUGIN_PATH = r"D:\!GIT\jspl_scripts\Maya2015\FaceRig\x64\Release\fixLocators.mll"
MESH_NAME   = 'clerk_girl_head_head2'
# ---------------------------------------------

plugin_name = os.path.basename(PLUGIN_PATH)

# 1. Перезагрузка плагина
if cmds.pluginInfo(plugin_name, query=True, loaded=True):
    try:
        cmds.unloadPlugin(plugin_name)
        print "Плагин выгружен"
    except:
        print "Не удалось выгрузить плагин (возможно используется)"

try:
    cmds.loadPlugin(PLUGIN_PATH)
    print "Плагин загружен:", plugin_name
except Exception, e:
    cmds.error("Ошибка загрузки плагина: " + str(e))

# 2. Запуск
if not cmds.objExists(MESH_NAME):
    cmds.error("Меш '%s' не найден!" % MESH_NAME)

cmds.select(clear=True)

# Вызываем C++ команду
cmds.fixLocators(MESH_NAME)

print "Выполнение C++ команды завершено"