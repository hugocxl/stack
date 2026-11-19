from geometry import EDGE, rounded
from scenes.redraws._w5 import charger, rect
from scenes.redraws.car_park_height_limit import car

DESCRIPTION = "A charging cable connects a compact EV pedestal to the side port of an electric car."


def draw(s):
    car(s)
    rect(s, lambda x, z: (x, 36, z), 34, 16, 8.5, 7.5, 1.6)
    s.face([(x, 38, z) for x, z in rounded(35.8, 17.4, 4.8, 4.6, 1)])
    socket = charger(s, -8, 42, .77, connected=True)
    s.tube([socket, (1, 57, 13), (4, 56, 6), (10, 53, 3), (19, 46, 3),
            (29, 42, 5), (36, 40, 10), (38, 39.5, 19.7), (38, 38, 19.7)], 1.05, EDGE)
