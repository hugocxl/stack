from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w5 import avatar_mark, panel, rect

DESCRIPTION = "A tabbed personal dossier shows a profile on its cover and carries a downward arrow badge at its opening."


def draw(s):
    s.face([(0, -14, 0), (65, -14, 0), (65, -23, 50), (30, -23, 50),
            (26, -24, 58), (4, -24, 58), (0, -23, 52)], EDGE)
    paper = lambda x, z: (x, -13 - .14 * z, z)
    panel(s, rounded(5, 4, 55, 43, 1.3), paper, 1.8, DETAIL)
    face = lambda x, z: (x, -.12 * z, z)
    panel(s, rounded(0, 0, 65, 40, 2.4), face, 2.4)
    rect(s, face, 7, 8, 23, 24, 2, DETAIL)
    avatar_mark(s, face, 18.5, 19, 1.23)
    for z, length in ((23, 18), (15, 15)):
        s.line([face(36, z), face(36 + length, z)], DETAIL)
    badge(s, "down", 59, -14, 47, 11)
