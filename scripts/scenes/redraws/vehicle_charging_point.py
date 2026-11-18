from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import cable_sleeve, upright_profile

DESCRIPTION = "A charging cable plugs directly into the side of a three-quarter-view electric car."


def draw(s):
    tire_centers = (-23, 28)
    for x in tire_centers:
        cable_sleeve(s, x, -18, -13, 10, 10, 2.6)
    side = [(-43, 9), (-43, 20), (-38, 25), (-24, 28), (-14, 40), (12, 40),
            (31, 27), (43, 25), (48, 19), (47, 9)]
    for x in reversed(tire_centers):
        side += oval(x, 9, 11, 11, 0, 180, 24)
    side += [(-43, 9)]
    upright_profile(s, side[:-1], 17, 34)
    s.face([(-29, 17, 28), (-13, 17, 38), (11, 17, 38), (25, 17, 28)], EDGE)
    s.line([(1, 17, 38), (1, 17, 28)], DETAIL)
    s.line([(1, 17, 27), (1, 17, 13), (12, 17, 13)], DETAIL)
    s.line([(8, 17, 24), (14, 17, 24)], DETAIL)
    for x in tire_centers:
        cable_sleeve(s, x, 14, 18, 9, 9, 3)
    windshield = [(14, y, 38.6) for y in (-13, 13)]
    windshield += [(28, y, 29) for y in (13, -13)]
    s.face(windshield, EDGE)
    for y in (-13, 8):
        s.line([(46.6, y, 14), (46.6, y + 5, 14), (47.5, y + 5, 18),
                (47.5, y, 18), (46.6, y, 14)], EDGE)
    s.line([(47.2, -5, 11), (47.2, 5, 11)], DETAIL)
    s.tube([(-30, 27, 22), (-30, 36, 15), (-35, 43, 7), (-45, 44, 4),
            (-53, 37, 4), (-54, 29, 9), (-55, 27, 15)], 1.5, EDGE)
    s.box(-61, 15, 0, 12, 12, 30, 2)
    glyph(s, "bolt", -55, 27, 24, 3.6, EDGE)
    s.box(-35, 17, 18, 10, 12, 8, 2.2)
    s.line([(-34, 25, 21), (-27, 25, 21)], DETAIL)
