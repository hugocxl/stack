from geometry import EDGE
from scenes.redraws._w4 import speech_bubble

DESCRIPTION = "A single speech bubble contains a three-dot typing indicator."


def draw(s):
    bubble = speech_bubble(s)
    for u in (28, 46, 64):
        bubble.oval(u, 28, 3.6, 3.6, EDGE)
