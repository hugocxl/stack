from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, camera_mark, speech_bubble, stethoscope_mark

DESCRIPTION = "A laptop shows a video consultation with a stethoscope in the call tile and a speech bubble beside it."


def draw(s):
    s.box(-5, -3, 0, 101, 54, 5, 4)
    keys = Surface(s, lambda u, v: (u, v, 5))
    keys.frame(8, 9, 74, 20, 2)
    for v in (15, 22):
        keys.line([(10, v), (80, v)])
    keys.frame(34, 34, 22, 10, 2)
    display = Surface(s, lambda u, v: (u, 1 - .32*v, v + 5))
    display.slab(rounded(0, 0, 91, 62, 4), 6)
    display.frame(6, 7, 79, 48, 3, EDGE)
    display.oval(46, 58.5, 1.35, 1.35, DETAIL)
    stethoscope_mark(display, 36, 37, .94)
    display.line([(6, 19), (85, 19)], DETAIL)
    camera_mark(display, 43, 13, .27)
    bubble = speech_bubble(s, width=33, height=22, y=-18, z=38, depth=3, angle=0, u0=68)
    bubble.rows(7, 13, (17, 11), step=-5, ink=EDGE)
