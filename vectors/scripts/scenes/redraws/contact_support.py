from geometry import EDGE
from scenes.redraws._w4 import headset, speech_bubble

DESCRIPTION = "A support headset has a speech bubble at the tip of its boom microphone."


def draw(s):
    headset(s)
    bubble = speech_bubble(s, width=35, height=22, u0=-24, y=18, z=15, depth=3, tail_at=.63)
    bubble.rows(8, 15, (18, 12), step=-6, ink=EDGE)
