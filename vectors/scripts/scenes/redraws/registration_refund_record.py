from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import ticket

DESCRIPTION = "A perforated event ticket carries a two-coin emblem and a curved return-arrow badge."


def draw(s):
    face = ticket(s, marks=False)
    face.oval(35, 27, 12, 12, EDGE)
    face.stroke([(39, 31), (33, 32), (31, 30), (31, 28), (38, 26),
                 (39, 24), (37, 22), (31, 23)], EDGE)
    face.stroke([(35, 20), (35, 34)], DETAIL)
    face.stroke([(27, 18), (27, 14), (32, 10), (39, 10), (45, 14), (47, 19), (47, 27)], EDGE)
    face.rules(53, 33, [12, 9, 11])
    for x in (81, 86, 92, 97):
        face.stroke([(x, 27), (x, 39)], EDGE)
    badge(s, "refresh", 98, 0, 7, 13)
