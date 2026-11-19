from geometry import BOLD, EDGE
from scenes.redraws._w3 import accessibility_phone

DESCRIPTION = "A sign-in field on a smartphone forks into a key option and a fingerprint option."


def draw(s):
    phone = accessibility_phone(s)
    phone.rect(10, 59, 27, 9, 2, EDGE)
    phone.rules(14, 63.5, [15])
    phone.stroke([(23.5, 59), (23.5, 48), (15, 40), (15, 36)], BOLD)
    phone.stroke([(23.5, 48), (32, 40), (32, 36)], BOLD)
    for x in (9, 26):
        phone.rect(x, 18, 12, 16, 3, EDGE)
    phone.oval(15, 28, 2.8, 2.8, EDGE)
    phone.stroke([(15, 25), (15, 21), (18, 21)], EDGE)
    for x, v, r in ((32, 26, 4), (32, 26, 2)):
        phone.stroke([(x - r, v - 1), (x - r, v + 1), (x - r/2, v + r),
                      (x + r/2, v + r), (x + r, v + 1), (x + r, v - 3)], EDGE)
