from geometry import DETAIL, EDGE
from scenes.redraws._w5 import ticket_face, train_mark
from scenes.redraws.hotel_search import magnifier

DESCRIPTION = "A magnifying glass enlarges the barcode on the stub of a notched rail ticket."


def draw(s):
    face = ticket_face(s)
    train_mark(s, face, 23, 21, 1.24)
    for z, w in ((16, 16), (23, 20)):
        s.line([face(40, z), face(40 + w, z)], DETAIL)
    x, z, r = 83, 24, 12
    y = -z*.54 + 5
    magnifier(s, x, y, z, r)
    for a, h in ((78, 11), (81, 14), (85, 14), (88, 10)):
        s.line([(a, y, z - h*.5), (a, y, z + h*.5)], EDGE)
