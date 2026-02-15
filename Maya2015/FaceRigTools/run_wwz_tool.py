# -*- coding: utf-8 -*-
import sys
import os
import maya.cmds as cmds

def run():
    # 1. Автоматически получаем путь к папке, где лежит этот файл run.py
    # Это лучше, чем хардкодить путь, так как скрипт будет работать из любой папки.
    current_path = os.path.dirname(os.path.abspath(__file__))

    # 2. Добавляем путь в sys.path, если его там нет
    if current_path not in sys.path:
        sys.path.insert(0, current_path)

    try:
        # 3. Импортируем главный файл UI
        import main_ui
        
        # 4. ОБЯЗАТЕЛЬНО: Перезагружаем модуль. 
        # Это позволяет обновлять код в main_ui.py и видеть изменения без перезапуска Maya.
        reload(main_ui)
        
        # 5. Запускаем инструмент
        if hasattr(main_ui, 'LocatorsTool'):
            main_ui.LocatorsTool()
        else:
            cmds.warning("Class 'LocatorsTool' not found in main_ui.py")
            
    except ImportError as e:
        cmds.error(u"Import Error. Check if main_ui.py exists in {}.\nLog: {}".format(current_path, e))
    except Exception as e:
        cmds.error(u"Critical Error executing FaceRigTools: {}".format(e))

# Важно: Мы НЕ вызываем run() здесь в конце файла.
# Его вызовет ваш Script Manager автоматически.