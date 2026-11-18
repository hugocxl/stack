from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import arrow

DESCRIPTION = "A curved return arrow wraps beneath the battery grip of a cordless power drill."


def draw(s):
    loop = [(x, y, 3) for x, y in oval(34, 25, 39, 33, -65, 119, 32)]
    arrow(s, loop, EDGE, head=9)

    s.box(13, 10, 0, 43, 26, 11, 4)
    s.line([(17, 36, 5), (51, 36, 5)], DETAIL)
    s.tube([(-32, 19, 46), (-15, 19, 46)], 1.7)
    for x in (-30, -25, -20):
        s.line([(x, 19, 47.4), (x + 2, 20, 45.1)], DETAIL)
    s.tube([(-16, 19, 46), (-6, 19, 46)], 4.5)

    outline = [(-6, 37), (-6, 56), (42, 56), (49, 51), (49, 39), (43, 35),
               (38, 34), (40, 11), (23, 11), (19, 34), (11, 34), (8, 37)]
    s.face([(x, 13, z) for x, z in outline], EDGE)
    for a, b in zip(outline, outline[1:] + outline[:1]):
        if b[0] > a[0] or (b[0] == a[0] and b[1] < a[1]):
            s.face([(a[0], 13, a[1]), (b[0], 13, b[1]),
                    (b[0], 28, b[1]), (a[0], 28, a[1])], EDGE)
    s.face([(x, 28, z) for x, z in outline], EDGE)
    s.face([(14, 28, 34), (21, 28, 34), (22, 28, 25), (16, 28, 27)], EDGE)
    for x in (33, 38, 43):
        s.line([(x, 28, 44), (x, 28, 49)], DETAIL)
