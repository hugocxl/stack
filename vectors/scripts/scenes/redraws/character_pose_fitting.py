from geometry import EDGE
from scenes.redraws._sf import turned

DESCRIPTION = "A jointed four-legged armature stands with one front leg raised at its pivots."


def ball(s, p, r):
    x, y, z = p
    turned(s, [(.4, -r), (r*.72, -r*.72), (r, 0), (r*.72, r*.72), (.4, r)], x, y, z, steps=3)


def limb(s, hip, knee, foot):
    s.tube([hip, knee], 2.6, EDGE)
    s.tube([knee, foot], 2.2, EDGE)
    ball(s, knee, 3.6)
    if foot[2] < 5:
        turned(s, [(4.5, 0), (4.5, 2.4)], foot[0], foot[1], 0, steps=1)
    else:
        ball(s, foot, 3)


def draw(s):
    back = [((-24, -11, 38), (-26, -11, 20), (-24, -11, 3)), ((22, -11, 38), (20, -11, 20), (22, -11, 3))]
    front = [((-24, 11, 38), (-28, 11, 20), (-26, 11, 3)), ((22, 11, 38), (36, 11, 44), (44, 11, 32))]
    for hip, knee, foot in back:
        limb(s, hip, knee, foot)
        ball(s, hip, 4.2)
    s.tube([(-26, 0, 40), (24, 0, 40)], 7.5, EDGE)
    s.tube([(26, 0, 44), (40, 0, 56)], 2.8, EDGE)
    ball(s, (46, 0, 60), 7)
    for hip, knee, foot in front:
        limb(s, hip, knee, foot)
        ball(s, hip, 4.2)
