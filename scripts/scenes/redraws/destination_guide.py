from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "An open city guide shows a street map on one page and a triumphal arch on the facing page."


def draw(s):
    def left(x, z):
        return x, -z*.71 - x*.22, z + x*.07

    def right(x, z):
        return x, -z*.71 + (x - 40)*.23 - 8.8, z + (80 - x)*.07

    for a, b, point in ((0, 40, left), (40, 80, right)):
        outline = [point(a, 0), point(b, 0), point(b, 48), point(a, 48)]
        cover = [(x, y - 2.8, z - 1.3) for x, y, z in outline]
        s.face(cover, EDGE)
        s.face(outline)
        s.line([point(a + 2, 1.6), point(b - 1, 1.6)], DETAIL)
    for street in ([(5, 13), (17, 14), (35, 19)], [(5, 28), (20, 29), (34, 33)],
                   [(12, 6), (13, 18), (11, 34), (11, 42)],
                   [(27, 6), (25, 20), (22, 34), (26, 42)],
                   [(6, 35), (19, 22), (33, 11)]):
        s.line([left(x, z) for x, z in street], DETAIL)
    arch = [(46, 12), (46, 16), (49, 16), (49, 31), (46, 31), (46, 35),
            (50, 35), (50, 39), (70, 39), (70, 35), (74, 35), (74, 31),
            (71, 31), (71, 16), (74, 16), (74, 12), (64.5, 12),
            (64.5, 23), (63.5, 27), (60, 29), (56.5, 27), (55.5, 23), (55.5, 12), (46, 12)]
    s.line([right(x, z) for x, z in arch], BOLD)
    for z in (31, 35):
        s.line([right(49, z), right(71, z)], DETAIL)
