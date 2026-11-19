from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w3 import Surface, pen_on

DESCRIPTION = "A pencil crosses the ruled page of a tilted editing pad with a check badge on its lower corner."


def edit_marks(page, scale=1):
    page.rules(11 * scale, 65 * scale, [27 * scale], ink=EDGE)
    page.rules(11 * scale, 53 * scale, [n * scale for n in (48, 42, 36, 45, 30)],
               gap=8 * scale)
    pen_on(page, 31 * scale, 22 * scale, 43 * scale, pencil=True)


def edited_document(s):
    """Draw the edited page on its inclined backing."""
    pad = Surface(s, (0, 34, 0), rise=(-.67, .74), back=(0, -.74, -.67))
    pad.plate(rounded(0, 0, 78, 84, 4), 7)
    page = Surface(s, pad.point(3, 4, -.8), rise=pad.rise, back=pad.back)
    page.plate(rounded(0, 0, 72, 77, 3), 1.4)
    edit_marks(page)
    return page


def draw(s):
    page = edited_document(s)
    badge(s, "check", *page.point(70, 10, -4), 15)
