from geometry import DETAIL, EDGE

DESCRIPTION = "Four equal service cubes connect directly to their peers through a crisscross mesh."


def draw(s):
    back, left, right, front = (-31, -31), (-31, 31), (31, -31), (31, 31)
    for a, b in ((back, left), (back, right), (left, front), (right, front), (back, front)):
        s.line([(*a, 10), (*b, 10)], EDGE)
    for a, b in ((left, (-3, 3)), ((3, -3), right)):
        s.line([(*a, 10), (*b, 10)], EDGE)
    for x, y in (back, left, right, front):
        s.box(x - 11, y - 11, 0, 22, 22, 22, 1.8)
        for offset in (-4, 2):
            s.line([(x + offset, y + 11, 11), (x + offset + 2, y + 11, 11)], DETAIL)
