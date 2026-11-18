from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A courier delivery van carries a check badge on its cargo panel."


def draw(s):
    for x in (-26, 30):
        for y in (-17, 17):
            s.face([(a, y, b) for a, b in oval(x, 9, 9, 9, count=32)[:-1]], EDGE)
            s.line([(a, y, b) for a, b in oval(x, 9, 3.5, 3.5, count=24)], DETAIL)

    profile = [(-45, 12), (-45, 47), (-42, 51), (12, 51), (27, 45),
               (42, 30), (48, 27), (48, 12), (40, 12), (37, 18), (24, 18),
               (20, 12), (-16, 12), (-20, 18), (-32, 18), (-36, 12)]
    upright_profile(s, profile, 19, 38)
    s.face([(27, y, 45) for y in (-19, 19)] + [(42, 19, 30), (42, -19, 30)], EDGE)
    s.line([(30, y, 42) for y in (-15, 15)] + [(39, 15, 33), (39, -15, 33), (30, -15, 42)], DETAIL)
    s.line([(x, 19, z) for x, z in ((16, 43), (25, 41), (35, 31), (16, 31), (16, 43))], EDGE)
    s.line([(13, 19, 46), (13, 19, 19), (39, 19, 19)], DETAIL)
    s.line([(17, 19, 26), (23, 19, 26)], DETAIL)
    for y in (-15, 9):
        s.line([(48, y, 21), (48, y + 6, 21)], DETAIL)
    badge(s, "check", -14, 20, 42, 12)
