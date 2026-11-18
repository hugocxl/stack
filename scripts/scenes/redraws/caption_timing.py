from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "One caption block starts on a bold playhead that also crosses the audio waveform below it."


def draw(s):
    timeline = Surface(s, (0, 0, 0), rise=(-.5, .87), back=(0, -.87, -.5))
    timeline.plate(rounded(0, 0, 120, 65, 5), 13)
    timeline.rect(7, 8, 106, 49, 3, EDGE)
    timeline.rules(7, 32, [106], ink=EDGE)
    timeline.stroke([(43, 52), (95, 52), (97, 50), (97, 39),
                     (95, 37), (43, 37)], EDGE)
    timeline.rules(50, 44, [37], ink=EDGE)
    timeline.rules(12, 21, [95], ink=DETAIL)
    for i, h in enumerate((3, 6, 4, 9, 6, 3, 7, 5, 10, 4, 5, 8, 4, 7, 4, 2)):
        x = 13 + i * 6
        if x != 43:
            timeline.stroke([(x, 21 - h), (x, 21 + h)], EDGE)
    timeline.stroke([(38, 60), (48, 60), (43, 54)], BOLD, closed=True)
    timeline.stroke([(43, 54), (43, 10)], BOLD)
