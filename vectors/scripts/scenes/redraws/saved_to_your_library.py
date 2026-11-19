from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w5 import cupboard_shell, cupboard_trim, rect

DESCRIPTION = "A bookshelf holds a row of volumes with one book partly pushed into its slot and a check badge on the shelf."


def draw(s):
    cupboard_shell(s, 59, 27, 53)
    s.box(9, 4, 3, 15, 19, 37, 1)
    for z in (10, 34):
        s.line([(11, 23, z), (22, 23, z)])
    cupboard_trim(s, 59, 27, 53)
    # The new book still protrudes from the shelf at the same floor height.
    s.box(29, 15, 3, 15, 25, 42, 1)
    pages = [(31, 17, 45), (42, 17, 45), (42, 37, 45), (31, 37, 45)]
    s.line(pages + pages[:1])

    def spine(x, z):
        return x, 40, z

    rect(s, spine, 33, 28, 7, 9, 1, EDGE)
    s.line([spine(31, 12), spine(42, 12)])
    badge(s, "check", 56, 8, 48, 12)
