from geometry import EDGE
from scenes.redraws._kit import warning
from scenes.redraws.replace_file_failed import file_page

DESCRIPTION = "A folded document with a pencil across its lower half carries a warning triangle."


def pencil(page):
    """An editing pencil set diagonally across the lower corner of a page."""
    u, v = 26, 14
    cosine, sine = .86, .51

    def point(along, across):
        return (u + along * cosine - across * sine,
                v + along * sine + across * cosine)

    body = [point(a, b) for a, b in [(0, 0), (10, -4), (41, -4), (44, -2),
                                      (44, 2), (41, 4), (10, 4)]]
    page.plate(body, 3)
    for along in (10, 35):
        page.line([point(along, -4), point(along, 4)], EDGE)
    page.line([point(10, 0), point(35, 0)])


def edited_document(s):
    page = file_page(s)
    for z, width in ((49, 21), (37, 33), (26, 16)):
        page.line([(10, z), (10 + width, z)])
    pencil(page)
    return page


def draw(s):
    page = edited_document(s)
    x, y, z = page.point(56, 52)
    warning(s, x + 11, y - 1, z - 7, 31)
