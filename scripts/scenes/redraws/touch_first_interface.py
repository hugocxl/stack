from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w3 import interface_phone

DESCRIPTION = "A large fingerprint and two contact ripples mark the primary touch target on a phone screen."


def draw(s):
    phone = interface_phone(s)
    phone.rules(10, 65, [15], ink=EDGE)
    phone.rules(10, 59, [25])
    phone.oval(23, 35, 15, 17, EDGE)
    for r, drop in ((10, 4), (7, 7), (4, 8)):
        arch = oval(23, 37, r, r, -25, 180, 32)
        phone.stroke([*arch, (23 - r - 1, 37 - drop)], BOLD)
    for start, end in ((56, 124), (236, 304)):
        phone.stroke(oval(23, 35, 17, 22, start, end, 20), DETAIL)
