from geometry import BOLD, DETAIL, EDGE, rounded

DESCRIPTION = "A chip card sits in the front reader of an angled checkout terminal."


def draw(s):
    def surface(x, y):
        return x, y, 36 - (y + 34) * 21 / 68

    s.face([(-28, -34, 0), (28, -34, 0), (28, 34, 0), (-28, 34, 0)], EDGE)

    # The front of the card is outside the slot. The terminal masks its inserted end.
    card = rounded(-20, 26, 40, 39, 3)
    s.solid(card, 9, 2, crease=False)
    chip = rounded(-13, 40, 11, 9, 2)
    s.line([(x, y, 11) for x, y in chip + chip[:1]], EDGE)
    s.line([(-13, 44.5, 11), (-2, 44.5, 11)], DETAIL)
    s.line([(4, 49, 11), (14, 49, 11)], DETAIL)
    s.line([(4, 54, 11), (12, 54, 11)], DETAIL)

    s.face([(28, -34, 0), (28, 34, 0), surface(28, 34), surface(28, -34)], EDGE)
    s.face([(-28, 34, 0), (28, 34, 0), surface(28, 34), surface(-28, 34)], EDGE,
           openings=([(-23, 34, 7), (23, 34, 7), (23, 34, 12), (-23, 34, 12)],))
    s.face([surface(x, y) for x, y in ((-28, -34), (28, -34), (28, 34), (-28, 34))], EDGE)
    screen = rounded(-20, -27, 40, 25, 3)
    s.line([surface(x, y) for x, y in screen + screen[:1]], BOLD)
    for y in (-17, -10):
        s.line([surface(-12, y), surface(9 if y == -17 else 3, y)], DETAIL)
    for row in (5, 13, 21):
        for column in (-14, 0, 14):
            key = rounded(column - 4, row, 8, 4.5, 1)
            s.line([surface(x, y) for x, y in key + key[:1]], DETAIL)
