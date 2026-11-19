from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, flat, printed_glyph, ticket_outline

DESCRIPTION = "A perforated event response card with a row of stars slips into a feedback box."


def draw(s):
    s.box(0, 0, 0, 86, 55, 38, 4)
    flat(s, 0, 55, 38).rect(12, 19, 61, 11, 3, BOLD)
    front = Surface(s, (0, 55, 0))
    front.rect(29, 8, 28, 19, 2, EDGE)
    front.rules(35, 18, [16], ink=EDGE)
    ballot = Surface(s, (14, 29, 38), rise=(-.26, .97), back=(0, -.97, -.26))
    ballot.plate(rounded(0, 0, 57, 45, 2), 2)
    ballot.stroke([(6 + x * .43, 28 + v * .23) for x, v in ticket_outline()],
                  EDGE, closed=True)
    for x in (11, 28, 45):
        printed_glyph(ballot, "star", x, 16, 7.5)
