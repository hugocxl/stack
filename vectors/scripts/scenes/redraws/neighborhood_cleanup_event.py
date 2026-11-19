from geometry import DETAIL, EDGE
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "The jaws of a litter grabber grip a crumpled scrap of paper."


def draw(s):
    y = 2
    grip = [(-41, 56), (-38, 68), (-30, 75), (-19, 74), (-13, 68),
            (-18, 62), (-27, 64), (-34, 53)]
    upright_profile(s, grip, y, 4)
    s.tube([(-21, y - 2, 64), (31, y - 2, 26)], 2.3)
    s.line([(-29, y, 63), (-23, y, 55), (-16, y, 59)], EDGE)
    s.tube([(31, y, 26), (37, y, 29), (44, y, 25), (46, y, 18)], 1.85)
    paper = [(39, y + 1, 11), (41, y + 1, 19), (49, y + 1, 24),
             (55, y + 1, 19), (63, y + 1, 17), (58, y + 1, 10),
             (60, y + 1, 4), (49, y + 1, 3), (42, y + 1, 6)]
    s.face(paper, EDGE)
    s.line([(46, y + 1, 17), (48, y + 1, 10), (55, y + 1, 12),
            (60, y + 1, 15)], DETAIL)
    s.line([(48, y + 1, 10), (49, y + 1, 3)], DETAIL)
    s.tube([(31, y + 2, 25), (31, y + 2, 17), (35, y + 2, 11),
            (42, y + 2, 10)], 1.85)
