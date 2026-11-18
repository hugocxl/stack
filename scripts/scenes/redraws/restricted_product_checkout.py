from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import warning
from scenes.redraws._w1 import software_package

DESCRIPTION = "A shopping cart holds one parcel and carries an exclamation triangle on its basket."


def draw(s):
    base = [(11, 5, 12), (82, 5, 12), (82, 53, 12), (11, 53, 12)]
    rim = [(-2, -3, 55), (94, -3, 55), (94, 64, 55), (-2, 64, 55)]

    def between(a, b, fraction):
        return tuple(u + (v - u) * fraction for u, v in zip(a, b))

    def wall(i, j):
        for height in (.33, .66):
            s.line([between(base[i], rim[i], height),
                    between(base[j], rim[j], height)], DETAIL)
        for along in (.28, .57, .78):
            s.line([between(base[i], base[j], along),
                    between(rim[i], rim[j], along)], DETAIL)
        s.line([base[j], rim[j]], EDGE)
        s.line([rim[i], rim[j]], EDGE)

    for x, y in ((17, 11), (76, 11), (17, 57), (76, 57)):
        s.face([(a, y, b) for a, b in oval(x, 6.8, 6, 6, count=24)[:-1]], EDGE)
    s.box(11, 5, 10, 71, 48, 2, 2)
    wall(0, 1)
    wall(3, 0)
    software_package(s, 54, 24, 12, 1.02, show_code=False)
    wall(1, 2)
    wall(2, 3)
    s.line([rim[2], (111, 64, 72), (111, -3, 72), rim[1]], EDGE)
    s.box(108, 12, 69, 6, 37, 6, 2)
    warning(s, 6, 67, 48, 35)
