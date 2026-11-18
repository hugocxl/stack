from geometry import BOLD, EDGE, rounded
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import Surface

DESCRIPTION = "A pointer drags a lifted content tile toward a dashed insertion outline in a browser window."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.42, .91), back=(0, -.91, -.42),
                   across=(.94, -.34))
    face.plate(rounded(0, 0, 113, 79, 5), 9)
    face.stroke([(0, 65), (113, 65)], EDGE)
    for x in (9, 15, 21):
        face.oval(x, 72, 1.2, 1.2)
    face.stroke(rounded(72, 12, 29, 26, 3), EDGE, closed=True, dashed=True)
    path = [(52, 46), (62, 46), (71, 43), (78, 39), (83, 33)]
    arrow(s, [face.point(*p) for p in path], head=7)
    tile = Surface(s, face.point(17, 27, -6), rise=face.rise, back=face.back,
                   across=face.across)
    tile.plate(rounded(0, 0, 35, 29, 4), 4, EDGE)
    tile.rules(7, 19, [21, 15], gap=7)
    place = tile.viewer_axes(30, 13)
    outline = [(0, 0), (0, 27), (19, 8), (11, 9), (16, -1), (12, -3), (7, 7)]
    s.face([tile.point(*place(x, v), -3) for x, v in outline], BOLD)
