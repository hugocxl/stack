from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w3 import Surface, sheet

DESCRIPTION = "A magnifier centers on one outlined match within the ruled lines of a folded-corner document."


def draw(s):
    page = sheet(s, 86, 89, rise=(-.43, .9), depth=6)
    page.rules(11, 75, [26], ink=EDGE)
    page.rules(11, 62, [59, 63])
    page.rules(11, 48, [15])
    page.rules(59, 48, [15])
    page.rules(11, 41, [63, 54, 61, 44], gap=8)
    page.rect(30, 44, 24, 8, 1, EDGE)
    page.rules(34, 48, [16], ink=BOLD)

    lens = Surface(s, page.point(0, 0, -3), rise=page.rise, back=page.back)
    s.tube([lens.point(56, 34, 2), lens.point(79, 12, 2)], 4.5)
    outer = oval(42, 48, 21, 21, count=48)[:-1]
    inner = oval(42, 48, 17, 17, count=48)[:-1]
    s.face([lens.point(*p) for p in outer], EDGE,
           openings=[[lens.point(*p) for p in inner]])
