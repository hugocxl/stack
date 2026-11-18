from geometry import DETAIL
from scenes.redraws._kit import _screen, _strokes, badge
from scenes.redraws._w5 import map_stroke, standing_map

DESCRIPTION = "An accordion-fold street map carries a slashed Wi-Fi badge."


def draw(s):
    standing_map(s)
    for street in ([(5, 15), (21, 15), (29, 23), (44, 23), (53, 17), (70, 17)],
                   [(6, 32), (24, 31), (35, 35), (50, 35), (68, 30)],
                   [(14, 5), (14, 15), (18, 24), (17, 38)],
                   [(31, 5), (34, 14), (33, 23), (39, 37)],
                   [(58, 5), (60, 18), (58, 30), (62, 38)]):
        map_stroke(s, street, DETAIL)

    x, y, z, r = 70, -8, 40, 15
    badge(s, "wifi", x, y, z, r)
    for stroke in _strokes("slash", r*.86):
        s.tube([_screen(x, y, z, u, v) for u, v in stroke], .85)
