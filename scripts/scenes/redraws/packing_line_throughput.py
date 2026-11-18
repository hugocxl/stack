from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w1 import roller_bridge, software_package

DESCRIPTION = "A taped carton rides a short roller conveyor with a speed gauge built into its side housing."


def draw(s):
    for x in (-35, 31):
        s.box(x, -11, 0, 5, 26, 20, 1.3)
    roller_bridge(s, -40, 43, 0)
    software_package(s, 14, -2, 20, .60, show_code=False)
    s.box(-40, 10, 6, 29, 7, 23, 2)

    arc = oval(-25.5, 12, 10.5, 12, 0, 180, count=32)
    s.line([(x, 17, z) for x, z in [*arc, arc[0]]], EDGE)
    for x, z in oval(-25.5, 12, 8.4, 9.5, 34, 146, count=4):
        s.line([(x, 17, z), (-25.5 + (x + 25.5) * .77, 17, 12 + (z - 12) * .77)], DETAIL)
    s.line([(-25.5, 17, 12), (-20.7, 17, 19)], BOLD)
