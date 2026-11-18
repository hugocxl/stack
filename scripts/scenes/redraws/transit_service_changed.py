from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import rect
from scenes.redraws.bus_shelter_directory import bus_pictogram

DESCRIPTION = "A station timetable uses a hooked arrow to move one departure row to another."


def draw(s):
    s.box(30, -4, 0, 7, 9, 30, 1.5)
    s.box(24, -9, 0, 19, 19, 3.5, 2)
    s.box(3, -2, 14, 61, 8, 50, 3)
    face = lambda x, z: (x, 6, z)
    rect(s, face, 7, 18, 53, 41, 2, DETAIL)
    bus_pictogram(s, 18, 6, 50, .65)
    s.line([face(28, 49), face(53, 49)], DETAIL)
    for z, length in ((38, 21), (31, 16), (24, 21)):
        s.line([face(12, z), face(12 + length, z)], EDGE)
        s.line([face(39, z), face(47, z)], DETAIL)
    arrow(s, [face(49, 38), face(55, 38), face(55, 24)], BOLD, head=5)
