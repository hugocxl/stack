from scenes.redraws._kit import badge
from scenes.redraws.replace_file_failed import file_page

DESCRIPTION = "A folded file carries an X badge at its lower-right corner."


def draw(s):
    page = file_page(s)
    for z, width in ((48, 20), (35, 33), (25, 26)):
        page.line([(11, z), (11 + width, z)])
    badge(s, "x", *page.point(54, 5), 12)
