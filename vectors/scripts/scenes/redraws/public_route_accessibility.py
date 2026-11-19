from geometry import BOLD, DETAIL, oval
from scenes.redraws.next_bus_countdown import side_window, wheel_side, windscreen

DESCRIPTION = "A city bus displays a wheelchair accessibility pictogram beside its double doors."


def accessibility_symbol(s, x, y, z, size):
    # Standard wheelchair pictogram with the wheel open at the knees.
    def line(points):
        s.line([(x + a * size, y, z + b * size) for a, b in points], BOLD)

    line(oval(-.18, -.20, .30, .30, 78, 335, 28))
    line([(-.26, .27), (-.18, -.12), (.24, -.12), (.40, -.46), (.56, -.46)])
    line([(-.19, .03), (.11, .03)])
    line(oval(-.29, .43, .071, .071, count=18))


def draw(s):
    y = 32
    centers = (16, 79)
    for x in centers:
        wheel_side(s, x, y - 1, 9)

    arches = []
    for x in reversed(centers):
        arches.extend((a, y, z) for a, z in oval(x, 10, 10, 10, 0, 180, 22))
    s.face([(0, y, 10), (0, y, 44), (4, y, 49), (93, y, 49), (98, y, 44),
            (98, y, 10), *arches])
    s.face([(4, 0, 49), (93, 0, 49), (93, y, 49), (4, y, 49)])
    s.face([(93, 0, 49), (98, 0, 44), (98, y, 44), (93, y, 49)])
    s.face([(98, 0, 10), (98, 0, 44), (98, y, 44), (98, y, 10)])
    windscreen(s, 98, 4, 25, 24, 15)
    for a in (6, 24):
        s.face([(98, b, z) for b, z in oval(a, 18, 2, 2, count=24)[:-1]], DETAIL)

    for x, w in ((6, 20), (30, 18), (78, 15)):
        side_window(s, x, y, 29, w, 14)
    side_window(s, 52, y, 13, 19, 30)
    s.line([(61.5, y, 13), (61.5, y, 43)], DETAIL)
    s.line([(52, y, 23), (71, y, 23)], DETAIL)
    accessibility_symbol(s, 39, y + .01, 19.9, 15.5)
