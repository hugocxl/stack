from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "A two-row language selector uses a bent arrow to return from a primary script to its fallback row."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.31, .95), back=(0, -.95, -.31),
                   across=(.96, -.28))
    face.plate(rounded(0, 0, 104, 74, 5), 12)
    for v in (42, 12):
        face.rect(9, v, 67, 21, 4, EDGE)
        face.rules(41, v + 13, [22, 15], gap=5)
    face.stroke([(17, 57), (31, 57)], EDGE)
    face.stroke([(23, 60), (22, 51), (24, 46)], EDGE)
    face.stroke([(30, 55), (26, 49), (21, 47), (17, 50), (20, 53),
                 (28, 53), (32, 50), (29, 46)], EDGE)
    face.stroke([(17, 17), (24, 29), (31, 17)], EDGE)
    face.rules(20, 22, [8], ink=EDGE)
    place = face.viewer_axes(78, 39)
    path = [(0, 13), (8, 13), (13, 11), (16, 7), (17, 2), (17, -5),
            (16, -10), (12, -14), (7, -15), (-7, -15)]
    arrow(s, [face.point(*place(x, v)) for x, v in path], ink=BOLD, head=8)
