from geometry import DETAIL, EDGE
from scenes.redraws._w2 import chart_line, rule, upright_face

DESCRIPTION = "A clipped packet of closing papers shows a house outline above two signature lines."


def house_emblem(s, point, x, z, size, ink=EDGE):
    """Print a gable, walls and doorway on a document surface."""
    def stroke(vertices):
        s.line([point(x + u*size, z + v*size) for u, v in vertices], ink)

    stroke([(-1, .05), (0, .92), (1, .05)])
    stroke([(-.77, .25), (-.77, -.72), (.77, -.72), (.77, .25)])
    stroke([(-.19, -.72), (-.19, -.15), (.19, -.15), (.19, -.72)])


def signature(s, point, x, z, width):
    rule(s, point, x, z, width)
    chart_line(s, point, [(x + width*u, z + width*v) for u, v in
                          ((.07, .04), (.22, .18), (.27, .16), (.20, .03),
                           (.33, .09), (.42, .055), (.68, .10))], EDGE)


def draw(s):
    def point(x, z):
        return x, -.36*z, .84*z

    for dx, dy, dz in ((8, -7, 7), (4, -3.5, 3.5), (0, 0, 0)):
        def sheet(x, z):
            a, b, c = point(x, z)
            return a + dx, b + dy, c + dz

        upright_face(s, sheet, [(0, 0), (76, 0), (76, 86), (0, 86)], 2.6)

    house_emblem(s, point, 37, 60, 19)
    signature(s, point, 12, 24, 49)
    signature(s, point, 12, 11, 41)
    clip = [(8, 76), (-2, 91), (3, 96), (15, 84)]
    s.tube([point(x, z) for x, z in clip], 1.35, DETAIL)
