from geometry import DETAIL, EDGE
from scenes.redraws._w1 import software_package, upright_profile

DESCRIPTION = "A small code package rests inside an upright project folder with a raised tab."


def draw(s):
    back = [(-38, 0), (-38, 44), (-33, 50), (-15, 50),
            (-10, 44), (38, 44), (38, 0)]
    upright_profile(s, back, -11, 4)
    s.box(-38, -12, 0, 76, 32, 4, 2)
    s.face([(38, -11, 0), (38, -11, 42), (38, 19, 11), (38, 19, 0)], DETAIL)
    software_package(s, 6, -2, 4, .72)
    front = [(-38, 0), (-38, 11), (-34, 15), (34, 15), (38, 11), (38, 0)]
    upright_profile(s, front, 20, 4, EDGE)
    s.line([(-28, 20, 9), (-13, 20, 9)], DETAIL)
