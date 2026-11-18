from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import basket_apple, location_pin

DESCRIPTION = "A handled harvest basket filled with produce carries a map-pin tag on its front."


def draw(s):
    s.tube([(12, 22, 21), (13, 14, 35), (21, 10, 48),
            (32, 9, 51), (44, 12, 47), (52, 18, 35), (54, 22, 21)], 2.2)
    top = oval(33, 24, 31, 21)[:-1]
    base = oval(33, 24, 24, 15)[:-1]
    s.solid(base, 0, 24, top=top, crease=False)
    s.ellipse(33, 24, 24, 29, 19, EDGE)
    for x, y, z, size in ((18, 19, 29, 8.5), (30, 16, 33, 10),
                          (44, 21, 31, 9), (28, 30, 27, 8)):
        basket_apple(s, x, y, z, size)
    front = [(x, y, 24) for x, y in oval(33, 24, 31, 21, 0, 140, 28)]
    hem = [(33+(x-33)*.98, 24+(y-24)*.98, 21) for x, y, _ in reversed(front)]
    s.face(front + hem)
    for z in (6, 13):
        k = z/24
        s.ellipse(33, 24, z, 24+7*k, 15+6*k, DETAIL, 0, 140)
    location_pin(s, lambda x, z: (x, 45, z), 41, 16, 8.1)
