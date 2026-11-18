from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w5 import ticket_face
from scenes.redraws.garage_vacancy_queue import parking_letter

DESCRIPTION = "A notched parking ticket shows a large parking P and carries a check badge on its stub."


def draw(s):
    face = ticket_face(s)
    parking_letter(s, lambda x, z: face(23 + .88*x, 21 + .88*z))
    for z, width in ((13, 20), (20, 16), (27, 20)):
        s.line([face(42, z), face(42 + width, z)], DETAIL)
    badge(s, "check", 86, -15, 31, 13)
