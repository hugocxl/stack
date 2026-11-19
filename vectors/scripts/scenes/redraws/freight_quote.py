from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w1 import file_card

DESCRIPTION = "A freight quote sheet shows a corrugated shipping container beside a currency-marked price line."


def draw(s):
    file_card(s, -38, 0, 76, 62, 4)
    for z, width in ((51, 35), (44, 25)):
        s.line([(-29, 0, z), (-29 + width, 0, z)], DETAIL)

    def stroke(points, ink=EDGE):
        s.line([(x, 0, z) for x, z in points], ink)

    # A ribbed side and offset end doors distinguish an intermodal container.
    stroke([(-31, 16), (-31, 33), (-6, 33), (-6, 16), (-31, 16)])
    stroke([(-31, 33), (-23, 39), (2, 39), (2, 22), (-6, 16)])
    stroke([(-6, 33), (2, 39)])
    stroke([(-2, 36), (-2, 19)], DETAIL)
    for x in (-27, -22, -17, -12):
        stroke([(x, 20), (x, 29)], DETAIL)

    stroke([(18, 33), (13, 33), (11, 31), (13, 28), (16, 27),
            (18, 24), (16, 22), (11, 22)], EDGE)
    stroke([(14.5, 20), (14.5, 35)])
    stroke([(22, 26), (32, 26)], BOLD)
    stroke([(10, 17), (32, 17)], DETAIL)
    stroke([(-30, 10), (30, 10)], DETAIL)
