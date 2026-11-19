from geometry import DETAIL, EDGE

DESCRIPTION = "A sofa and a low coffee table sit together inside a living room floor plan with a wide entry."


def draw(s):
    s.box(-43, -29, 0, 86, 58, 5, 1)
    s.box(-43, -29, 5, 86, 3.5, 11, .6)
    s.box(-43, -25.5, 5, 3.5, 54.5, 11, .6)

    s.box(-31, -19, 5, 56, 24, 6, 3)
    s.box(-31, -19, 10, 56, 7, 16, 2.4)
    for x in (-25, -3):
        s.box(x, -12, 10, 21, 15, 4, 2)
    for x in (-31, 19):
        s.box(x, -16, 10, 6, 21, 9, 2.5)
    for x in (-12, 10):
        s.box(x, 14, 5, 3, 9, 4, .8, DETAIL)
    s.box(-18, 11, 9, 37, 14, 4, 5, EDGE)
    s.box(39.5, -25.5, 5, 3.5, 20, 8, .5)
    s.box(39.5, 19, 5, 3.5, 10, 8, .5)
    s.box(-39.5, 26, 5, 79, 3, 6, .5)
