import maya.cmds as cmds
import os

# --- НАСТРОЙКИ ---
# Укажите точный путь к вашему файлу fixLocators.mll
# Обратите внимание на букву r перед кавычками для путей Windows
PLUGIN_PATH = r"D:\GitHub\jspl_scripts\Maya2015\FaceRig\x64\Release\fixLocators.mll"

# Имя меша
MESH_NAME = 'clerk_girl_head_head2'
# -----------------

# 1. Загрузка плагина
plugin_name = os.path.basename(PLUGIN_PATH)

# Если плагин уже загружен - выгружаем для обновления
if cmds.pluginInfo(plugin_name, q=True, loaded=True):
    try:
        cmds.unloadPlugin(plugin_name)
        print "Plugin unloaded."
    except:
        print "Could not unload plugin (maybe in use)."

# Загружаем
try:
    cmds.loadPlugin(PLUGIN_PATH)
    print "Plugin loaded successfully: " + plugin_name
except Exception as e:
    cmds.error("Failed to load plugin: " + str(e))

# 2. Выполнение команды
if cmds.objExists(MESH_NAME):
    # Чистим выделение, чтобы C++ нашел объекты сам
    cmds.select(cl=True)
    
    # ЗАПУСК C++ КОМАНДЫ
    # Аргумент - имя меша
    cmds.fixLocators(MESH_NAME)
    
    print "C++ execution finished."
else:
    cmds.error("Mesh '" + MESH_NAME + "' not found!")