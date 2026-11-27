from geometry import DETAIL, EDGE

DESCRIPTION = "One intake pipe branches through a manifold into three server units below."


def unit(s, x):
    s.box(x, 0, 0, 30, 30, 20, 4)
    for z in (7, 13):
        s.line([(x + 5, 30, z), (x + 19, 30, z)], DETAIL)


def draw(s):
    xs = (-55, -15, 25)
    for x in xs:
        unit(s, x)
    for x in xs:
        s.tube([(x + 15, 15, 20), (x + 15, 15, 46)], 2.4, EDGE)
    s.tube([(-40, 15, 46), (40, 15, 46)], 3.2, EDGE)
    s.tube([(0, 15, 46), (0, 15, 76)], 3.2, EDGE)
    s.disk(0, 15, 74, 6, 6, 4)
