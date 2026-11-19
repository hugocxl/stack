from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A pricing calculator brackets two fractional digit positions after a prominent decimal point."


def draw(s):
    face = Surface(s, (0, 0, 5), rise=(-.64, .77), back=(0, -.77, -.64))
    s.face([(116, 0, 0), face.point(116, 0), face.point(116, 78),
            (116, -55, 61), (116, -55, 0)])
    s.face([(0, 0, 0), (116, 0, 0), face.point(116, 0), face.point(0, 0)])
    face.plate(rounded(0, 0, 116, 78, 5), 8)
    face.rect(7, 30, 102, 40, 4, EDGE)
    place = face.viewer_axes(24, 49)
    for v in (-3, 3):
        face.stroke([place(-5, v), place(3, v)], BOLD)
    face.stroke([place(x, v) for x, v in oval(0, 0, 7, 10, 53, 307, 28)], BOLD)
    for x in (40, 55, 77, 93):
        face.stroke([(x, 57), (x, 43), (x + 9, 43), (x + 9, 57)])
    face.oval(69, 44, 1.6, 1.6, EDGE)
    face.stroke([(75, 40), (75, 36), (104, 36), (104, 40)], EDGE)
    for x in (13, 33, 53, 73, 93):
        face.rect(x, 9, 11, 12, 3)
