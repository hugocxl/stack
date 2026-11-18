from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, photo_art, printed_glyph

DESCRIPTION = "A standing landscape photo frame carries a corner control with two opposing arrows."


def draw(s):
    frame = Surface(s, (0, 0, 0), rise=(-.43, .9), back=(0, -.9, -.43),
                    across=(.71, -.70))
    support = Surface(s, frame.point(53, 0, 9), rise=frame.rise,
                      back=frame.back, across=frame.across)
    s.face([support.point(17, 47), support.point(34, 22.5, 38),
            support.point(19, 22.5, 38), support.point(4, 47)], EDGE)
    frame.plate(rounded(0, 0, 100, 71, 6), 7)
    photo_art(frame, 10, 10, 81, 50)
    control = Surface(s, frame.point(72, 53, -4), rise=frame.rise, back=frame.back,
                      across=frame.across)
    control.plate(rounded(0, 0, 37, 29, 5), 4)
    printed_glyph(control, "arrow", 18.5, 19.5, 13.5, BOLD)
    printed_glyph(control, "back", 18.5, 9.5, 13.5, BOLD)
