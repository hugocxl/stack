from geometry import EDGE
from scenes.redraws.page_moved import Surface
from scenes.redraws.replace_file_failed import FILE_OUTLINE, FOLD

DESCRIPTION = "A dashed document outline surrounds a blank page with a small folded corner."


def draw(s):
    page = Surface(s, lean=.26, side=True)
    page.loop(FILE_OUTLINE, EDGE, dashed=True)
    page.line(FOLD, EDGE)
