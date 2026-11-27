from geometry import DETAIL, EDGE
from scenes.redraws._sf import lip, turned

DESCRIPTION = "A studio microphone with a ribbed capsule stands on a round desk base."


def draw(s):
    turned(s, [(26, 0), (26, 5), (20, 7)], steps=2)
    s.tube([(0, 0, 7), (0, 0, 34)], 2.6, EDGE)
    turned(s, [(4, 34), (7, 36), (15, 44), (17, 56), (17, 76), (14, 88), (8, 94), (.4, 96)], steps=4)
    for z in (52, 64, 76):
        lip(s, 0, 0, z, 16, DETAIL, -60, 150)

