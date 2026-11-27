from geometry import EDGE
from scenes.redraws._sf import cylinder_db, smooth

DESCRIPTION = "Three cables gather into one hub that feeds a single database."


def draw(s):
    cylinder_db(s, 40, -20, 0, 24, 46)
    s.tube([(-2, -2, 12), (24, -10, 12)], 3.2, EDGE)
    for y in (-30, 0, 30):
        s.tube(smooth([(-70, y, 12), (-40, y, 12), (-22, y*.3, 12), (-6, 0, 12)], 6), 2.2, EDGE)
    s.disk(-6, 0, 6, 9, 9, 12)
