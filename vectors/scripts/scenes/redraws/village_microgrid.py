from geometry import EDGE
from scenes.redraws._w1 import solar_stand, turbine

DESCRIPTION = "A single local power cable connects a village house, a solar panel, and a wind turbine."


def draw(s):
    s.tube([(-38, -23, 1), (-38, 24, 1), (-30, 32, 1), (52, 32, 1),
            (63, 21, 1), (63, -8, 1), (56, -17, 1)], 1.3, EDGE)
    turbine(s, 56, -11, 0, 40)
    s.box(-51, -49, 0, 32, 26, 22, 1.1)
    s.face([(-53, -36, 36), (-17, -36, 36), (-17, -21, 22), (-53, -21, 22)], EDGE)
    s.face([(-17, -51, 22), (-17, -21, 22), (-17, -36, 36)], EDGE)
    s.line([(-45, -23, 0), (-45, -23, 12), (-35, -23, 12), (-35, -23, 0)], EDGE)
    solar_stand(s, 0, 32, .64)
