from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import inbox_base, inbox_front, panel

DESCRIPTION = "A document sits in an import tray with a clock badge attached to its front-right corner."


def draw(s):
    inbox_base(s)
    def face(x, z):
        return x, 34 - .67*z, 4 + z

    panel(s, [(10, 0), (53, 0), (53, 34), (43, 44), (10, 44)], face, 2.7)
    s.line([face(43, 44), face(43, 34), face(53, 34)], EDGE)
    for z, end in ((29, 43), (22, 40), (15, 36)):
        s.line([face(17, z), face(end, z)], DETAIL)
    inbox_front(s)
    badge(s, "clock", 59, 39, 14, 13)
