from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws.page_moved import Surface

DESCRIPTION = "An open laptop shows a job progress bar and carries a clock badge beside its screen."


def draw(s):
    screen = Surface(s, (0, 0, 7), lean=.25)
    screen.plate(rounded(0, 0, 104, 67, 5), 5)
    screen.frame(6, 6, 92, 55, 3)
    screen.frame(20, 16, 63, 36, 3, EDGE)
    screen.line([(20, 42), (83, 42)])
    screen.line([(29, 34), (57, 34)])
    screen.frame(28, 23, 44, 5, 2, EDGE)
    screen.line([(30, 25.5), (53, 25.5)], EDGE)
    s.box(0, 0, 0, 104, 46, 7, 5)
    s.line([(15, 9, 7), (89, 9, 7)])
    s.line([(15, 16, 7), (89, 16, 7)])
    s.line([(15, 23, 7), (89, 23, 7)])
    trackpad = rounded(38, 29, 28, 11, 2)
    s.line([(x, y, 7) for x, y in [*trackpad, trackpad[0]]])
    badge(s, "clock", *screen.point(103, 49), 14)
