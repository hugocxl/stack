from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._w4 import closed_book, upright

DESCRIPTION = "A megaphone with two sound rays rests against an interface preview on a release booklet."


def draw(s):
    cover = closed_book(s, angle=-24, width=74, height=88, depth=11)
    cover.rows(13, 17, (41,), ink=EDGE)
    cover.frame(13, 26, 47, 33, 3, EDGE)
    cover.line([(13, 35), (60, 35)], DETAIL)
    cover.rows(20, 44, (27, 20), step=7)
    cover.rows(13, 69, (35, 28), step=7)

    x, y, z = cover.at(56, 31)
    s.tube([(x - 7, y - 3, z + 11), (x - 5, y + 1, z - 5)], 3.9)
    rear = [(u, y - 4, v) for u, v in oval(x - 13, z + 17, 5.4, 5.4)]
    mouth_x, mouth_y, mouth_z = x + 32, y + 10, z + 24
    rim = oval(mouth_x, mouth_z, 13, 13)
    hull = MultiPoint([project(p) for p in rear + [(u, mouth_y, v) for u, v in rim]]).convex_hull
    s.layers.append((hull.boundary, hull, EDGE))
    upright(s, rim[:-1], mouth_y + 2, 2.5)
    s.line([(u, mouth_y + 2, v) for u, v in oval(mouth_x, mouth_z, 9.5, 9.5)], EDGE)
    s.line([(mouth_x + 13, mouth_y + 2, mouth_z + 13),
            (mouth_x + 21, mouth_y + 2, mouth_z + 20)], EDGE)
    s.line([(mouth_x + 17, mouth_y + 2, mouth_z + 4),
            (mouth_x + 28, mouth_y + 2, mouth_z + 7)], EDGE)
