from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import bezier_path, front_surface, upright

DESCRIPTION = "An hourglass shows its remaining sand as a marked level in the upper bulb and a stream falling below."


def draw(s):
    angle = -36
    glass = front_surface(s, angle=angle, y=2)
    left = bezier_path((-27, 6),
                       ((-30, 22), (-25, 33), (-16, 40)),
                       ((-9, 46), (-4, 48), (-4, 53)),
                       ((-4, 58), (-12, 61), (-19, 69)),
                       ((-25, 76), (-28, 83), (-27, 91)))
    right = [(-u, v) for u, v in reversed(left)]
    upright(s, left + right, 2, 6, angle=angle)
    for z, h in ((0, 7), (89, 7)):
        s.disk(0, 0, z, 31, 24, h)
    glass.line([(-16, 66), (-9, 64), (0, 63), (9, 64), (16, 66)], BOLD)
    glass.line([(0, 47), (0, 28)], DETAIL, dashed=True)
    glass.line([(-27, 15), (-15, 17), (0, 24), (15, 17), (27, 15)], EDGE)
