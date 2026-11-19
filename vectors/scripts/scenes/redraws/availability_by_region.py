from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w4 import bezier_path, front_surface
from scenes.redraws.platform_footprint import folded_map

DESCRIPTION = "A raised location pin points to a highlighted district on a standing folded map."


def location_pin(s, tip, *, size=1):
    """Plant the point of a pierced map pin at a precise location."""
    x, y, z = tip
    face = front_surface(s, angle=-26, y=0, z=z)

    def place(u, v):
        dx, dy, height = face.at(u*size, v*size)
        return (x + dx, y + dy, height)

    shape = bezier_path(
        (0, 0), ((-4, 6), (-15, 17), (-15, 26)),
        ((-15, 46), (15, 46), (15, 26)), ((15, 17), (4, 6), (0, 0)),
    )
    hole = oval(0, 27, 5, 5, count=32)
    front = [place(*point) for point in shape[:-1]]
    back = [(a, b - 2.2, c) for a, b, c in front]
    for i in range(len(front)):
        s.face([back[i - 1], back[i], front[i], front[i - 1]], DETAIL)
    s.face(front, BOLD, openings=([place(*point) for point in hole[:-1]],))


def draw(s):
    west, middle, east = folded_map(s)
    west.line([(0, 21), (13, 22), (17, 29)])
    east.line([(61, 22), (74, 23), (84, 16), (93, 18)])
    west.line([(31, 37), (27, 49), (14, 52), (9, 40), (17, 29),
               (22, 18), (31, 16)], EDGE)
    middle.line([(31, 37), (44, 41), (54, 35), (57, 24), (50, 17), (31, 16)], EDGE)
    middle.line([(61, 22), (57, 24)])
    u, v = 49, 31
    x, y, z = middle.at(u, v)
    location_pin(s, (x, y + .3, z), size=1.18)
