from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws.express_train_ticket import ticket

DESCRIPTION = "A boarding pass shows an airplane and a curved arrow connecting two airport markers."


def airplane(s, x, y, z, scale, *, vertical=False):
    outline = [(16, 0), (13, -2), (4, -2.4), (-3, -12), (-7, -12), (-3, -2.5),
               (-11, -2.5), (-14, -6), (-17, -6), (-15, 0), (-17, 6), (-14, 6),
               (-11, 2.5), (-3, 2.5), (-7, 12), (-3, 12), (4, 2.4), (13, 2)]
    if vertical:
        s.face([(x + a * scale, y, z + b * scale) for a, b in outline], EDGE)
    else:
        s.face([(x + a * scale, y + b * scale, z) for a, b in outline], EDGE)


def draw(s):
    ticket(s, 89, 53)
    z = 2.5
    airplane(s, 33, 16, z, .65)
    for x in (12, 59):
        s.ellipse(x, 36, z, 4.6, 4.6, EDGE)
    path = oval(35.5, 38, 19, 10, 187, 353, 30)
    arrow(s, [(x, y, z) for x, y in path], head=4.8)
    for x, y, h in ((77, 12, 28), (80, 13, 23), (83, 12, 28)):
        s.line([(x, y, z), (x, y + h, z)], DETAIL)
