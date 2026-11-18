from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w5 import device, shield_mark

DESCRIPTION = "A smartphone setup screen shows a shield, a progress strip, and an attached plus badge."


def draw(s):
    face = device(s)
    shield_mark(s, face, 19, 40, 23)
    for x, end in ((10, 15), (17, 22), (24, 29)):
        s.line([face(x, 22), face(end, 22)], DETAIL)
    badge(s, "plus", *face(37, 19), 11)
