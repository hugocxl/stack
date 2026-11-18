from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "An open-ended wrench crosses the lower corner of a flat-roofed building."


def draw(s):
    s.box(-10, 0, 0, 74, 34, 71, 2)
    s.box(-12, -2, 70, 78, 38, 4, 2)
    s.box(-5, 34, 45, 63, 1.2, 14, 1)
    for x in (10, 26, 42):
        s.line([(x, 35.2, 45), (x, 35.2, 59)], DETAIL)
    s.box(0, 34, 0, 19, 1.2, 30, 1)

    # The wrench is an extruded, concave silhouette with a real open jaw.
    def point(u, v, depth=0):
        return 38 + .84*u - .54*v, 42 - depth, 18 + .54*u + .84*v

    outline = [(-29, -4), (6, -4), (10, -9), (16, -11), (23, -9), (27, -4),
               (17, -4), (14, 0), (17, 4), (27, 4), (23, 9), (16, 11),
               (10, 9), (6, 4), (-29, 4), (-33, 2), (-33, -2)]
    s.face([point(u, v, 4) for u, v in outline], EDGE)
    s.face([point(u, v) for u, v in outline], BOLD)
