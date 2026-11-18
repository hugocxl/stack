from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import clipboard, plane_mark, rect

DESCRIPTION = "A travel clipboard displays a plane above three connected waypoints with calendar tabs and entry lines."


def draw(s):
    face = clipboard(s, w=58, h=76)
    plane_mark(s, face, 14, 59, .36)
    s.line([face(26, 59), face(47, 59)], DETAIL)
    s.line([face(17, 14), face(17, 46)], BOLD)
    for z in (14, 30, 46):
        s.face([face(a, b) for a, b in oval(17, z, 3.15, 3.15, count=22)[:-1]], EDGE)
        rect(s, face, 26, z - 4, 10, 8, 1.1)
        s.line([face(26, z + 1), face(36, z + 1)], DETAIL)
        s.line([face(39, z + 2), face(48, z + 2)], DETAIL)
        s.line([face(39, z - 2), face(46, z - 2)], DETAIL)
