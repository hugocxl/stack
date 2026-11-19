from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import money_coin, printed_stroke

DESCRIPTION = "A curved return arrow points toward coins held in an open clasp purse."


def draw(s):
    rim = [(0, 30), (4, 36), (14, 40), (40, 40), (52, 36), (57, 30)]
    base = [(57, 23), (54, 12), (48, 6), (38, 2), (17, 2),
            (8, 6), (2, 13), (0, 21)]
    back = lambda x, z: (x, -6, z)
    front = lambda x, z: (x, 12, z - 4)
    back_bottom = [(57, 16), (0, 16)]
    s.face([back(x, z) for x, z in rim + back_bottom])
    money_coin(s, 25, 3, 35, 12)
    front_rim = [(0, 30), (9, 31), (22, 29), (37, 29), (51, 31), (57, 30)]
    s.face([back(57, 30), front(57, 30), front(57, 23),
            front(54, 12), back(57, 16)], EDGE)
    s.face([front(x, z) for x, z in front_rim + base])
    printed_stroke(s, front, [(2, 24), (13, 24), (27, 22), (42, 22), (55, 24)], DETAIL)
    for x in (27, 33):
        s.disk(x, 12, 26, 2.8, 2, 3, EDGE)
    arrow(s, [(67, 5, 49), (54, 5, 59), (43, 5, 64), (33, 5, 64),
              (27, 5, 61), (25, 5, 54)], BOLD, head=7)
