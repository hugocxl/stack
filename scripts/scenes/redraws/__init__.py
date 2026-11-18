"""Hand-authored redraws that replace a figure's recipe composition.

Each module in this package is named after the figure it draws (dashes become
underscores) and defines draw(s) and DESCRIPTION. Modules whose names start
with an underscore hold shared helpers.
"""
from importlib import import_module
from pathlib import Path

REDRAWS = {}
for module_path in sorted(Path(__file__).parent.glob("[!_]*.py")):
    module = import_module(f"{__name__}.{module_path.stem}")
    REDRAWS[module_path.stem.replace("_", "-")] = (module.draw, module.DESCRIPTION)
