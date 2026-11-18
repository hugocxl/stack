from geometry import BOLD, EDGE
from scenes.redraws._w3 import video_device

DESCRIPTION = "An open laptop pairs a scanned handwritten manuscript with typed lines and a text cursor."


def draw(s):
    screen = video_device(s)
    scan = [(14, 13), (14, 60), (39, 60), (49, 50), (49, 13)]
    screen.stroke(scan, EDGE, closed=True)
    screen.stroke([(39, 60), (39, 50), (49, 50)])
    for v, extent in ((47, 13), (39, 23), (31, 19), (23, 22)):
        screen.stroke([(19, v), (22, v + 1.5), (25, v - .6), (28, v + 1.4),
                       (31, v - .4), (19 + extent, v + .7)])
    screen.rules(60, 52, [34, 28, 32, 18], gap=9, ink=EDGE)
    screen.stroke([(82, 31), (88, 31)], BOLD)
    screen.stroke([(85, 31), (85, 19)], BOLD)
    screen.stroke([(82, 19), (88, 19)], BOLD)
