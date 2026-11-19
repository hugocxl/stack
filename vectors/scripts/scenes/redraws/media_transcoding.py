from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import paper, play_mark

DESCRIPTION = "A video file shows a conversion arrow pointing from a perforated film frame to a playback frame."


def draw(s):
    file = paper(s, 76, pitch=.77, run=.50, angle=-22, depth=6)
    file.slab([(0, 0), (95, 0), (112, 17), (112, 76), (0, 76)], 6)
    file.line([(95, 0), (95, 17), (112, 17)], EDGE)
    file.rows(10, 14, (44,), ink=EDGE)
    file.frame(15, 25, 23, 39, 2, EDGE)
    file.line([(21, 26), (21, 63)])
    file.line([(32, 26), (32, 63)])
    file.line([(21, 45), (32, 45)], EDGE)
    for v in (32, 40, 49, 57):
        file.rows(17, v, (2,), ink=EDGE)
        file.rows(34, v, (2,), ink=EDGE)
    file.frame(75, 29, 27, 31, 2, EDGE)
    play_mark(file, 88, 42, 6, EDGE)
    file.rows(81, 54, (14,))
    arrow(s, [file.at(45, 45), file.at(68, 45)], BOLD, head=9)
