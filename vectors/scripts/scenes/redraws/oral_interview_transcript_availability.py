from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import microphone, printed_glyph, sheet

DESCRIPTION = "A checked interview transcript alternates two speaker markers and clock pictograms alongside lines of dialogue."


def draw(s):
    face = sheet(s, w=81, h=95, rise=(-.26, .97))
    microphone(face, 22, 77, 16)
    face.rules(35, 79, [28], ink=BOLD)
    face.rules(35, 72, [23])
    for i, v in enumerate((56, 35, 14)):
        face.oval(16, v, 4.6, 4.6, EDGE)
        printed_glyph(face, "clock", 16, v, 3.6, ink=EDGE)
        x = 29 if i != 1 else 39
        face.rules(x, v + 4, [17], ink=EDGE)
        face.rules(x, v - 2, [36 - (x-29), 27 - (x-29)], gap=5)
    badge(s, "check", *face.point(77, 75, -3), 12)
