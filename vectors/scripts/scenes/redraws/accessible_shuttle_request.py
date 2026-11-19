from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import bus

DESCRIPTION = "A shuttle bus displays a wheelchair pictogram and carries a plus badge at its rear corner."


def draw(s):
    bus(s)
    # The chair has an open seat, a push handle, a drive wheel and a caster.
    face = lambda x, z: (x, 35, z)
    s.line([face(x, z) for x, z in oval(27, 16, 5.7, 5.7, 68, 382, 32)], EDGE)
    s.line([face(21, 24), face(24, 24), face(26, 18.5),
            face(34, 18.5), face(37, 12), face(40, 12)], EDGE)
    s.line([face(x, z) for x, z in oval(36, 12, 1.6, 1.6, count=18)], EDGE)
    badge(s, "plus", 2, 37, 43, 12)
