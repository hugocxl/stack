from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import currency_mark, printed_stroke

DESCRIPTION = "A prominent currency tag hangs from the closed shackle of a padlock threaded through its eyelet."


def draw(s):
    # The shackle crosses the tag plane once, inside the punched eyelet.
    face = lambda x, z: (x, 10 - .39 * z, z)
    outline = [(0, 3), (3, 0), (50, 0), (53, 3), (53, 47),
               (37, 67), (16, 67), (0, 47)]
    hole = oval(36, 55, 6.6, 5.2, count=28)
    s.tube([(36, -16, 56), (40, -16, 66), (50, -10, 74),
            (61, -4, 72), (68, 1, 65), (69, 5, 52)], 2.6)
    for a, b in zip(outline, outline[1:] + outline[:1]):
        if b[1] > a[1] or a[1] == b[1] == 67:
            p, q = face(*a), face(*b)
            s.face([p, q, (q[0], q[1] - 3, q[2]), (p[0], p[1] - 3, p[2])], DETAIL)
    s.face([face(x, z) for x, z in outline], EDGE,
           openings=[[face(x, z) for x, z in hole]])
    currency_mark(s, face, 21, 31, 13, ink=BOLD)
    printed_stroke(s, face, [(11, 12), (37, 12)], DETAIL)

    s.tube([(36, -15, 56), (39, -8, 54), (45, 1, 54), (48, 5, 52)], 2.6)
    s.box(44, -3, 30, 30, 16, 25, 3.4)
    key = lambda x, z: (x, 13, z)
    s.line([key(x, z) for x, z in oval(59, 45, 2.6, 2.6, count=24)], EDGE)
    s.line([key(59, 42.4), key(59, 38)], EDGE)
