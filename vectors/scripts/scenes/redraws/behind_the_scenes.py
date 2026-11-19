from geometry import DETAIL, EDGE, oval
from scenes.redraws._w4 import Surface, upright

DESCRIPTION = "A film camera opens on a side hinge to reveal the reel inside its housing."


def draw(s):
    s.box(0, 0, 0, 65, 31, 47, 5)
    s.box(40, 6, 47, 16, 15, 5, 2, ink=DETAIL)
    upright(s, oval(-15, 28, 14, 14)[:-1], 73, 9, angle=-90)
    upright(s, oval(-15, 28, 16, 16)[:-1], 84, 12, angle=-90)
    s.line([(84, -u, v) for u, v in oval(-15, 28, 10, 10)], EDGE)
    s.line([(84, -u, v) for u, v in oval(-15, 28, 6.5, 6.5)], DETAIL)
    chamber = Surface(s, lambda u, v: (u, 31, v))
    chamber.frame(6, 5, 48, 37, 3, EDGE)
    upright(s, oval(28, 23.5, 16, 16)[:-1], 33, 3)
    reel = Surface(s, lambda u, v: (u, 33, v))
    reel.oval(28, 23.5, 3, 3, EDGE)
    for u, v in ((28, 33), (37.5, 23.5), (28, 14), (18.5, 23.5)):
        reel.oval(u, v, 3.6, 3.6, EDGE)
    chamber.line([(48, 12), (48, 34)], DETAIL)

    door = Surface(s, lambda u, v: (6 - u*.71, 32 + u*.70, v + 5))
    door.slab([(0, 0), (34, 0), (37, 3), (37, 34), (34, 37),
               (0, 37)], 3)
    door.line([(6, 5), (32, 5), (32, 32), (6, 32)], DETAIL)
    s.tube([(6, 32, 8), (6, 32, 39)], 1.25)
