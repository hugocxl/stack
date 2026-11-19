from geometry import BOLD, DETAIL, EDGE, rounded

DESCRIPTION = "A standing weekly calendar highlights one block in its appointment grid."


def draw(s):
    def face(x, z):
        return (x, 6 - .27 * z, z)

    s.face([face(35, 0), face(35, 60), (35, -25, 0)], EDGE)
    s.face([face(x, z) for x, z in ((-35, 0), (35, 0), (35, 60), (-35, 60))], EDGE)
    for x in (-21, 21):
        s.tube([(x, -6, 53), (x, -6, 61), (x, -10, 65),
                (x, -14, 64), (x, -16, 59), (x, -14, 56)], 1.5)
    s.line([face(-34, 44), face(34, 44)], EDGE)
    for z in (10, 21, 32):
        s.line([face(-30, z), face(30, z)], DETAIL)
    for x in (-30, -18, -6, 6, 18, 30):
        s.line([face(x, 10), face(x, 44)], DETAIL)
    selection = rounded(7.1, 14, 9.8, 16.5, 1.8)
    s.face([face(x, z) for x, z in selection], BOLD)
    s.line([face(10, 22), face(14, 22)], BOLD)
