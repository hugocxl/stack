from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, chart_marker, upright_face

DESCRIPTION = "An image tile shows a stepped pixel edge turning into a smooth curve with two square Bézier anchors."


def draw(s):
    def point(x, z):
        return .68*x, -.32*x - .23*z, z

    upright_face(s, point, rounded(0, 0, 103, 72, 5), 9)
    stairs = [(11, 19), (22, 19), (22, 28), (33, 28), (33, 37), (44, 37)]
    chart_line(s, point, stairs, BOLD)
    controls = ((44, 37), (58, 37), (71, 58), (90, 58))
    curve = []
    for i in range(25):
        t = i/24
        v = 1 - t
        weights = (v**3, 3*v*v*t, 3*v*t*t, t**3)
        curve.append(tuple(sum(weight*coord for weight, coord in zip(weights, axis))
                           for axis in zip(*controls)))
    chart_line(s, point, curve, BOLD)
    for anchor, handle in ((controls[0], controls[1]), (controls[3], controls[2])):
        chart_line(s, point, [anchor, handle], DETAIL)
        chart_marker(s, point, *handle, 1.5, EDGE)
        x, z = anchor
        s.face([point(a, b) for a, b in rounded(x - 3, z - 3, 6, 6, .5)], EDGE)
