from geometry import DETAIL, oval
from scenes.redraws._kit import coin
from scenes.redraws._w5 import cloche_mark, printed_stroke

DESCRIPTION = "A delivery scooter carries a latched insulated food box behind its seat."


def draw(s):
    for x, y in ((8, 12), (57, 12)):
        coin(s, x, y, 11, 10.5, depth=7)
        printed_stroke(s, lambda u, v: (u, y + .02, v), oval(x, 11, 5.6, 5.6), DETAIL)

    near = lambda x, z: (x, 13, z)
    # The rear fairing and step-through floor are joined beneath the saddle.
    profile = [(-3, 19), (0, 28), (13, 33), (25, 33), (28, 27), (29, 19),
               (44, 19), (51, 39), (55, 43), (60, 42), (57, 30), (49, 14),
               (27, 13), (21, 16), (15, 22), (7, 24), (2, 20)]
    s.face([(x, -2, z) for x, z in profile], DETAIL)
    for (a, z), (b, h) in zip(profile[:9], profile[1:10]):
        if a < b:
            s.face([(a, -2, z), (b, -2, h), near(b, h), near(a, z)], DETAIL)
    s.face([near(x, z) for x, z in profile])
    printed_stroke(s, near, [(2, 25), (11, 29), (22, 29)], DETAIL)
    s.tube([(55, 7, 39), (57, 8, 29), (57, 12, 11)], 1.55)
    s.solid(oval(57, 7, 11, 6)[:-1], 21, 4, crease=False)
    s.tube([(54, 7, 40), (53, 7, 51), (50, 7, 54)], 1.7)
    s.tube([(49, -4, 54), (52, 6, 54), (47, 16, 53)], 1.3)
    coin(s, 56, 9, 45, 4.3, depth=4.5)
    s.box(14, -2, 33, 17, 15, 4.5, 2.2)
    s.box(-8, -6, 29, 22, 23, 3, 1.4)
    s.box(-10, -7, 32, 25, 25, 20, 2.5)
    s.box(-11, -8, 49, 27, 27, 5, 2)
    face = lambda x, z: (x, 18, z)
    cloche_mark(s, face, 2.5, 39, .66)
