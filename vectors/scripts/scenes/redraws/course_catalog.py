from geometry import DETAIL, EDGE
from scenes.redraws._w3 import book, cover_cap

DESCRIPTION = "A closed course catalog has a graduation cap above three subject rows on its cover."


def draw(s):
    cover = book(s, 81, 94, 16)
    cover_cap(cover, 27, 76, 24)
    cover.rules(47, 80, [24, 16], ink=EDGE)

    for v, width in ((51, 34), (33, 28), (15, 32)):
        cover.stroke([(16, v + 10), (73, v + 10)], DETAIL)
        cover.stroke([(17, v - 4), (23, v - 5), (29, v - 4),
                      (29, v + 5), (23, v + 4), (17, v + 5)], EDGE, closed=True)
        cover.stroke([(23, v - 5), (23, v + 4)])
        cover.rules(37, v + 2, [width, 13], gap=5)
