from geometry import BOLD, EDGE, oval, rounded
from scenes.redraws._w2 import chart_line, closed_outline, rule, speech_bubble

DESCRIPTION = "A prominent at sign sits directly before a selected name chip inside a comment composer."


def draw(s):
    def point(x, z):
        return .77*x, -.23*x - .18*z, z

    speech_bubble(s, point, 113, 62, depth=7)
    closed_outline(s, point, rounded(13, 25, 86, 25, 8), EDGE)
    s.line([point(x, z) for x, z in oval(28, 37, 8.4, 8.4, 1, 313, 40)], BOLD)
    s.line([point(x, z) for x, z in oval(28, 37, 3.3, 3.8, count=24)], BOLD)
    chart_line(s, point, [(31.3, 40.2), (31.3, 35.3), (32.5, 33.7),
                          (34.3, 33.7), (35.7, 35.1), (36.4, 37.2)], BOLD)
    rule(s, point, 44, 37, 41, EDGE)
    rule(s, point, 14, 14, 58)
    rule(s, point, 78, 14, 11)
