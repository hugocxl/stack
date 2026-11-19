from geometry import EDGE, oval
from scenes.redraws._w3 import Surface, sheet

DESCRIPTION = "A magnifying glass lies over the heading of a folded-corner document."


def draw(s):
    page = sheet(s, 74, 83, rise=(-.47, .88), depth=5)
    page.rules(10, 63, [43], ink=EDGE)
    page.rules(10, 42, [51, 44, 35], gap=11)

    lens = Surface(s, page.point(0, 0, -3), rise=page.rise, back=page.back)
    align = lens.viewer_axes(44, 62)
    s.tube([lens.point(*align(13.3, -13.3)), lens.point(*align(33, -33))], 3.8)
    outer = [lens.point(*align(x, z)) for x, z in oval(0, 0, 18, 18)[:-1]]
    inner = [lens.point(*align(x, z)) for x, z in oval(0, 0, 14, 14)[:-1]]
    s.face(outer, EDGE, openings=(inner,))
