from geometry import BOLD, EDGE, GUIDE, oval, rounded
from scenes.redraws._w3 import Surface, component_art

DESCRIPTION = "A magnifier shows the padding measurement between a component diamond and its selection boundary."


def draw(s):
    tile = Surface(s, (0, 0, 0), rise=(-.48, .88), back=(0, -.88, -.48),
                   across=(.96, -.28))
    tile.plate(rounded(0, 0, 72, 65, 8), 9)
    component_art(tile, 28, 40, 32, 26, EDGE)
    tile.stroke([(9, 13), (64, 13), (64, 57), (9, 57), (9, 13)], GUIDE, dashed=True)
    for x in (44, 64):
        tile.stroke([(x, 24), (x, 36)], EDGE)
    tile.rules(44, 30, [20], ink=BOLD)

    lens = Surface(s, tile.point(0, 0, -4), rise=tile.rise, back=tile.back, across=tile.across)
    s.tube([lens.point(68, 20, 3), lens.point(86, 3, 3)], 4.3, EDGE)
    s.face([lens.point(*p) for p in oval(55, 30, 18, 18)[:-1]], EDGE,
           openings=[[lens.point(*p) for p in oval(55, 30, 14, 14)[:-1]]])
