from geometry import DETAIL, EDGE

DESCRIPTION = "Two bound issues stack inside an open archive slipcase with grouped markings on their exposed spines."


def draw(s):
    s.box(0, 0, 0, 97, 64, 5, 2)
    s.face([(0, 0, 5), (0, 64, 5), (0, 64, 49), (0, 0, 49)], DETAIL)
    s.face([(0, 0, 5), (97, 0, 5), (97, 0, 49), (0, 0, 49)], DETAIL)
    for z, spine in ((6, 67), (24, 72)):
        s.box(6, 7, z, 84, spine - 7, 17, 2)
        for offset in (3, 14):
            s.line([(9, spine, z + offset), (87, spine, z + offset)], DETAIL)
        for start, width in ((14, 26), (67, 12)):
            s.line([(start, spine, z + 8.5), (start + width, spine, z + 8.5)], EDGE)
    s.face([(97, 0, 5), (97, 64, 5), (97, 64, 49), (97, 0, 49)])
    for x in (0, 92):
        s.face([(x, 64, 5), (x + 5, 64, 5), (x + 5, 64, 44), (x, 64, 44)])
    s.box(0, 0, 44, 97, 64, 5, 2)
