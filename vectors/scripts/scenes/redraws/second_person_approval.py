from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import avatar_mark, clipboard, rect

DESCRIPTION = "An approval clipboard shows two signer portraits with a check badge at the second signature line."


def draw(s):
    face = clipboard(s, 62, 68)
    for z, scale in ((40, .69), (19, .83)):
        rect(s, face, 10, z - 7, 15, 15, 2.5, DETAIL)
        avatar_mark(s, face, 17.5, z, scale)
        s.line([face(30, z - 4), face(48, z - 4)], DETAIL)
    for stroke in ([(31, 38), (35, 43), (36, 42), (35, 38), (40, 41), (43, 39)],
                   [(30, 17), (33, 22), (36, 21), (34, 17), (38, 19), (42, 17)]):
        s.line([face(x, z) for x, z in stroke], EDGE)
    badge(s, "check", *face(56, 17), 11)
