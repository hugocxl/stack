from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import printed_stroke

DESCRIPTION = "A measuring jug has two graduation scales with matching volume levels aligned across its front."


def draw(s):
    x, y = 25, 23
    s.tube([(45, 22, 44), (56, 22, 44), (61, 22, 38),
            (61, 22, 22), (54, 22, 16), (44, 22, 16)], 2.2)
    lower = oval(x, y, 17, 15)[:-1]
    upper = [(a, b) for a, b in oval(x, y, 22, 20, -153, 153, count=48)]
    upper.extend([(3, 32), (-7, 28), (-7, 24), (2, 16)])
    s.solid(lower, 0, 51, top=upper, crease=False)
    s.face([(a, b, 51) for a, b in upper],
           openings=[[(a, b, 51) for a, b in oval(x, y, 18, 16)[:-1]]])
    for z in (10, 19, 28, 37):
        f = z/51
        for a, b in ((12, 39 if z in (19, 37) else 31),
                     (60 if z in (19, 37) else 68, 92)):
            s.ellipse(x, y, z, 17+5*f, 15+5*f, EDGE, a, b)
        if z in (19, 37):
            s.ellipse(x, y, z, 17+5*f, 15+5*f, DETAIL, 43, 56)
    for z in (14.5, 23.5, 32.5):
        f = z/51
        s.ellipse(x, y, z, 17+5*f, 15+5*f, DETAIL, 13, 25)
    # A cup outline and a droplet distinguish the two units without lettering.
    u = lambda a, z: (32+a, 40-.25*a, z+.32*a)
    printed_stroke(s, u, [(-4, 44), (-3, 40), (2, 40), (3, 44), (-4, 44)], BOLD)
    printed_stroke(s, u, [(3, 43.5), (5, 43.5), (4, 41.5), (2.5, 41.5)], BOLD)
    printed_stroke(s, u, [(13, 45), (10, 41), (10, 39), (13, 38),
                          (15, 40), (15, 42), (13, 45)], BOLD)
