from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import coin

DESCRIPTION = "An articulated quadruped armature has exposed pivot joints and one front leg held in a raised pose."


def draw(s):
    # The far legs support the body, and the near pair show the bend at each pivot.
    for joints in (
        [(17, -13, 43), (23, -17, 26), (15, -18, 8)],
        [(51, -13, 43), (59, -19, 27), (63, -24, 8)],
    ):
        s.tube(joints, 3, EDGE)
        x, y, _ = joints[-1]
        s.box(x - 7, y - 4, 3, 13, 8, 5, 3)

    s.box(7, -17, 39, 59, 27, 21, 10)
    s.tube([(10, -5, 48), (-3, -6, 51), (-12, -8, 61)], 2.4)
    s.tube([(57, -7, 52), (69, -7, 67), (70, -7, 72)], 4)
    s.box(62, -15, 66, 26, 18, 14, 7)

    for joints in (
        [(18, 10, 46), (25, 12, 25), (20, 15, 8)],
        [(53, 10, 46), (61, 19, 25), (81, 17, 42)],
    ):
        for start, end in zip(joints, joints[1:]):
            s.tube([start, end], 3.8, EDGE)
        for x, y, z in joints[:2]:
            coin(s, x, y + 2, z, 5, depth=2, ink=BOLD)
            s.line([(x - 1.5, y + 2, z), (x + 1.5, y + 2, z)], DETAIL)
        x, y, z = joints[-1]
        s.box(x - 3, y - 4, z - 5, 13, 9, 5, 3)
