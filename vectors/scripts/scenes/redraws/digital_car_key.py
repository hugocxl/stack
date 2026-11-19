from geometry import BOLD, DETAIL, EDGE, oval, rounded

DESCRIPTION = "A smartphone displays a car silhouette with a toothed key centered beneath it."


def draw(s):
    s.box(0, 0, 0, 43, 72, 6, 6)
    screen = rounded(3, 3, 37, 66, 4.4)
    s.line([(x, y, 6) for x, y in screen + screen[:1]], EDGE)
    s.line([(16, 7.5, 6), (26, 7.5, 6)], DETAIL)
    s.line([(16, 64, 6), (27, 64, 6)], DETAIL)

    s.line([(9, 33, 6), (9, 28, 6), (13, 26, 6), (17, 21, 6), (25, 21, 6),
            (29, 26, 6), (34, 28, 6), (34, 33, 6), (31, 33, 6), (31, 36, 6),
            (27, 36, 6), (27, 33, 6), (16, 33, 6), (16, 36, 6), (12, 36, 6),
            (12, 33, 6), (9, 33, 6)], EDGE)
    s.line([(13, 26, 6), (29, 26, 6)], DETAIL)
    s.line([(12, 30, 6), (16, 30, 6)], DETAIL)
    s.line([(27, 30, 6), (31, 30, 6)], DETAIL)

    bow = oval(15, 46, 5.6, 5.6, 20, 340, 44)
    shaft = [(31, 44.1), (34, 46.7), (32, 49.1), (29, 49.1),
             (29, 47.5), (26, 47.5), (26, 49.1), (23, 49.1), (23, 47.9)]
    s.face([(x, y, 6) for x, y in bow + shaft], BOLD,
           openings=[[(x, y, 6) for x, y in oval(14.2, 46, 2, 2)[:-1]]])
