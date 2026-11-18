from geometry import BOLD, DETAIL, EDGE, oval
from scenes.systems_shapes import bezel

DESCRIPTION = "A low-floor shuttle bus has an open side door and a wheelchair ramp lowered to the ground."

BODY_WIDTH = 36
WHEELS = (20, 85)


def _side(y):
    rear, front = WHEELS
    # The wheel arches interrupt the lower edge of the body.
    profile = [
        (0, 11), (0, 45), (5, 51), (94, 51),
        (99, 46), (105, 30), (105, 14), (102, 11),
        *oval(front, 11, 12, 12, 0, 180, 24),
        *oval(rear, 11, 12, 12, 0, 180, 24),
    ]
    return [(x, y, z) for x, z in profile]


def _wheel(s, x, y):
    s.face([(a, y, z) for a, z in oval(x, 9.3, 9, 9)[:-1]], EDGE)
    s.line([(a, y, z) for a, z in oval(x, 9.3, 3.6, 3.6)], DETAIL)


def _span(s, a, b):
    x0, z0 = a
    x1, z1 = b
    s.face([(x0, 0, z0), (x1, 0, z1),
            (x1, BODY_WIDTH, z1), (x0, BODY_WIDTH, z0)])


def draw(s):
    y = BODY_WIDTH
    for x in WHEELS:
        _wheel(s, x, y - 1)

    # The open doorway reveals the thickness of its rear jamb.
    s.face([(46, y - 4, 13), (46, y, 13),
            (46, y, 45), (46, y - 4, 45)], DETAIL)

    roof_and_nose = [(5, 51), (94, 51), (99, 46), (105, 30), (105, 14), (102, 11)]
    for a, b in zip(roof_and_nose, roof_and_nose[1:]):
        _span(s, a, b)

    doorway = [(46, y, 13), (68, y, 13), (68, y, 45), (46, y, 45)]
    s.face(_side(y), openings=[doorway])
    bezel(s, 7, y, 31, 33, 14, EDGE, 2)
    s.line([(23, y, 31), (23, y, 45)], DETAIL)
    s.face([(75, y, 31), (98, y, 31), (93, y, 45), (75, y, 45)], EDGE)

    # Windshield follows the raked nose. The lamps sit on the vertical fascia.
    def windshield(y, z):
        return (105 - (z - 30) * 6 / 16, y, z)

    s.face([windshield(a, z) for a, z in ((4, 32), (32, 32), (32, 44), (4, 44))])
    for a in (4, 25):
        s.face([(105, a, 22), (105, a + 7, 22),
                (105, a + 7, 26), (105, a, 26)], DETAIL)
    s.line([(105, 4, 17), (105, 32, 17)], DETAIL)

    ramp_length = 31
    ramp_end = y + ramp_length
    s.face([(46, y, 13), (68, y, 13),
            (68, ramp_end, 1), (46, ramp_end, 1)], BOLD)
    for x in (49, 65):
        s.line([(x, y + offset, 13 - 12 * offset / ramp_length)
                for offset in (4, ramp_length - 4)], DETAIL)
