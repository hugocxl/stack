from geometry import BOLD, rounded
from scenes.redraws._w5 import panel, printed_stroke, rect

DESCRIPTION = "A folded tabletop tent displays a large square QR pattern."


def draw(s):
    face = lambda x, z: (x, 15 - .47 * z, z)
    left, right = face(0, 55), face(50, 55)
    s.face([(0, -28, 0), (50, -28, 0), right, left])
    s.face([(50, -28, 0), face(50, 0), right])
    panel(s, rounded(0, 0, 50, 55, 1.5), face, 2.8)
    for x, z in ((8, 30), (29, 30), (8, 9)):
        rect(s, face, x, z, 13, 13, .4, BOLD)
        rect(s, face, x + 4, z + 4, 5, 5, .18, BOLD)
    for shape in (
        [(25, 36), (25, 42)],
        [(25, 12), (25, 24), (32, 24), (32, 19), (41, 19), (41, 25)],
        [(29, 9), (35, 9), (35, 14), (42, 14), (42, 9)],
        [(8, 26), (16, 26), (16, 22)],
        [(35, 27), (39, 27)],
    ):
        printed_stroke(s, face, shape, BOLD)
