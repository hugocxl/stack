from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w5 import device, rect

DESCRIPTION = "A smartphone shows a row of one-time passcode dots and carries a lock badge."


def draw(s):
    face = device(s, w=43)
    rect(s, face, 7, 27, 29, 13, 2.8)
    for x in (12.5, 18.5, 24.5, 30.5):
        s.line([face(u, v) for u, v in oval(x, 33.5, 1.3, 1.3, count=16)], EDGE)
    badge(s, "lock", *face(45, 52), 12)
