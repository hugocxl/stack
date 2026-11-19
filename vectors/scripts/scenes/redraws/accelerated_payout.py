from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import upright_card

DESCRIPTION = "A banknote with a stepped border and oval medallion carries a forward-arrow badge and trails three speed lines."


def draw(s):
    upright_card(s, 84, 45, 2, 2.5)
    border = [(x, 0, z) for x, z in ((5, 11), (11, 11), (11, 5), (73, 5),
                                    (73, 11), (79, 11), (79, 34), (73, 34),
                                    (73, 40), (11, 40), (11, 34), (5, 34))]
    s.line(border + border[:1], DETAIL)
    s.line([(x, 0, z) for x, z in oval(42, 22.5, 13, 11)], EDGE)
    s.line([(x, 0, z) for x, z in oval(42, 22.5, 9.5, 7.5)], DETAIL)
    for x in (17, 67):
        for z in (19, 26):
            s.line([(x - 4, 0, z), (x + 4, 0, z)], DETAIL)

    for z, start in ((12, -15), (22, -22), (32, -13)):
        s.line([(start, 0, z), (-5, 0, z)], DETAIL)

    badge(s, "arrow", 81, 3, 45, 14)
