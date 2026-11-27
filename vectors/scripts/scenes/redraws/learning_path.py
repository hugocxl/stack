from geometry import DETAIL, EDGE
from scenes.redraws._sf import smooth

DESCRIPTION = "A winding path links three round milestones on the ground to a finish flag."


def draw(s):
    stops = [(-44, 26), (-14, -12), (18, 18), (44, -16)]
    path = smooth([(-66, 50), *stops], 12)
    s.line([(x, y, 0) for x, y in path], DETAIL, dashed=True)
    for x, y in stops[:3]:
        s.disk(x, y, 0, 11, 11, 5)
        s.ellipse(x, y, 5, 6.5, 6.5, DETAIL)
    x, y = stops[3]
    s.disk(x, y, 0, 11, 11, 5)
    s.tube([(x, y, 5), (x, y, 66)], 1.6, EDGE)
    s.face([(x, y, 65), (x + 24, y - 24, 57), (x, y, 49)], EDGE)
