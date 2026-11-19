from geometry import BOLD, DETAIL, EDGE
from scenes.systems_shapes import rectangle

DESCRIPTION = "An open laptop displays a terminal window with a command prompt."


def draw(s):
    s.box(-43, -25, 0, 86, 61, 4, 4)
    for y in (-8, -2, 4):
        s.line([(-32, y, 4), (32, y, 4)], DETAIL)
    rectangle(s, -11, 13, 4, 22, 14, DETAIL, 1.5)

    # Tilt the display back from the hinge while keeping its terminal on the glass.
    def display(points, depth=0):
        return [(x, -19 - .24 * z + depth, 4 + z) for x, z in points]

    outline = [(-43, 0), (43, 0), (43, 49), (-43, 49)]
    s.face(display(outline, -4), EDGE)
    s.face(display([(-43, 49), (43, 49)]) + display([(43, 49), (-43, 49)], -4), EDGE)
    s.face(display([(43, 0), (43, 49)]) + display([(43, 49), (43, 0)], -4), EDGE)
    s.face(display(outline), EDGE)
    s.line(display([(-37, 6), (37, 6), (37, 43), (-37, 43), (-37, 6)]), EDGE)
    s.line(display([(-37, 35), (37, 35)]), DETAIL)
    for x in (-31, -26):
        s.line(display([(x, 39), (x + 1.2, 39)]), EDGE)
    s.line(display([(-27, 29), (-15, 22), (-27, 15)]), BOLD)
    s.line(display([(-9, 15), (5, 15)]), BOLD)
