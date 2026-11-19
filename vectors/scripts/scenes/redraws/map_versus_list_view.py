from geometry import EDGE, rounded
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A two-tab view switcher pairs a folded-map glyph with three bulleted list lines."


def draw(s):
    control = front_surface(s, angle=-8, z=8, lean=.55)
    control.slab(rounded(0, 0, 118, 53, 12), 8)
    control.line([(59, 0), (59, 53)], EDGE)

    folds = ((12, 15, 37), (24, 19, 41), (36, 14, 36), (48, 18, 40))
    outline = [(u, bottom) for u, bottom, _ in folds]
    outline.extend((u, top) for u, _, top in reversed(folds))
    control.outline(outline)
    for u, bottom, top in folds[1:-1]:
        control.line([(u, bottom), (u, top)], EDGE)
    control.line([(16, 25), (24, 32), (36, 23), (44, 31)])

    for v, width in ((39, 23), (27, 19), (15, 23)):
        control.oval(72, v, 1.7, 1.7, EDGE)
        control.rows(80, v, (width,), ink=EDGE)
