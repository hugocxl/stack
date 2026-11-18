from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A folded conference program has three session rows, each headed by an analog time."


def draw(s):
    front = Surface(s, (0, 22, 0), rise=(-.22, .97), back=(0, -.97, -.22))
    s.face([(0, -25, 0), (89, -25, 0), front.point(89, 97), front.point(0, 97)])
    s.face([(89, -25, 0), front.point(89, 0), front.point(89, 97)])
    front.plate(rounded(0, 0, 89, 97, 3), 3)
    front.rules(12, 83, [58], ink=EDGE)
    front.rules(12, 74, [36])
    for v, width, hour in ((57, 48, (-3.5, .5)), (37, 38, (3.5, 0)), (17, 45, (2.5, -2.5))):
        front.oval(18, v, 6.8, 6.8, EDGE)
        front.stroke([(18, v + 4.5), (18, v), (18 + hour[0], v + hour[1])], EDGE)
        front.rules(31, v + 3, [width], ink=EDGE)
        front.rules(31, v - 4, [width - 15])
        front.rules(11, v + 10, [68])
