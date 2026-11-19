from geometry import BOLD, EDGE, oval
from scenes.redraws._w4 import paper

DESCRIPTION = "A thick step-goal ring surrounds a footprint and leaves one progress segment open."


def draw(s):
    dial = paper(s, 93, pitch=.86, run=.42, angle=-22, depth=6)
    outer = oval(0, 46, 49, 45, -25, 285, 64)
    inner = oval(0, 46, 36, 33, 285, -25, 64)
    dial.slab([*outer, *inner], 6, EDGE)

    sole = [(-13, 71), (-19, 66), (-18, 60), (-12, 52), (-13, 44),
            (-12, 37), (-7, 33), (3, 33), (10, 37), (12, 43), (10, 50),
            (3, 55), (0, 62), (-3, 68), (-8, 71)]
    dial.outline(sole, BOLD)
    for x, y, r in ((9, 26, 4.4), (-1, 24, 3.6), (-9, 26, 2.8),
                    (-16, 30, 2.3)):
        dial.oval(x, y, r, r, EDGE)
