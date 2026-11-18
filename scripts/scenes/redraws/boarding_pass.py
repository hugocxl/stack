from geometry import BOLD, DETAIL
from scenes.redraws._w5 import plane_mark, ticket_face

DESCRIPTION = "A notched airline boarding pass shows a large airplane silhouette and a barcode on its stub."


def draw(s):
    face = ticket_face(s)
    plane_mark(s, face, 22, 21, 1.01, BOLD)
    for z, length in ((26, 20), (20, 15), (14, 20)):
        s.line([face(42, z), face(42 + length, z)], DETAIL)
    for x in (74, 76, 79, 81, 84, 86):
        s.line([face(x, 8), face(x, 32)], BOLD)
