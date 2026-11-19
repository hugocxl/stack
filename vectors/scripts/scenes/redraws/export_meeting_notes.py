from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w2 import face_arrow, rule, speech_bubble
from scenes.redraws.meeting_notes import notes_sheet

DESCRIPTION = "Speaker bubbles label the lines of a transcript as a download arrow leads off its lower corner."


def draw(s):
    point = notes_sheet(s)
    for z, widths in ((48, (45, 33)), (20, (37, 23))):
        def label(x, v):
            return point(x + 12, v + z)

        speech_bubble(s, label, 14, 11, tail=.27, depth=0, ink=EDGE)
        for offset, length in zip((9, 2), widths):
            rule(s, point, 32, z + offset, length, DETAIL)

    face_arrow(s, point, [(88, 42), (99, 42), (107, 35), (107, 1)], BOLD, head=9)
    s.line([point(94, 6), point(94, -7), point(120, -7), point(120, 6)], EDGE)
