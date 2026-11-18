from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import clipboard, printed_check

DESCRIPTION = "A clipboard holds a completed form with three checked fields and a clock badge on its lower corner."


def draw(s):
    form = clipboard(s, 72, 83)
    form.rules(14, 60, [26], ink=EDGE)
    for z, width in ((45, 31), (32, 25), (19, 29)):
        form.rect(14, z - 4, 8, 8, .8, EDGE)
        printed_check(form, 18, z, 4.5)
        form.rules(29, z + 2, [width])
    badge(s, "clock", *form.point(69, 9, -4), 14)
