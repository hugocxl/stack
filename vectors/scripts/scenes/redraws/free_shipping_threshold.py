from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import coin
from scenes.redraws._sf import BACK, capsule, plate, screen

DESCRIPTION = "A delivery truck sits below a progress bar that is filled almost to its flagged free-shipping mark."


def draw(s):
    s.box(-40, -16, 8, 56, 32, 36, 3)
    s.box(16, -16, 8, 24, 32, 24, 4)
    s.face([(40, -12, 24), (40, 12, 24), (40, 12, 30), (40, -12, 30)], DETAIL)
    for x in (-26, 26):
        coin(s, x, 17, 8, 8, 3)
        s.ellipse(x, 17, 8, 0, 0)
    at = screen(0, 0, 0)
    bar = lambda u, v: at(u - 46, v + 64)
    plate(s, bar, capsule(92, 16), 5, BACK)
    s.line([bar(8, 8), bar(64, 8)], BOLD)
    s.line([bar(74, 2), bar(74, 26)], EDGE)
    s.line([bar(74, 26), bar(86, 22), bar(74, 18)], EDGE)
