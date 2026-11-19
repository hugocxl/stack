from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import laptop
from scenes.redraws._w5 import rect

DESCRIPTION = "An open laptop displays a workspace with a sidebar and a check badge on the window's title bar."


def draw(s):
    face = laptop(s, 83, 57)
    s.line([face(5, 51), face(78, 51)], EDGE)
    s.line([face(29, 9), face(29, 51)], EDGE)
    for z, end in ((41, 23), (34, 20), (27, 22)):
        s.line([face(10, z), face(end, z)], DETAIL)
    rect(s, face, 36, 29, 31, 14, 1.8, EDGE)
    for z, end in ((23, 63), (17, 58)):
        s.line([face(37, z), face(end, z)], DETAIL)
    badge(s, "check", *face(76, 54), 12.8)
