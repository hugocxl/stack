from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w3 import Surface
from scenes.redraws.expired_member_access import member_emblem

DESCRIPTION = "A magnifying glass overlaps an upright profile card with a framed membership seal."


def draw(s):
    profile = Surface(s, (0, 0, 0), rise=(-.31, .95), back=(0, -.95, -.31))
    profile.plate(rounded(0, 0, 62, 91, 5), 7)
    profile.rect(9, 34, 44, 44, 3, EDGE)
    member_emblem(profile, 31, 56, 14)
    profile.rules(11, 24, [31], ink=EDGE)
    profile.rules(11, 14, [23])
    lens = Surface(s, (55, 8, 40))
    s.tube([lens.point(15, -12), lens.point(31, -31)], 3.7)
    lens.plate(oval(0, 0, 18, 20, count=44)[:-1], 4, BOLD)
    lens.oval(0, 0, 13.5, 15.5, DETAIL)
