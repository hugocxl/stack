from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, wrench_mark

DESCRIPTION = "A repair pickup locker shows one open compartment with a check badge attached to its swung-out door."


def draw(s):
    near, far = 25, -13
    w, h = 72, 80
    s.face([(0, far, h), (w, far, h), (w, near, h), (0, near, h)])
    s.face([(w, far, 0), (w, near, 0), (w, near, h), (w, far, h)])
    s.face([(38, near, 9), (64, near, 9), (64, near - 18, 9), (38, near - 18, 9)], DETAIL)
    s.face([(38, near - 18, 9), (64, near - 18, 9), (64, near - 18, 37),
            (38, near - 18, 37)], DETAIL)
    front = Surface(s, lambda u, v: (u, near, v))
    opening = [(38, 9), (64, 9), (64, 37), (38, 37)]
    s.face([front.at(u, v) for u, v in ((0, 0), (w, 0), (w, h), (0, h))],
           openings=[[front.at(u, v) for u, v in opening]])
    front.line([(0, 45), (72, 45)], EDGE)
    front.line([(33, 0), (33, 80)], DETAIL)
    front.line([(25, 19), (25, 28)], EDGE)
    front.line([(61, 57), (61, 66)], EDGE)
    wrench_mark(front, 17, 62, .37)
    door = Surface(s, lambda u, v: (64 + .98*u, near + .20*u, v))
    door.slab([(0, 9), (27, 9), (27, 37), (0, 37)], 3)
    door.line([(22, 18), (22, 26)], DETAIL)
    badge(s, "check", *door.at(28, 36), 14)
