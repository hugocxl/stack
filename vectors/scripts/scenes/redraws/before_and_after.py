from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._kit import _strokes
from geometry import project
from scenes.redraws._sf import left_face, plate, screen, squircle

DESCRIPTION = "A standing photo splits down a bold seam into a faint sketch and a finished landscape, with a slider knob."


def draw(s):
    w, h = 120, 80
    face = left_face(0, 0, 0)
    plate(s, face, squircle(w, h, 7), 6, (0, -1, 0))
    m = w/2
    hills = [(8, 18), (30, 44), (46, 28), (60, 40)]
    s.line([face(u, v) for u, v in hills], DETAIL, dashed=True)
    s.line([face(u, v) for u, v in [(60, 40), (76, 54), (94, 32), (112, 46)]], EDGE)
    s.line([face(92 + a, 62 + b) for a, b in oval(0, 0, 6, 6, count=32)], EDGE)
    s.line([face(22 + a, 62 + b) for a, b in oval(0, 0, 6, 6, count=32)], DETAIL, dashed=True)
    s.line([face(m, -6), face(m, h + 6)], BOLD)
    at = screen()
    centre = project(face(m, h/2))
    from scenes.redraws._kit import _screen
    cx, cy, cz = face(m, h/2)
    knob = lambda u, v: _screen(cx, cy + 2, cz, u, v)
    plate(s, knob, oval(0, 0, 11, 11, count=48)[:-1], 3, (0, -1, 0))
    for sign in (-1, 1):
        s.line([knob(sign*2.6, 4.6), knob(sign*7, 0), knob(sign*2.6, -4.6)], BOLD)
