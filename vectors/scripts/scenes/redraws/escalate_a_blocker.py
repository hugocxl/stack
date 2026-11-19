from geometry import BOLD, DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_marker, printed_glyph, request_card, rule

DESCRIPTION = "A tabbed task card with a blocked symbol carries an upward arrow badge on its upper corner."


def draw(s):
    def point(x, z):
        return .76*x, -.24*x - .43*z, .85*z

    request_card(s, point, 92, 73, print_rows=False)
    chart_marker(s, point, 30, 34, 13, BOLD)
    printed_glyph(s, point, "slash", 30, 34, 10, BOLD)
    for z, length in ((40, 19), (28, 25)):
        rule(s, point, 51, z, length, DETAIL)
    badge(s, "up", *point(92, 65), 14)
