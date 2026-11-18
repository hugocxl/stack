from geometry import EDGE
from scenes.redraws._w4 import bezier_path, headset, speech_bubble

DESCRIPTION = "A call-center headset with a microphone boom carries a small speech bubble with a question mark."


def draw(s):
    headset(s)
    question = speech_bubble(s, width=26, height=26, y=0, z=52, depth=4,
                             u0=30, tail_at=.20)
    question.line(bezier_path(
        (9, 17), ((9, 22), (18, 23), (18, 18)),
        ((18, 14), (13, 15), (13, 11)),
    ), EDGE)
    question.oval(13, 6.5, .85, .85, EDGE)
