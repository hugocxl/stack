from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._kit import glyph
from scenes.redraws._w3 import Surface

DESCRIPTION = "A text input underlines Japanese composition marks above an attached list of candidates."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.29, .96), back=(0, -.96, -.29))
    face.plate(rounded(0, 0, 92, 72, 5), 9)
    face.rect(7, 49, 78, 16, 3, EDGE)
    # Isolated kana strokes illustrate composition without spelling a word.
    face.stroke([(15, 59), (17, 56)])
    face.stroke([(23, 61), (22, 55), (18, 53)], EDGE)
    face.stroke([(30, 61), (29, 58)])
    face.stroke([(35, 61), (38, 58), (36, 55), (31, 53)], EDGE)
    face.rules(13, 51, [27], ink=BOLD)
    face.stroke([(44, 53), (44, 62)], BOLD)
    face.stroke([(10, 49), (10, 9), (70, 9), (70, 49)], EDGE)
    face.stroke([(10, 36), (70, 36)])
    face.stroke([(10, 23), (70, 23)])
    face.stroke([(16, 45), (25, 45), (25, 39), (16, 39), (16, 45)], EDGE)
    face.stroke([(16, 42), (25, 42)], EDGE)
    face.stroke([(16, 32), (25, 32), (23, 29), (18, 26)], EDGE)
    face.stroke([(16, 17), (25, 17)], EDGE)
    face.stroke([(20, 20), (20, 13), (24, 13)], EDGE)
    for v, width in ((42, 22), (29, 15), (16, 19)):
        face.rules(31, v, [width], ink=DETAIL)
    glyph(s, "check", *face.point(61, 42), 6, BOLD)
