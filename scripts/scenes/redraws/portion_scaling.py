from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import arrow

DESCRIPTION = "A graduated measuring jug has an upward arrow alongside its volume scale."


def draw(s):
    x, y = 25, 23
    s.tube([(45, 22, 42), (56, 22, 42), (61, 22, 36),
            (61, 22, 21), (54, 22, 15), (44, 22, 15)], 2.1)
    lower = oval(x, y, 17, 15)[:-1]
    upper = [(a, b) for a, b in oval(x, y, 22, 20, -153, 153, count=48)]
    upper.extend([(3, 32), (-7, 28), (-7, 24), (2, 16)])
    s.solid(lower, 0, 49, top=upper, crease=False)
    s.face([(a, b, 49) for a, b in upper],
           openings=[[(a, b, 49) for a, b in oval(x, y, 18, 16)[:-1]]])
    for z, end in ((9, 58), (17, 69), (25, 59), (33, 69), (41, 58)):
        fraction = z/49
        s.ellipse(x, y, z, 17+5*fraction, 15+5*fraction, EDGE, 30, end)
    arrow(s, [(25, 39, 9), (25, 42, 36)], BOLD, head=6)
