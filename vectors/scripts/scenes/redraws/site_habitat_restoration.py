from geometry import DETAIL, EDGE
from scenes.redraws._sf import left_face, tree

DESCRIPTION = "A young tree and new shoots grow from a cutaway block of soil with exposed roots."


def draw(s):
    s.box(-50, -36, 0, 100, 72, 26, 2)
    front = left_face(-50, 36, 0)
    for pts in ([(50, 26), (46, 16), (40, 8)], [(50, 26), (54, 14), (62, 6)], [(48, 20), (34, 14)], [(52, 18), (66, 16)]):
        s.line([front(u, v) for u, v in pts], DETAIL)
    tree(s, 0, 20, 26, 54, 20)
    for x, y in ((-34, 10), (-24, 22), (32, 4)):
        s.line([(x, y, 26), (x, y, 34)], EDGE)
        s.line([(x, y, 31), (x - 4, y + 4, 35)], EDGE)
        s.line([(x, y, 33), (x + 4, y - 4, 37)], EDGE)
