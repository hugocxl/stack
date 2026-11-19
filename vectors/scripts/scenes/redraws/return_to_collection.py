from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import bezier_path, front_surface

DESCRIPTION = "A thick tabbed collection folder has a curved return arrow printed on its raised tab."


def draw(s):
    angle = -24
    folder = front_surface(s, angle=angle, y=-5, z=6, lean=.26)
    folder.slab([(0, 0), (90, 0), (90, 54), (54, 54), (46, 73),
                 (6, 73), (0, 67)], 5)
    front = front_surface(s, angle=angle, y=4, z=6, lean=.08)
    s.face([folder.at(90, 0), folder.at(90, 41), front.at(90, 42), front.at(90, 0)])
    front.slab([(0, 0), (90, 0), (90, 42), (85, 48), (0, 48)], 5)
    front.rows(13, 13, (25,))
    front.rows(13, 20, (35,), ink=EDGE)
    turn = bezier_path((39, 54), ((48, 54), (46, 65), (34, 65)))
    end = [(27, 65), (16, 65)]
    arrow(s, [folder.at(u, v) for u, v in turn + end], BOLD, head=8)
