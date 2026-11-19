from geometry import DETAIL, EDGE

DESCRIPTION = "Three upright volumes with projecting bookmark ribbons form a reading list."


def draw(s):
    for x, w, h in ((0, 24, 72), (28, 25, 82), (57, 26, 67)):
        s.box(x, 0, 0, w, 33, h, 2)
        s.line([(x + 4, 2, h), (x + 4, 30, h), (x + w - 4, 30, h),
                (x + w - 4, 2, h)], DETAIL)
        u = x + w/2
        s.face([(u - 4, 33, h - 1), (u + 4, 33, h - 1), (u + 4, 33, h - 19),
                (u, 33, h - 15), (u - 4, 33, h - 19)], EDGE)
        s.line([(x + 4, 33, 12), (x + w - 4, 33, 12)], DETAIL)
