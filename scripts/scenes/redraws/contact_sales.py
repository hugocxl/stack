from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import Surface, currency_mark, phone_receiver, speech_bubble

DESCRIPTION = "A desk telephone with a handset and keypad sits beneath a speech bubble containing a price tag."


def draw(s):
    s.solid(rounded(0, 0, 89, 66, 7), 0, 16, rounded(1, 1, 87, 64, 6))
    phone_receiver(s, x=44, y=29, z=16, on_base=True)
    keypad = Surface(s, lambda u, v: (u, v, 16.1))
    for y in (45, 54):
        for x in (31, 44, 57):
            keypad.frame(x, y, 8, 5, 1, EDGE)

    reply = speech_bubble(s, width=43, height=36, angle=-27,
                          y=-8, z=40, depth=4, u0=43, tail_at=.21)
    reply.outline([(5, 18), (14, 27), (35, 27), (35, 9), (14, 9)], EDGE)
    reply.oval(12, 18, 1.7, 1.7, DETAIL)
    currency_mark(reply, 25, 18, .65, EDGE)
