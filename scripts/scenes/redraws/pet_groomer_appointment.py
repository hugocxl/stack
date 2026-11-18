from geometry import EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface

DESCRIPTION = "A paw-printed pet bowl sits beside grooming scissors with a clock badge attached to the bowl."


def draw(s):
    s.solid(oval(-18, -5, 35, 29)[:-1], 0, 22, oval(-18, -5, 26, 22)[:-1])
    s.ellipse(-18, -5, 22, 22, 18, EDGE)
    s.ellipse(-18, -5, 18, 19, 15, start=195, end=347)
    front = Surface(s, lambda u, v: (-5 + u*.707, 13 - u*.707, v))
    front.oval(0, 7, 5, 3.5, EDGE)
    for u, v in ((-7, 11), (-3, 15), (3, 15), (7, 11)):
        front.oval(u, v, 1.6, 1.8, EDGE)

    scissors = Surface(s, lambda u, v: (27 + .39*u + .92*v, 61 - .92*u + .39*v, 4))
    outline = [(-40, -10), (-38, -17), (-31, -21), (-22, -20),
               (-15, -15), (-12, -8), (-3, -5), (32, -17), (38, -16),
               (6, -1), (36, 13), (30, 15), (-3, 5), (-13, 10),
               (-16, 17), (-24, 22), (-33, 21), (-39, 16), (-41, 10),
               (-38, 4), (-31, 0), (-38, -4)]
    s.face([scissors.at(u, v) for u, v in outline], EDGE, openings=[
        [scissors.at(u, v) for u, v in oval(-27, center, 8, 5.5)[:-1]]
        for center in (-11, 12)
    ])
    scissors.oval(-2, 0, 2.2, 2.2, EDGE)
    badge(s, "clock", -9, -22, 28, 12)
