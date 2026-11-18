from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w4 import Surface, upright
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A patient transport van has a prominent medical cross on its side panel."


def draw(s):
    depth = 39
    for x in (20, 88):
        upright(s, oval(x, 11, 11, 11)[:-1], depth - 1, 6)
        Surface(s, lambda u, v: (u, depth - 1, v)).oval(x, 11, 4, 4, DETAIL)

    shell = [(0, 11), (0, 48), (5, 55), (72, 55), (82, 50),
             (93, 33), (108, 28), (111, 23), (111, 11)]
    for (x, z), (u, v) in zip(shell[1:], shell[2:]):
        s.face([(x, 0, z), (u, 0, v), (u, depth, v), (x, depth, z)])
    arches = [(a, z) for x in (88, 20) for a, z in oval(x, 11, 13, 13, 0, 180, 30)]
    s.face([(x, depth, z) for x, z in (*shell, *arches)])
    s.face([(111, 0, 11), (111, 0, 23), (111, depth, 23), (111, depth, 11)])

    face = Surface(s, lambda u, v: (u, depth, v))
    face.outline([(72, 47), (80, 47), (88, 35), (72, 35)], EDGE)
    face.line([(66, 49), (66, 14)], DETAIL)
    face.rows(72, 30, (7,))
    medical_cross(face, 43, 36, 12, BOLD)
    face.line([(6, 19), (9, 19)], EDGE)
    face.line([(53, 19), (62, 19)], EDGE)

    s.face([(83.3, y, 48) for y in (4, 35)] + [(91.7, y, 35) for y in (35, 4)])
    for y in (4, 28):
        s.line([(111, y, 19), (111, y + 7, 19)], EDGE)
    s.line([(111, 8, 14), (111, 31, 14)], DETAIL)
