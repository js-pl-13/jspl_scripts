import sys
import os

# Путь к GitHub папке
project_root = r"D:\GitHub\jspl_scripts"

if project_root not in sys.path:
    sys.path.insert(0, project_root)

import jspl_anims_tool.main

# Перезагружаем сам main, чтобы он запустил перезагрузку остальных
try:
    from importlib import reload
except:
    pass

reload(jspl_anims_tool.main)

# Запускаем
jspl_anims_tool.main.run()