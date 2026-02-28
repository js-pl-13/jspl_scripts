# -*- coding: utf-8 -*-
# config.py
import os
import tempfile

# Путь, где будут храниться Проекты -> Персонажи -> Анимации
# Скрипт сам создаст эту папку, если её нет.
BASE_PROJECT_PATH = r"D:\!MyScripts\jspl_transform_anims"

# Путь к временному файлу (можно оставить в Temp системы или поменять на BASE_PROJECT_PATH)
TEMP_FILE_PATH = os.path.join(tempfile.gettempdir(), "maya_joint_export.json")