from geometry import BOLD, EDGE

DESCRIPTION = "An open breaker lever lifts away from one of two contacts in a single circuit."


def draw(s):
    s.tube([(-20, 8, 6), (-39, 8, 6), (-39, -27, 6), (39, -27, 6),
            (39, 8, 6), (21, 8, 6)], 2.5, EDGE)
    for x in (-20, 21):
        s.disk(x, 8, 4, 6, 6, 6)
    s.disk(-20, 8, 10, 4, 4, 5)
    s.tube([(-20, 8, 14), (12, 8, 58)], 3.5, BOLD)
    s.ellipse(21, 8, 10, 3, 3, EDGE)
