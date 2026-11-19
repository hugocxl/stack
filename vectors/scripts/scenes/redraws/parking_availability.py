from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w5 import rect
from scenes.redraws.garage_vacancy_queue import parking_letter, post

DESCRIPTION = "A freestanding parking sign displays a large P and a check badge at its upper corner."


def draw(s):
    post(s, 20, -2, 53, width=6)
    s.box(0, -5, 29, 42, 7, 40, 3)
    rect(s, lambda x, z: (x, 2, z), 4, 33, 34, 32, 2, DETAIL)
    parking_letter(s, lambda x, z: (19 + x, 2, 49 + z))
    badge(s, "check", 46, 3, 69, 12)
