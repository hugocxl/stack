from geometry import DETAIL, EDGE, oval

DESCRIPTION = "A moisture meter drives two probe tips into soil beside the exposed courses of a foundation wall."


def draw(s):
    s.box(0, 0, 0, 80, 50, 17, 2)
    # The brickwork remains visible above and behind the ground cut.
    s.box(1, 0, 16, 78, 20, 38, 1)
    for z in (27, 39):
        s.line([(1, 20, z), (79, 20, z)], DETAIL)
    for x, low, high in ((19, 16, 27), (56, 16, 27), (39, 27, 39), (25, 39, 54), (62, 39, 54)):
        s.line([(x, 20, low), (x, 20, high)], DETAIL)
    s.line([(5, 50, 7), (25, 50, 9), (44, 50, 6), (72, 50, 8)], DETAIL)

    for x in (46, 56):
        s.tube([(x, 35, 34), (x + 5, 38, 17)], 1.4, EDGE)
        s.ellipse(x + 5, 38, 17, 2.5, 2.5, DETAIL)
    s.box(39, 26, 29, 24, 13, 28, 4)
    droplet = [(52, 39, 51), (57, 39, 44)]
    droplet += [(x, 39, z) for x, z in oval(52, 43, 5, 5, 5, -185, 18)]
    s.line([*droplet, droplet[0]], EDGE)
