from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import audio_deck, chart_line, recorder_trace, rule

DESCRIPTION = "Three spaced bursts of speech sit above a single pacing slider on an audio display."


def draw(s):
    point = audio_deck(s, height=76)
    pattern = (0, 5, -6, 9, -13, 10, -6, 5, 0)
    rule(s, point, 13, 51, 108, DETAIL)
    for x, strength in ((15, .7), (50, 1), (92, .8)):
        recorder_trace(s, point, x, 51, 3.2, [strength*v for v in pattern], EDGE)
    chart_line(s, point, [(8, 34), (126, 34)], DETAIL)
    rule(s, point, 25, 20, 84, EDGE)
    s.face([point(x, z) for x, z in rounded(64, 13, 13, 14, 3)], BOLD)
