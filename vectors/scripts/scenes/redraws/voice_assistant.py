from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w2 import chart_line, closed_outline, speech_bubble

DESCRIPTION = "A dimensional speech bubble holds a large microphone capsule with a curved yoke and stand."


def draw(s):
    def point(x, z):
        return .63*x, -.37*x, z

    speech_bubble(s, point, 102, 72, tail=.27, depth=8)
    closed_outline(s, point, rounded(42, 32, 18, 27, 9), BOLD)
    chart_line(s, point, [(35, 41), *oval(51, 36, 16, 13, 180, 360, 28), (67, 41)], EDGE)
    chart_line(s, point, [(51, 23), (51, 13)], EDGE)
    chart_line(s, point, [(41, 13), (61, 13)], EDGE)
    for z in (43, 48):
        chart_line(s, point, [(43, z), (48, z)], DETAIL)
