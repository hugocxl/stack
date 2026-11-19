from geometry import DETAIL, EDGE
from scenes.redraws._w1 import database, upright_profile

DESCRIPTION = "A database cylinder carries a divider with a stepped index tab and three ruled entries."


def draw(s):
    database(s, -6, -4, 30, pitch=11)
    outline = [(5, 0), (5, 40), (25, 40), (29, 47), (44, 47), (44, 0)]
    upright_profile(s, outline, 15, 5)
    for z, length in ((28, 24), (20, 21), (12, 16)):
        s.line([(12, 15, z), (12 + length, 15, z)], DETAIL)
    s.line([(31, 15, 42), (39, 15, 42)], EDGE)
