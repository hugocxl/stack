from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project

DESCRIPTION = "A beer keg stands upright with rolled chimes, handholds, and a central valve."


def draw(s):
    rings = ((0, 19), (5, 19), (13, 22), (18, 23), (38, 23),
             (44, 22), (49, 20), (54, 20))
    outline = MultiPoint([project((x, y, z)) for z, radius in rings
                          for x, y in oval(23, 22, radius, radius*.91)]).convex_hull
    s.layers.append((outline.boundary, outline, EDGE))
    s.ellipse(23, 22, 54, 20, 18.2, EDGE, -45, 135)
    s.ellipse(23, 22, 54, 17.6, 15.8, EDGE)
    s.ellipse(23, 22, 6, 19.3, 17.56, EDGE, -45, 135)
    s.ellipse(23, 22, 38, 23, 20.9, DETAIL, -45, 135)
    s.ellipse(23, 22, 18, 23, 20.9, DETAIL, -45, 135)
    s.disk(23, 22, 53.5, 6.2, 5.6, 3)
    s.ellipse(23, 22, 56.5, 3.1, 2.8, EDGE)
    for start, end in ((3, 40), (62, 97)):
        top = [(a, b, 50.9) for a, b in oval(23, 22, 20.2, 18.4, start, end, 18)]
        bottom = [(a, b, 46.6) for a, b in oval(23, 22, 20.7, 18.8, start, end, 18)]
        s.face(top + bottom[::-1])
