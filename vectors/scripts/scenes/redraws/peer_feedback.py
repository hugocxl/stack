from geometry import DETAIL, EDGE
from scenes.redraws._w3 import Surface, sheet, speech_outline

DESCRIPTION = "Two overlapping speech bubbles sit along the edge of an assignment with marked answers."


def conversation(face, x, v, w, h, *, depth=2, lines=2):
    """Attach a speech balloon with a short tail to the local face."""
    face.plate(speech_outline(x, v, w, h), depth)
    widths = [w * .64, w * .43][:lines]
    face.rules(x + w * .18, v + h * .66, widths, gap=h * .24, ink=EDGE)


def draw(s):
    page = sheet(s, 73, 84, rise=(-.61, .79))
    page.rules(9, 72, [32], ink=EDGE)
    for v, width in ((54, 30), (37, 23), (20, 26)):
        page.oval(14, v, 3.8, 3.8, EDGE)
        if v != 37:
            page.rules(12, v, [4], ink=EDGE)
        page.rules(24, v, [width], ink=DETAIL)

    back = Surface(s, page.point(56, 45, -2), rise=page.rise, back=page.back)
    conversation(back, 0, 0, 41, 26, lines=1)
    front = Surface(s, page.point(42, 17, -6), rise=page.rise, back=page.back)
    conversation(front, 0, 0, 47, 27)
