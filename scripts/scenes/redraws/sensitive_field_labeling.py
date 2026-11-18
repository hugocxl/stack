from geometry import EDGE, oval
from scenes.redraws._w5 import field_dots, field_form, panel

DESCRIPTION = "A clipped classification tag sits at the end of the label above a masked form field."


def draw(s):
    face = field_form(s)
    field_dots(s, face)
    tag = lambda x, z: (x, face(x, z)[1] + 4, z)
    outline = [(30, 38), (37, 43), (55, 43), (55, 33), (37, 33)]
    panel(s, outline, tag, 2, EDGE)
    s.line([tag(x, z) for x, z in oval(37, 38, 1.35, 1.35, count=20)], EDGE)
    s.line([tag(43, 38), tag(50, 38)], EDGE)
    s.line([face(26, 35), tag(29, 37), tag(36, 38)], EDGE)
