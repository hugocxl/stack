from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import printed_check, sheet, vial_art

DESCRIPTION = "A laboratory quiz with a specimen-vial heading carries a check badge beside its answer rows."


def draw(s):
    face = sheet(s, 78, 94, rise=(-.34, .94), depth=6)
    vial_art(face, 22, 68, 29)
    face.rules(36, 72, [22], ink=EDGE)
    face.rules(36, 62, [28])
    for v, width in ((42, 32), (30, 37), (18, 23)):
        face.rules(13, v, [width], ink=EDGE)
        face.rect(53, v - 4, 8, 8, 1)
    printed_check(face, 57, 42, 4)
    badge(s, "check", *face.point(80, 27), 15)
