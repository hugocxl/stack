from geometry import DETAIL, EDGE
from scenes.redraws._sf import plane, plate, smooth

DESCRIPTION = "A sheet arcs from one tray into the next along a dashed path."


def tray(s, x, y):
    s.box(x, y, 0, 50, 38, 9, 3)
    s.line([(x + 4, y + 4, 9), (x + 46, y + 4, 9), (x + 46, y + 34, 9)], DETAIL)


def draw(s):
    tray(s, -70, -6)
    tray(s, 22, 6)
    s.line([(x, y, z) for x, y, z in smooth([(-44, 12, 12), (-24, 12, 52), (14, 16, 58), (46, 24, 14)], 8)], DETAIL, dashed=True)
    sheet = plane((-24, 0, 40), (.96, .2, -.18), (0, .28, .96))
    plate(s, sheet, [(0, 0), (46, 0), (46, 36), (0, 36)], 1.6, (0, -.96, .28))
    for v in (22, 15, 8):
        s.line([sheet(8, v + 4), sheet(36, v + 4)], DETAIL)
    s.line([(41, 23, 21), (46, 24, 14), (50, 20, 20)], EDGE)
