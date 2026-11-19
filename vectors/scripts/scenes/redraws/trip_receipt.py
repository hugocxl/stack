from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws._w5 import train_mark

DESCRIPTION = "A curled trip receipt has a rail pictogram, two itemized fare rows, and a separated total."


def draw(s):
    upper = lambda x, z: (x, -z*.28, z)
    lower = lambda x, z: (x, 9 - z*.78, z)
    s.face([lower(0, 18), lower(50, 18), lower(50, 4),
            *[lower(x, 2 if x % 4 == 0 else 5) for x in range(48, -1, -2)]])
    s.face([upper(0, 18), upper(50, 18), upper(50, 64), upper(0, 64)])
    curl = oval(-20, 62.8, 3.6, 3.5, 19, 292, 24)
    s.line([(50, y, z) for y, z in curl], EDGE)
    s.line([(0, y, z) for y, z in curl[:11]], DETAIL)
    y, z = curl[6]
    s.line([(0, y, z), (50, y, z)], EDGE)
    train_mark(s, upper, 25, 50, .82)
    for z, length in ((29, 18), (23, 13)):
        s.line([upper(6, z), upper(6 + length, z)], DETAIL)
        s.line([upper(35, z), upper(44, z)], EDGE)
    s.line([lower(5, 15), lower(45, 15)], DETAIL)
    s.line([lower(32, 9), lower(44, 9)], BOLD)
