from geometry import EDGE
from scenes.redraws.page_moved import Surface
from scenes.redraws.replace_file_failed import FILE_OUTLINE, FOLD

DESCRIPTION = "An empty upload tray holds the dashed outline of an upright file above its opening."


def draw(s):
    s.box(0, 0, 0, 95, 51, 6, 4)
    s.face([(0, 0, 6), (95, 0, 6), (95, 0, 25), (0, 0, 25)])
    s.face([(0, 0, 6), (0, 51, 6), (0, 51, 16), (0, 0, 25)])
    page = Surface(s, (19, 21, 11), lean=.24)
    page.loop(FILE_OUTLINE, EDGE, dashed=True)
    page.line(FOLD, EDGE, dashed=True)
    s.face([(95, 0, 6), (95, 51, 6), (95, 51, 16), (95, 0, 25)])
    s.face([(0, 51, 0), (95, 51, 0), (95, 51, 16), (67, 51, 16),
            (61, 51, 10), (34, 51, 10), (28, 51, 16), (0, 51, 16)])
