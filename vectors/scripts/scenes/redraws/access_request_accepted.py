from geometry import EDGE, oval, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import loop, rule, upright

DESCRIPTION = "An access request form shows a key over two fields and a check badge at the upper-right corner."


def draw(s):
    s.face(upright(rounded(0, 0, 76, 87, 3)))

    # The bow and the teeth form a single cut key silhouette.
    bow = oval(25, 62, 11, 11, 24, 336, 40)
    top, bottom = bow[0][1], bow[-1][1]
    shaft = [(42, bottom), (42, 54), (47, 54), (47, bottom),
             (51, bottom), (51, 52), (56, 52), (56, bottom),
             (59, bottom), (59, top)]
    s.face(upright([*bow, *shaft]),
           openings=[upright(oval(22, 62, 3.5, 3.5, count=32)[:-1])])

    for z, end in ((30, 52), (10, 44)):
        rule(s, 11, 25, z + 14, EDGE)
        loop(s, rounded(11, z, 53, 10, 2))
        rule(s, 17, end, z + 5)

    badge(s, "check", 77, 2, 78, 14)
