from geometry import DETAIL, EDGE, oval

DESCRIPTION = "A service coffee urn has a lidded stainless body, a coffee bean emblem, a dispensing tap, and a drip ledge."


def draw(s):
    s.box(6, 5, 0, 39, 49, 4, 4)
    s.box(8, 36, 4, 35, 15, 2, 2)
    for x in (14, 22, 30, 38):
        s.line([(x, 44, 6), (x, 49, 6)], DETAIL)
    s.box(13, 10, 4, 24, 25, 12, 2)
    s.tube([(5, 22, 39), (-3, 22, 39), (-5, 22, 41),
            (-5, 22, 48), (5, 22, 48)], 1.6)
    s.disk(25, 22, 15, 20, 18, 40)
    s.disk(25, 22, 54, 20.5, 18.5, 4)
    s.solid(oval(25, 22, 19, 17)[:-1], 58, 4, top=oval(25, 22, 13, 11)[:-1], crease=False)
    s.box(19, 19, 62, 12, 6, 4, 2)
    def emblem(u, v):
        return (42 - .32*u, 30 + .84*u, 41 + v)

    bean = [(-3.5, -5), (-4.6, -2), (-3.8, 2), (-1, 5), (2.5, 5),
            (4.5, 2), (4, -2), (1.5, -5)]
    s.face([emblem(u, v) for u, v in bean], EDGE)
    s.line([emblem(-2, -5), emblem(0, -2), emblem(-.2, 1), emblem(2, 5)], DETAIL)
    s.tube([(24, 38, 37), (24, 45, 37), (24, 48, 34), (24, 48, 27)], 2.1)
    s.tube([(24, 45, 37), (24, 45, 46), (19, 45, 46)], 1.35)
