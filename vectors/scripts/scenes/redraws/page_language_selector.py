from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph

DESCRIPTION = "A browser language menu shows a Latin and a Japanese script sample with one selected check."


def draw(s):
    face = Surface(s, (0, 0, 0))
    face.plate(rounded(0, 0, 94, 71, 5), 10)
    face.stroke([(0, 57), (94, 57)], EDGE)
    for x in (8, 14, 20):
        face.oval(x, 64, 1.3, 1.3, EDGE)
    face.rect(17, 7, 60, 44, 3, EDGE)
    face.stroke([(17, 36), (77, 36)], EDGE)
    face.stroke([(17, 21), (77, 21)])
    face.oval(28, 44, 4.5, 4.5, EDGE)
    face.oval(28, 44, 2, 4.5)
    face.rules(24, 44, [8])
    face.rules(38, 44, [20])
    printed_glyph(face, "down", 68, 44, 4, EDGE)

    # One isolated letter from each of the two writing systems.
    face.stroke([(25, 25), (29, 33), (33, 25)], BOLD)
    face.rules(27, 28, [4], ink=BOLD)
    face.rules(39, 29, [17])
    face.stroke([(25, 17), (32, 17)], EDGE)
    face.stroke([(28, 19), (27, 15), (28, 11)], EDGE)
    face.stroke([(31, 15), (29, 12), (26, 11), (25, 13), (28, 15),
                 (32, 15), (33, 13), (31, 11)], EDGE)
    face.rules(39, 14, [14])
    printed_glyph(face, "check", 68, 29, 7, BOLD)
