from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line, open_volume, rule
from scenes.redraws.homebuyer_closing_packet import house_emblem, signature

DESCRIPTION = "An open guest register pairs a house pictogram with a ruled list for visitor signatures."


def draw(s):
    left, right = open_volume(s)
    house_emblem(s, left, 26, 41, 16)
    rule(s, left, 15, 21, 23, DETAIL)
    for z in (54, 40, 26, 12):
        rule(s, right, 5, z, 45, EDGE)
    chart_line(s, right, [(19, 12), (19, 54)], DETAIL)
    signature(s, right, 23, 40, 22)
