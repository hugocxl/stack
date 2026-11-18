from geometry import DETAIL, EDGE

DESCRIPTION = "A ladder leans against a building facade with its upper rails seated at the sill of an elevated service hatch."


def draw(s):
    s.box(-43, -16, 0, 78, 16, 71, .7)
    s.box(-44, -17, 71, 80, 18, 3, .7)
    s.box(-9, 0, 47, 28, 2.5, 20, 1.5)
    s.box(-10, 0, 45, 30, 4, 2, .5)
    s.face([(-5, 2.5, 51), (15, 2.5, 51), (15, 2.5, 63), (-5, 2.5, 63)], DETAIL)
    s.line([(10, 2.5, 56), (13, 2.5, 56)], EDGE)
    for z in (13, 35):
        s.line([(-42, 0, z), (35, 0, z)], DETAIL)
    s.line([(-27, 0, 13), (-27, 0, 35)], DETAIL)
    s.line([(35, -13, 13), (35, 0, 13)], DETAIL)

    def lean(z):
        return 30 - .55 * z

    for z in (8, 16, 24, 32, 40):
        s.tube([(-6, lean(z), z), (16, lean(z), z)], 1.2, EDGE)
    for x in (-6, 16):
        s.tube([(x, lean(2), 2), (x, lean(47), 47)], 1.9, EDGE)
        s.box(x - 2.1, lean(2) - 2, 0, 4.2, 4, 3, .6)
