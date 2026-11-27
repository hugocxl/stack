from geometry import DETAIL, EDGE
from scenes.redraws._sf import plane, plate

DESCRIPTION = "An empty folder stands open, its front cover tipped forward to show nothing inside."


def tabbed(w, h, tab=(6, 30, 7)):
    a, b, t = tab
    return [(0, 0), (w, 0), (w, h), (b + 6, h), (b, h + t), (a + 4, h + t), (a, h + t - 2), (0, h + t - 2)][:3] + \
        [(b + 6, h), (b, h + t), (a + 3, h + t), (a, h + t - 3), (0, h + t - 3)]


def draw(s):
    w, h = 96, 66
    back = plane((-w/2, 0, 0), (1, 0, 0), (0, -.12, .99))
    plate(s, back, tabbed(w, h), 3, (0, -.99, -.12))
    s.line([back(6, 8), back(w - 6, 8)], DETAIL)
    front = plane((-w/2, 2, 0), (1, 0, 0), (0, .4, .92))
    plate(s, front, [(0, 0), (w, 0), (w, h - 6), (0, h - 6)], 3, (0, -.92, .4))
