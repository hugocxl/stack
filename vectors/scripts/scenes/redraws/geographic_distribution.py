from math import cos, radians, sin

from geometry import BOLD, DETAIL, EDGE, oval

DESCRIPTION = "A globe marks three service regions on North America, South America, and Europe."


# Simplified coastlines, sampled in longitude and latitude.
NORTH_AMERICA = (
    (-131, 55), (-124, 48), (-124, 40), (-114, 31), (-107, 23),
    (-100, 20), (-95, 17), (-87, 16), (-82, 9), (-78, 9), (-84, 15),
    (-86, 22), (-91, 20), (-96, 24), (-94, 29), (-86, 30), (-81, 25),
    (-79, 27), (-81, 33), (-75, 36), (-69, 44), (-62, 47), (-58, 52),
    (-65, 59), (-72, 62), (-76, 56), (-84, 57), (-88, 62), (-89, 67),
    (-99, 71), (-118, 70), (-130, 72),
)
SOUTH_AMERICA = (
    (-79, 9), (-73, 12), (-64, 9), (-60, 8), (-51, 3), (-49, -1),
    (-43, -3), (-35, -6), (-39, -15), (-44, -23), (-51, -28),
    (-54, -35), (-62, -42), (-66, -53), (-72, -55), (-74, -45),
    (-74, -32), (-71, -22), (-77, -14), (-81, -5), (-79, 9),
)
GREENLAND = (
    (-63, 60), (-50, 60), (-43, 67), (-29, 72), (-19, 76), (-23, 82),
    (-44, 83), (-65, 80), (-67, 72), (-60, 67), (-63, 60),
)
EURAFRICA = (
    (56, 70), (36, 70), (28, 72), (15, 69), (8, 63), (7, 58),
    (13, 55), (7, 54), (4, 51), (-4, 48), (-2, 43), (-9, 43),
    (-9, 37), (2, 36), (8, 43), (14, 39), (17, 38), (15, 44),
    (21, 39), (27, 36), (34, 36), (36, 31), (43, 13), (51, 12),
    (45, 5), (41, -2), (40, -11), (34, -18), (32, -25), (26, -34),
    (18, -35), (15, -28), (11, -17), (12, -7), (8, 3), (2, 5),
    (-7, 4), (-15, 10), (-17, 15), (-16, 21), (-11, 28), (-9, 32),
    (-5, 36), (4, 37), (11, 34), (15, 32), (23, 32), (31, 31),
)
BRITAIN = ((-5, 50), (1, 51), (0, 54), (-3, 56), (-3, 59), (-6, 57), (-5, 54), (-5, 50))


def draw(s):
    radius = 49
    tilt = radians(10)

    def screen(u, v):
        return u * .57735 - v * .3849, -u * .57735 - v * .3849, v * .7698

    def project_map(lon, lat):
        lon, lat = radians(lon + 35), radians(lat)
        return (cos(lat) * sin(lon),
                cos(tilt) * sin(lat) - sin(tilt) * cos(lat) * cos(lon),
                sin(tilt) * sin(lat) + cos(tilt) * cos(lat) * cos(lon))

    def map_line(positions, ink):
        visible = []
        for a, b in zip(positions, positions[1:]):
            u, v, depth = project_map(*a)
            next_u, next_v, next_depth = project_map(*b)
            if depth >= 0:
                visible.append(screen(radius * u, radius * v))
            if (depth >= 0) != (next_depth >= 0):
                mix = depth / (depth - next_depth)
                edge = screen(radius * (u + mix * (next_u - u)), radius * (v + mix * (next_v - v)))
                visible.append(edge)
                if depth >= 0:
                    s.line(visible, ink)
                    visible = []
        u, v, depth = project_map(*positions[-1])
        if depth >= 0:
            visible.append(screen(radius * u, radius * v))
        s.line(visible, ink)

    s.line([screen(u, v) for u, v in oval(0, 0, radius, radius)], EDGE)
    for outline in (NORTH_AMERICA, SOUTH_AMERICA, GREENLAND, EURAFRICA, BRITAIN):
        map_line(outline, DETAIL)
    for lon, lat in ((-91, 37), (-54, -12), (18, 49)):
        u, v, _ = project_map(lon, lat)
        s.face([screen(a, b) for a, b in oval(radius * u, radius * v, 4.5, 4.5, count=28)[:-1]], BOLD)
