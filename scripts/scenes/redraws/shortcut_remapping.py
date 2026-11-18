from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import flat, keycap

DESCRIPTION = "A curved remapping arrow joins two separate keyboard keycaps with different key markings."


def draw(s):
    keycap(s, 0, 17, 38)
    keycap(s, 62, 0, 38)
    left = flat(s, 0, 55, 8)
    left.stroke([(11, 16), (19, 24), (27, 16)], EDGE)
    left.stroke([(19, 24), (19, 11)], EDGE)
    right = flat(s, 62, 38, 8)
    right.stroke([(12, 20), (26, 20), (26, 26)], EDGE)
    right.stroke([(12, 20), (18, 25)], EDGE)
    right.stroke([(12, 20), (18, 15)], EDGE)
    arrow(s, [(21, 23, 11), (33, 15, 22), (46, 8, 28),
              (60, 5, 28), (72, 7, 23), (80, 12, 16)], BOLD, head=7)
