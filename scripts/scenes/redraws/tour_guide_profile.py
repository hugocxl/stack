from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w5 import mountain_mark, panel, rect

DESCRIPTION = "A guide credential hanging from a lanyard shows a mountain trail in its header and profile lines below."


def draw(s):
    face = lambda x, z: (x, -z*.21, z)
    s.tube([(22, -10, 57), (12, -12, 75), (13, -12, 82),
            (22, -12, 86), (34, -12, 85), (40, -12, 78),
            (34, -12, 66), (26, -10, 57)], 2)
    panel(s, rounded(0, 0, 51, 63, 4), face, 3)
    rect(s, face, 18, 54, 15, 4.5, 2)
    s.tube([(25, -12, 65), (25, -10.8, 60), (25, -10.8, 56)], .95)
    s.line([face(2, 29), face(49, 29)], DETAIL)
    mountain_mark(s, face, 25, 41, 1.03, BOLD)
    s.line([face(28, 31.5), face(34, 37), face(29, 41), face(32, 45)], DETAIL)
    s.line([face(x, z) for x, z in oval(12, 15, 4.7, 4.7, count=26)], EDGE)
    s.line([face(10, 13), face(14, 18)], EDGE)
    for z, width in ((10, 17), (16, 20), (22, 14)):
        s.line([face(21, z), face(21 + width, z)], DETAIL)
