from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph, typeset_a

DESCRIPTION = "An arrow leads from an empty glyph square on one piece of type to a capital A on another."


def draw(s):
    type_faces = Surface(s, (0, 0, 0), rise=(-.28, .96), back=(0, -.96, -.28),
                         across=(.64, -.77))
    for x in (0, 78):
        block = Surface(s, type_faces.point(x, 0), rise=type_faces.rise, back=type_faces.back,
                        across=type_faces.across)
        block.plate(rounded(0, 0, 39, 47, 3), 17)
        if x == 0:
            block.rect(9, 11, 21, 25, 0, EDGE)
        else:
            typeset_a(block, 9, 11, 29)
    printed_glyph(type_faces, "arrow", 62, 23, 10, BOLD)
