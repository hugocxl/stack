from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface, side_wheel, upright, wrench_mark

DESCRIPTION = "A maintenance van carries a wrench on its cargo door and a recurrence badge above its cab."


def draw(s):
    profile = [(-47, 15), (-47, 46), (-42, 55), (13, 55), (26, 51),
               (40, 32), (51, 28), (54, 22), (53, 12), (47, 12),
               (45, 20), (40, 25), (31, 25), (25, 20), (23, 12),
               (-18, 12), (-20, 20), (-26, 25), (-34, 25), (-40, 20),
               (-43, 12)]
    upright(s, profile, 20, 38)
    side_wheel(s, -31, 22, 11, 10)
    side_wheel(s, 35, 22, 11, 10)
    side = front_surface(s, angle=0, y=20)
    side.outline([(-41, 26), (-41, 49), (8, 49), (8, 18), (-15, 18),
                  (-20, 26)], DETAIL)
    side.outline([(15, 47), (24, 46), (36, 31), (15, 31)], EDGE)
    side.line([(15, 27), (20, 27)], DETAIL)
    side.line([(12, 21), (12, 47)], DETAIL)
    wrench_mark(side, -16, 37, .40, BOLD)
    s.line([(27, -14, 49), (39, -14, 34), (39, 15, 34), (27, 15, 49),
            (27, -14, 49)], EDGE)
    s.line([(53, -13, 20), (53, -4, 20)], EDGE)
    s.line([(53, 10, 20), (53, 17, 20)], EDGE)
    badge(s, "refresh", 34, -9, 63, 14)
