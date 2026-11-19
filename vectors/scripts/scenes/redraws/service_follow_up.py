from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import speech_bubble

DESCRIPTION = "A curved reply arrow sweeps across the upper corner of a message bubble."


def draw(s):
    bubble = speech_bubble(s)
    bubble.rows(16, 33, (32, 24), step=-13, ink=EDGE)
    points = oval(75, 44, 24, 17, -57, 91, count=25) + [(59, 61), (46, 61)]
    arrow(s, [bubble.at(u, v) for u, v in points], BOLD, head=9)
