from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w2 import chart_line, chart_marker, closed_outline, rule, upright_face

DESCRIPTION = "A prompt editor shows two prompt lines above a landscape thumbnail and a paperclip."


def draw(s):
    def point(x, z):
        return .73*x, -.27*x - .30*z, z

    upright_face(s, point, rounded(0, 0, 111, 85, 6), 9)
    closed_outline(s, point, rounded(8, 8, 95, 69, 3), DETAIL)
    rule(s, point, 16, 66, 69, EDGE)
    rule(s, point, 16, 56, 42, EDGE)
    chart_line(s, point, [(8, 46), (103, 46)], DETAIL)
    s.face([point(x, z) for x, z in rounded(16, 13, 47, 28, 2)], EDGE)
    chart_marker(s, point, 50, 33, 4, EDGE)
    chart_line(s, point, [(16, 21), (29, 34), (39, 24), (45, 28), (63, 19)], EDGE)
    chart_line(s, point, [(86, 33), (79, 25), (79, 22), (81, 21), (84, 22),
                          (94, 33), (94, 36), (91, 37), (88, 36), (77, 24),
                          (76, 20), (79, 17), (83, 17), (87, 20), (95, 29)], EDGE)
