from geometry import DETAIL, EDGE

DESCRIPTION = "A shopfront with an awning and entry door frames one dashed outline inside its empty display bay."


def draw(s):
    s.box(0, 0, 0, 96, 31, 70, 2)
    y = 31.4
    s.face([(9, y, 9), (34, y, 9), (34, y, 49), (9, y, 49)])
    s.line([(14, y, 13), (14, y, 44), (29, y, 44), (29, y, 13)], DETAIL)
    s.line([(26, y, 23), (26, y, 30)], EDGE)
    s.face([(40, y, 14), (87, y, 14), (87, y, 49), (40, y, 49)])
    s.line([(46, y, 20), (81, y, 20), (81, y, 43), (46, y, 43), (46, y, 20)],
           EDGE, dashed=True)

    s.face([(3, 30, 66), (93, 30, 66), (93, 45, 56), (3, 45, 56)])
    s.face([(3, 45, 56), (93, 45, 56), (93, 45, 52), (3, 45, 52)])
    for x in (18, 33, 48, 63, 78):
        s.line([(x, 30, 66), (x, 45, 56), (x, 45, 52)], DETAIL)
