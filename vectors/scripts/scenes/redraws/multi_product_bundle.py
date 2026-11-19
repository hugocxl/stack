from geometry import DETAIL, EDGE

DESCRIPTION = "An open retail carton reveals a tall product box and a short bottle held by one band."


def draw(s):
    s.box(0, 0, 0, 75, 47, 5, 2)
    s.face([(0, 0, 5), (75, 0, 5), (75, 0, 44), (0, 0, 44)])
    s.face([(0, 0, 44), (75, 0, 44), (70, -20, 57), (5, -20, 57)])
    s.face([(0, 0, 5), (0, 47, 5), (0, 47, 22), (0, 0, 44)])

    s.box(11, 9, 5, 27, 25, 50, 2)
    s.face([(15, 34, 39), (34, 34, 39), (34, 34, 49), (15, 34, 49)], DETAIL)
    s.disk(55, 22, 5, 12, 12, 34)
    s.disk(55, 22, 39, 7, 7, 6, EDGE)
    s.face([(11, 34, 27), (67, 34, 27), (67, 34, 36), (11, 34, 36)], EDGE)
    s.face([(67, 34, 27), (67, 15, 27), (67, 15, 36), (67, 34, 36)], DETAIL)
    s.face([(75, 0, 5), (75, 47, 5), (75, 47, 22), (75, 0, 44)])
    s.face([(0, 47, 5), (75, 47, 5), (75, 47, 22), (0, 47, 22)])
