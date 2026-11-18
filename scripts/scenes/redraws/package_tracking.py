from geometry import BOLD, EDGE
from scenes.redraws._w1 import software_package

DESCRIPTION = "A taped parcel rests at a waypoint on a folded map marked with a bold route and two waypoints."


def draw(s):
    folds = [(-56, 24), (-28, 7), (34, 7), (58, 24)]
    for (a, za), (b, zb) in zip(folds, folds[1:]):
        s.face([(a, -33, za), (b, -33, zb), (b, 33, zb), (a, 33, za)], EDGE)
        s.face([(a, 33, za), (b, 33, zb), (b, 33, zb - 2), (a, 33, za - 2)], EDGE)

    def on_map(x, y):
        for (a, za), (b, zb) in zip(folds, folds[1:]):
            if a <= x <= b:
                return x, y, za + (x - a) * (zb - za) / (b - a)
        raise ValueError("Route point is outside the map")

    route = [(-49, 12), (-28, 13), (-15, -7), (9, -8), (34, 4), (48, -9)]
    s.line([on_map(x, y) for x, y in route], BOLD)
    for x, y in (route[0], route[-1]):
        s.disk(*on_map(x, y), 4, 4, 2, EDGE)
    software_package(s, 9, -8, 7, .58, show_code=False)
