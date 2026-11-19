from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, printed_glyph, speech_outline, ticket_outline, wheelchair

DESCRIPTION = "An open volunteer field guide lists three roles beside ticket, speech bubble and wheelchair pictograms."


def draw(s):
    # A short back cover supports the open guide on its lower edge.
    s.face([(0, 0, 2), (27, -17, 2), (27, -29, 79), (0, -21, 79)], EDGE)
    page = Surface(s, (0, 0, 2), rise=(-.25, .97), back=(0, -.97, -.25))
    page.plate(rounded(0, 0, 98, 80, 5), 4)
    page.stroke([(12, 4), (12, 76)], EDGE)
    printed_glyph(page, "heart", 22, 69, 7)
    page.rules(33, 69, [42], ink=EDGE)

    ticket = [(20 + x * .20, 48 + v * .24) for x, v in ticket_outline()]
    page.stroke(ticket, EDGE, closed=True)
    page.stroke(speech_outline(20, 28, 21, 13), EDGE, closed=True)
    wheelchair(page, 30, 16, 13, EDGE)
    for v, width in ((54, 34), (34, 26), (16, 33)):
        page.rules(50, v, [width], ink=EDGE)
        page.rules(50, v - 5, [width - 9])
