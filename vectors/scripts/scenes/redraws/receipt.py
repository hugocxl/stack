from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._sf import plane, plate

DESCRIPTION = "A tall receipt with a torn zigzag foot leans back, its itemized lines ending in a bold total."


def draw(s):
    w, h = 64, 100
    at = plane((-w/2, 0, 0), (1, 0, 0), (0, -.36, .93))
    teeth = 8
    foot = [(w - i*w/(teeth*2), 0 if i % 2 == 0 else 5) for i in range(teeth*2 + 1)]
    outline = [(0, 5)] + foot[::-1][1:] + [(w, h - 4), (w - 4, h), (4, h), (0, h - 4)]
    outline = [(0, 0)] + [(u, v) for u, v in foot[::-1]] + [(w, h - 4), (w - 4, h), (4, h), (0, h - 4)]
    plate(s, at, outline, 2.5, (0, -.93, -.36))
    for v, width in ((84, 30), (72, 44), (64, 40), (56, 46), (48, 36)):
        s.line([at(10, v), at(10 + width*.62, v)], DETAIL)
        s.line([at(w - 16, v), at(w - 10, v)], DETAIL)
    s.line([at(10, 34), at(w - 10, 34)], DETAIL, dashed=True)
    s.line([at(10, 22), at(30, 22)], BOLD)
    s.line([at(w - 22, 22), at(w - 10, 22)], BOLD)
