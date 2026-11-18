from geometry import BOLD, EDGE
from scenes.redraws._w2 import chart_line, chart_marker, face_arrow, identification_card

DESCRIPTION = "An incoming arrow points to a clipped owner ID card with a large key stamped across its face."


def draw(s):
    def point(x, z):
        return .69*x, -.31*x - .31*z, .88*z

    identification_card(s, point, width=76, height=90, seal=False)
    chart_marker(s, point, 52, 57, 10, EDGE)
    chart_line(s, point, [(44, 51), (24, 37), (24, 45), (30, 49), (30, 55),
                          (35, 53), (42, 58)], EDGE)
    face_arrow(s, point, [(111, 66), (81, 66)], BOLD, head=10)
