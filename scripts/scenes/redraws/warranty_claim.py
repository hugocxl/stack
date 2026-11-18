from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import printed_glyph, standing_card

DESCRIPTION = "A framed warranty certificate has a star seal and an incoming arrow badge at its upper corner."


def draw(s):
    certificate = standing_card(s, 93, 70, angle=-28, depth=8, lean=.34)
    certificate.frame(6, 6, 81, 58, 3)
    certificate.rows(17, 52, (49,), ink=EDGE)
    certificate.rows(19, 39, (29, 25, 20), step=-8)
    certificate.line([(61, 22), (57, 11), (65, 14), (72, 10), (69, 22)], EDGE)
    certificate.oval(65, 29, 10, 10, EDGE)
    printed_glyph(certificate, "star", 65, 29, 9, EDGE)
    badge(s, "back", *certificate.at(91, 58), 15)
