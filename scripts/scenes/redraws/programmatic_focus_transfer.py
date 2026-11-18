from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "An arrow carries the focus outline from one field to the next on a sloped form panel."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.38, .92), back=(0, -.92, -.38))
    face.plate(rounded(0, 0, 96, 72, 5), 12)
    face.rules(12, 60, [27], ink=EDGE)
    face.rect(13, 38, 54, 13, 2, EDGE)
    face.rect(13, 13, 54, 13, 2, EDGE)
    face.rules(19, 44, [26])
    face.rules(19, 19, [19])
    face.stroke(rounded(10, 35, 60, 19, 3), DETAIL, closed=True, dashed=True)
    face.rect(10, 10, 60, 19, 3, BOLD)
    route = [(71, 45), (80, 45), (84, 41), (84, 24), (80, 19), (72, 19)]
    arrow(s, [face.point(x, v) for x, v in route], BOLD, head=5)
