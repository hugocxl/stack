from shapely.affinity import affine_transform

from geometry import DETAIL, EDGE, Scene
from scenes.redraws._w4 import open_book

DESCRIPTION = "An open book rests on the sloped top of a freestanding reading lectern."


def draw(s):
    s.box(15, 9, 0, 97, 51, 7, 4)
    s.box(46, 25, 7, 34, 20, 90, 2)
    s.box(42, 22, 91, 42, 26, 9, 2)

    slope = .40
    height = 119
    width = 130
    rear, front = -3, 79

    def top(x, y):
        return x, y, height - slope*y

    s.face([top(width, rear), top(width, front),
            (width, front, height - 36), (width, rear, height - 6)])
    s.face([top(-4, front), top(width, front),
            (width, front, height - 36), (-4, front, height - 36)])
    s.face([top(-4, rear), top(width, rear), top(width, front), top(-4, front)])

    book = Scene()
    left, right = open_book(book)
    left.rows(11, 15, (28,), ink=EDGE)
    left.rows(11, 26, (43, 36, 44, 33, 40), step=7)
    right.rows(74, 16, (41, 35, 41, 38, 39, 28), step=7)
    # Shear the projected book so its cover follows the lectern's incline.
    transform = (1, 0, -slope/2, 1 + slope, 0, -.8660254*height)
    for path, mask, ink in book.layers:
        s.layers.append((affine_transform(path, transform),
                         affine_transform(mask, transform) if mask is not None else None, ink))
    s.line([(-1, front, height - 30), (127, front, height - 30)], EDGE)
    s.line([(4, front, height - 34), (122, front, height - 34)], DETAIL)
