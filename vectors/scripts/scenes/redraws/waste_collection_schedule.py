from geometry import DETAIL, EDGE
from scenes.redraws._w1 import wheelie_bin
from scenes.systems_shapes import bezel

DESCRIPTION = "A desktop calendar marks its pickup date with a miniature wheeled waste bin."


def draw(s):
    s.face([(-43, -25, 0), (43, -25, 0), (43, -2, 69), (-43, -2, 69)], EDGE)
    s.box(-43, -4, 0, 86, 12, 69, 3)
    s.line([(-42, 8, 53), (42, 8, 53)], EDGE)
    for x in (-24, 0, 24):
        s.tube([(x, -6, 65), (x, -6, 72), (x, -3, 76), (x, 8, 76),
                (x, 12, 72), (x, 12, 63)], 1.8)
    for x in (-19, 0, 19):
        s.line([(x, 8, 7), (x, 8, 47)], DETAIL)
    for z in (7, 21, 34, 47):
        s.line([(-38, 8, z), (38, 8, z)], DETAIL)
    bezel(s, 19, 8, 6, 19, 16, EDGE, 1)
    wheelie_bin(s, 35, 14, 3, .52)
