from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import software_package

DESCRIPTION = "A tape dispenser feeds a strip across the seam of a carton resting on a workbench."


def draw(s):
    for x, y in ((-34, -21), (29, -21), (-34, 17), (29, 17)):
        s.box(x, y, 0, 5, 5, 29, .8)
    s.box(-36, 17, 20, 71, 4, 4, 1)
    s.box(-39, -24, 29, 78, 49, 6, 1.8)
    software_package(s, 0, 0, 35, .75, show_code=False)

    # The dispenser roller touches the end of the tape strip.
    def point(y, z):
        return 0, y, z

    profile = [(1, 63), (5, 66), (9, 82), (16, 87), (25, 87), (31, 81),
               (31, 73), (28, 68), (35, 62), (33, 58), (22, 66), (17, 70), (11, 63)]
    s.face([(0, y - 3, z + 1.5) for y, z in profile], EDGE)
    s.face([point(y, z) for y, z in profile], EDGE)
    for radius in (7.2, 3.2):
        s.line([point(y, z) for y, z in oval(21, 78, radius, radius, count=32)], EDGE)
    s.line([(-3.75, 2, 62), (3.75, 2, 62)], DETAIL)
