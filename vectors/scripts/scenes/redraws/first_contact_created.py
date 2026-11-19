from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w1 import portrait_mark, upright_profile

DESCRIPTION = "A ring-bound address book displays a contact card with a portrait, a name line and a plus badge."


def draw(s):
    s.box(-33, -8, 0, 66, 8, 48, 2)
    tabs = [(-30, 3), (-30, 51), (28, 51), (28, 36), (35, 36),
            (35, 25), (28, 25), (28, 17), (35, 17), (35, 7), (28, 7), (28, 3)]
    upright_profile(s, tabs, 2, 2)
    for z in (12, 25, 38):
        ring = [(x, y, z) for x, y in oval(-31, 0, 5.5, 4.7, -105, 56, 20)]
        s.tube(ring, 1.15)
    portrait_mark(s, -8, 2, 26, 11.5)
    s.line([(8, 2, 31), (23, 2, 31)], EDGE)
    s.line([(8, 2, 22), (19, 2, 22)], DETAIL)
    badge(s, "plus", 28, 2, 49, 11)
