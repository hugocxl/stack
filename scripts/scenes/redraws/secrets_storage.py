from geometry import BOLD, DETAIL, EDGE, oval, rounded

DESCRIPTION = "A safe has a closed inset door, two exposed hinges, and a prominent keyhole."


def draw(s):
    s.box(-39, -33, 0, 39, 66, 66, 4)
    door = rounded(-27, 7, 53, 52, 3)
    s.line([(0, -u, z) for u, z in door + door[:1]], EDGE)
    for z in (18, 45):
        s.box(-1, -30, z, 4, 7, 9, 1.5)
    s.line([(0, -u, z) for u, z in oval(-5, 34, 16, 16, count=40)], EDGE)
    head = oval(-5, 36, 5, 5, 240, -60, 30)
    keyhole = [*head, (-.8, 26), (-9.2, 26), head[0]]
    s.line([(0, -u, z) for u, z in keyhole], BOLD)
    s.line([(0, 20, 12), (0, -16, 12)], DETAIL)
