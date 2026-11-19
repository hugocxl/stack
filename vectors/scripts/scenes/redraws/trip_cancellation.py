from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w5 import plane_mark, ticket_face

DESCRIPTION = "A notched travel booking ticket with an airplane pictogram carries an X badge on its stub."


def draw(s):
    face = ticket_face(s)
    plane_mark(s, face, 25, 21, 1.06)
    for z, length in ((25, 18), (17, 14)):
        s.line([face(44, z), face(44 + length, z)], DETAIL)
    x, y, z = face(86, 35)
    badge(s, "x", x + 3, y + 3, z + 2, 15)
