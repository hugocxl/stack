from shapely.geometry import Polygon

from geometry import DETAIL, EDGE
from scenes.redraws._w4 import closed_book, landscape

DESCRIPTION = "A curling wrapper corner exposes part of a landscape on a hardback cover."


def draw(s):
    cover = closed_book(s, angle=-24)
    fold = [(25, 0), (76, 63)]
    revealed = Polygon([fold[0], (76, 0), fold[1]])
    landscape(cover, 30, 7, 39, 45, clip=revealed)
    cover.slab([(3, 0), *fold, (76, 99), (3, 99)], 1, DETAIL)

    curl = [cover.at(*fold[0])]
    for u, v, lift in ((17, 4, 5), (13, 10, 10), (15, 17, 14), (22, 24, 16),
                       (32, 31, 15), (47, 42, 11), (61, 53, 5)):
        x, y, z = cover.at(u, v)
        curl.append((x, y, z + lift))
    s.face([*curl, cover.at(*fold[1])], EDGE)
