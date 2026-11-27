from geometry import EDGE
from scenes.redraws._sf import turned

DESCRIPTION = "A jointed robot arm lowers its gripper over a single part on the floor."


def joint(s, p, r=7):
    x, y, z = p
    turned(s, [(.5, -r), (r*.72, -r*.72), (r, 0), (r*.72, r*.72), (.5, r)], x, y, z, steps=3)


def draw(s):
    turned(s, [(20, 0), (20, 7)], steps=1)
    turned(s, [(10, 7), (10, 30)], steps=1)
    shoulder, elbow, wrist, tool = (0, 0, 32), (30, -8, 80), (68, -4, 62), (68, -4, 40)
    joint(s, shoulder, 10)
    s.tube([shoulder, elbow], 6, EDGE)
    joint(s, elbow, 8)
    s.tube([elbow, wrist], 4.6, EDGE)
    joint(s, wrist, 6)
    s.tube([wrist, tool], 3, EDGE)
    s.tube([(63, 1, 40), (73, -9, 40)], 2.4, EDGE)
    for d in (-5, 5):
        s.tube([(68 + d, -4 - d, 40), (68 + d*1.3, -4 - d*1.3, 26)], 1.6, EDGE)
    s.box(60, -12, 0, 16, 16, 14, 2)
