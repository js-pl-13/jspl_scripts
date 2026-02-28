# -*- coding: utf-8 -*-
# main.py
import sys

# Импортируем модули
from . import ui
from . import config
from . import utils
from . import project_manager
from . import data_handler
from . import auto_rotation

# --- ЛОГИКА ПЕРЕЗАГРУЗКИ ---
# 1. Получаем функцию reload в зависимости от версии Python (2 или 3)
if sys.version_info[0] >= 3:
    from importlib import reload
else:
    # В Python 2.7 reload встроенная, импортировать не нужно
    pass 

# 2. Перезагружаем модули по порядку
# ВАЖНО: Мы убрали try/except, чтобы если в коде ошибка, Maya написала об этом,
# а не молча запустила старую версию.
print("Reloading modules...")
reload(config)
reload(utils)
reload(project_manager)
reload(data_handler)
reload(auto_rotation)
reload(ui)
print("Reload complete.")

def run():
    # Проверка создания папки данных при старте
    utils.ensure_base_path()
    # Запуск окна
    ui.create_window()

# Если файл запускается напрямую
if __name__ == "__main__":
    run()