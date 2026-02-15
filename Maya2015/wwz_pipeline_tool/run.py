import sys
import os

TOOL_PATH = r"U:\AssetStorage\CharTools\wwz_pipeline_tool"

if TOOL_PATH not in sys.path:
    sys.path.insert(0, TOOL_PATH)

import run_wwz_tool

reload(run_wwz_tool)

run_wwz_tool.run()
# ___________________________________________________________