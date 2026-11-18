from geometry import BOLD, EDGE
from scenes.redraws._w2 import face_arrow, folded_sheet, recorder_trace, rule, speech_bubble

DESCRIPTION = "A speech waveform in a dialog bubble feeds into three aligned lines on a transcript page."


def draw(s):
    def plane(x, z):
        return .64*x, -.36*x - .14*z, .94*z

    def bubble(x, z):
        return plane(x, z + 23)

    def page(x, z):
        return plane(x + 112, z)

    speech_bubble(s, bubble, 74, 45, tail=.27)
    recorder_trace(s, bubble, 10, 23, 4.5,
                   (0, 3, -5, 11, -13, 6, -3, 2, -8, 8, -4, 2, 0), EDGE)
    folded_sheet(s, page, 52, 66, fold=11)
    for z, length in ((47, 26), (34, 33), (21, 21)):
        rule(s, page, 9, z, length, EDGE)
    face_arrow(s, plane, [(81, 39), (105, 39)], BOLD, head=8)
