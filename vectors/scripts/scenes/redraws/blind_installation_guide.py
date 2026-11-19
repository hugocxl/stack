from geometry import DETAIL, EDGE


DESCRIPTION = "Two mounting brackets hold the headrail of a partly lowered Venetian blind inside a window frame."


def draw(s):
    s.box(54, -7, 6, 4, 3, 75, .5, DETAIL)
    s.face([(6, -7, 6), (106, -7, 6), (106, 0, 6), (6, 0, 6)], DETAIL)
    s.face([(6, 0, 6), (6, -7, 6), (6, -7, 81), (6, 0, 81)], DETAIL)
    s.face([(0, -7, 87), (112, -7, 87), (112, 0, 87), (0, 0, 87)], EDGE)
    s.face([(112, -7, 0), (112, 0, 0), (112, 0, 87), (112, -7, 87)], EDGE)
    s.face(
        [(0, 0, 0), (112, 0, 0), (112, 0, 87), (0, 0, 87)],
        EDGE,
        openings=[[(6, 0, 6), (106, 0, 6), (106, 0, 81), (6, 0, 81)]],
    )

    for x in (22, 92):
        s.line([(x, 2, 36), (x, 2, 72)], DETAIL)
    for z in (42, 49, 56, 63):
        s.box(14, 0, z, 88, 5, 1.8, .7)
    s.box(14, -1, 35, 88, 7, 2.8, .8)
    s.box(14, -2, 69, 88, 9, 9, .8)

    bracket_profile = [
        (-3, 81), (10, 81), (10, 67), (3, 67),
        (3, 69), (7, 69), (7, 78), (-3, 78),
    ]
    for x in (19, 89):
        end = x + 10
        s.face([(end, y, z) for y, z in bracket_profile], EDGE)
        s.face([(x, -3, 81), (end, -3, 81), (end, 10, 81), (x, 10, 81)], EDGE)
        s.face([(x, 10, 67), (end, 10, 67), (end, 10, 81), (x, 10, 81)], EDGE)
        s.line([(x + 3, 10, 74), (x + 7, 10, 74)], DETAIL)
