from geometry import DETAIL, EDGE
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A tabbed document folder protrudes through the open door of a civic pickup locker."


def draw(s):
    left, right, back, front = -31, 31, -18, 14
    s.box(left, back, 0, 62, 5, 70, 1.5)
    s.box(left, back, 0, 4, 32, 70, 1)
    s.box(27, back, 0, 4, 32, 70, 1)
    s.box(left, back, 66, 62, 32, 4, 1)
    s.box(left, back, 34, 62, 32, 4, 1)
    s.box(left, back, 0, 62, 32, 33, 1.5)
    s.line([(-7, front, 20), (7, front, 20)], DETAIL)
    points = [(-22, 38), (-22, 53), (-10, 53), (-6, 58),
              (13, 58), (13, 38)]
    upright_profile(s, points, 21, 3)
    s.line([(-17, 21, 45), (6, 21, 45)], DETAIL)
    door = [(right, front, 36), (right, front, 66), (46, 40, 66), (46, 40, 36)]
    s.face(door, EDGE)
    s.line([(44, 36, 47), (44, 36, 55)], DETAIL)
