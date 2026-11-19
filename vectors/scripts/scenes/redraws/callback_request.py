from geometry import BOLD, DETAIL, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import bezier_path, front_surface

DESCRIPTION = "A telephone handset has a curved callback arrow hooked around its receiver."


def draw(s):
    receiver = front_surface(s, angle=-13, z=35)
    outline = bezier_path(
        (-46, 1),
        ((-49, 7), (-46, 15), (-41, 21)),
        ((-29, 38), (-8, 43), (10, 41)),
        ((27, 39), (43, 29), (49, 14)),
        ((53, 7), (49, 2), (44, -1)),
        ((39, -5), (29, -7), (25, -3)),
        ((21, 0), (18, 9), (18, 13)),
        ((18, 17), (20, 19), (24, 21)),
        ((13, 30), (-11, 32), (-24, 22)),
        ((-20, 19), (-18, 16), (-19, 12)),
        ((-21, 6), (-23, -1), (-27, -4)),
        ((-31, -7), (-42, -4), (-46, 1)),
    )
    receiver.slab(outline[:-1], 11)
    receiver.line([(-43, 8), (-35, 5), (-27, 5)], DETAIL)
    receiver.line([(26, 5), (34, 6), (43, 10)], DETAIL)
    curve = oval(25, 19, 35, 42, -81, 92, count=33)
    arrow(s, [receiver.at(u, v) for u, v in curve] + [receiver.at(13, 61)], BOLD, head=10)
