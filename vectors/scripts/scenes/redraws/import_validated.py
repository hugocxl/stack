from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import inbox_base, inbox_front, panel, rect

DESCRIPTION = "A gridded document sits inside an import tray with a check badge on its corner."


def draw(s):
    inbox_base(s)
    face = lambda x, z: (x, 35 - .58*z, 4 + z)
    panel(s, [(8, 0), (54, 0), (54, 43), (44, 53), (8, 53)], face, 2.8)
    s.line([face(44, 53), face(44, 43), face(54, 43)], EDGE)
    rect(s, face, 14, 16, 33, 24, 1, EDGE)
    for z in (24, 32):
        s.line([face(14, z), face(47, z)], DETAIL)
    for x in (25, 36):
        s.line([face(x, 16), face(x, 40)], DETAIL)
    inbox_front(s)
    badge(s, "check", 57, 29, 39, 11.8)
