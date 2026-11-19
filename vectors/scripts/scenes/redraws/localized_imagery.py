from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A framed picture shows a torii gate and a map pin fitted to the frame."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.36, .93), back=(0, -.93, -.36),
                   across=(.94, -.34))
    x, y, _ = face.point(100, 0, 24)
    s.tube([face.point(88, 32, 7), (x, y, 1.5)], 2)
    face.plate(rounded(0, 0, 101, 72, 4), 9)
    face.rect(8, 9, 85, 54, 2, EDGE)
    face.stroke([(9, 17), (92, 17)])
    face.oval(19, 50, 4, 5)
    gate = [(30, 56), (39, 51), (63, 51), (73, 56), (70, 48),
            (63, 46), (39, 46), (33, 48)]
    face.stroke(gate, BOLD, closed=True)
    for x, step in ((38, 3), (63, -3)):
        face.stroke([(x + step, 46), (x + step * .7, 36)], EDGE)
        face.stroke([(x + step * .7 + 5, 36), (x + step + 5, 46)], EDGE)
        face.stroke([(x + step * .5, 31), (x, 17), (x + 5, 17),
                     (x + step * .5 + 5, 31)], EDGE)
    face.rect(31, 31, 44, 5, 0.7, EDGE)

    pin = Surface(s, face.point(91, 51, -2), across=face.across, back=face.back)
    outline = [(-7, 0), (-9, 5), (-8, 11), (-5, 15), (0, 17),
               (5, 15), (8, 11), (9, 5), (7, 0), (0, -9)]
    pin.plate(outline, 3)
    pin.oval(0, 8, 3.5, 4, EDGE)
