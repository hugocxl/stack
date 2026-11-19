from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, microphone, play

DESCRIPTION = "A transcript player groups short lines under alternating microphone and timestamp icons."


def draw(s):
    panel = Surface(s, (0, 60, 7), rise=(-.66, .75), back=(0, -.75, -.66))
    s.face([(11, 12, 0), (70, 12, 0), (70, 38, 26), (11, 38, 26)])
    panel.plate(rounded(0, 0, 83, 94, 6), 10)
    panel.rect(5, 6, 73, 82, 4, EDGE)
    play(panel, 15, 77, 9, EDGE)
    panel.rules(24, 77, [43])
    panel.stroke([(10, 69), (73, 69)], DETAIL)

    for i, v in enumerate((58, 36, 14)):
        microphone(panel, 17, v + 1, 11, EDGE if i % 2 == 0 else DETAIL)
        panel.oval(68, v + 3, 4.5, 4.5, EDGE)
        panel.stroke([(68, v + 5.5), (68, v + 3), (70, v + 2)], EDGE)
        widths = ([30, 23], [25, 31], [32, 18])[i]
        panel.rules(26, v + 4, widths, gap=7, ink=EDGE)
        if i < 2:
            panel.rules(10, v - 11, [63])
