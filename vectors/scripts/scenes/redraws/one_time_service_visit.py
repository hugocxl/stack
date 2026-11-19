from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w4 import desk_calendar, printed_glyph

DESCRIPTION = "A wire-bound service calendar has a van in its heading and one outlined appointment date."


def van_pictogram(face, u, v):
    """Print a cab, cargo roof, and two wheels in a calendar heading."""
    face.outline([(u, v+2), (u, v+14), (u+19, v+14), (u+23, v+10),
                  (u+27, v+8), (u+29, v+5), (u+29, v+2)], EDGE)
    face.line([(u+19, v+13), (u+19, v+8), (u+26, v+8)], DETAIL)
    for x in (u+6, u+23):
        wheel = oval(x, v+1, 2.5, 2.5, count=24)
        face.scene.face([face.at(a, b) for a, b in wheel], EDGE)


def draw(s):
    calendar = desk_calendar(s, reserved={(2, 1)})
    van_pictogram(calendar, 32, 63)
    calendar.frame(40, 22, 16, 15, 2, BOLD)
    printed_glyph(calendar, "dot", 48, 29.5, 8.5, EDGE)
