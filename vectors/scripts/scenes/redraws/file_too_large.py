from geometry import BOLD, EDGE
from scenes.redraws._kit import warning
from scenes.redraws._w3 import sheet

DESCRIPTION = "A file shows a size bar crossing a dashed limit line and carries an attached warning triangle."


def draw(s):
    file = sheet(s, 65, 76, rise=(-.29, .96), depth=5)
    file.rules(11, 56, [23], ink=EDGE)
    for x, height in ((12, 12), (27, 18), (42, 30)):
        file.rect(x, 15, 9, height, 1, BOLD if height == 30 else EDGE)
    for start, end in ((8, 42), (51, 58)):
        file.stroke([(start, 37), (end, 37)], EDGE, dashed=True)
    warning(s, *file.point(70, 3, -5), 28)
