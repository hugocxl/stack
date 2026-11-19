from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "An unrolled canvas tool wrap holds a screwdriver and open-jawed pliers in two stitched pockets."


def draw(s):
    roll = Surface(s, (0, 51, 4), rise=(-.62, .78), back=(0, -.78, -.62))
    roll.plate(rounded(0, 0, 96, 76, 9), 3)
    roll.stroke([(7, 7), (7, 67), (84, 67), (84, 7)], DETAIL, dashed=True)
    s.tube([roll.point(88, 6), roll.point(88, 68)], 5)

    roll.plate(rounded(21, 24, 14, 35, 5), 3, EDGE)
    s.tube([roll.point(28, 58), roll.point(28, 80)], 2.3)
    roll.stroke([(26, 77), (30, 77)], EDGE)

    pliers = [(49, 22), (50, 34), (54, 46), (53, 54), (46, 66), (47, 78),
              (50, 80), (58, 66), (63, 70), (68, 83), (71, 80), (71, 69),
              (63, 55), (63, 49), (72, 34), (73, 22), (66, 22), (57, 41),
              (54, 22)]
    roll.plate(pliers, 3)
    roll.oval(58, 53, 3, 3, EDGE)
    pocket = Surface(s, (-.4, 55, 6), rise=roll.rise, back=roll.back)
    pocket.plate([(8, 5), (82, 5), (82, 30), (46, 33), (8, 29)], 2)
    pocket.stroke([(46, 8), (46, 31)], EDGE)
    pocket.stroke([(12, 26), (46, 29), (78, 26)], DETAIL, dashed=True)
