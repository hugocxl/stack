from geometry import DETAIL, EDGE

DESCRIPTION = "Two identical modules slide together through a visible tongue-and-slot joint."


def module(s, offset, height=17):
    outline = [(0, 0), (48, 0), (48, 10), (36, 10), (36, 30), (48, 30),
               (48, 40), (0, 40), (0, 28), (-11, 28), (-11, 12), (0, 12)]
    for (a, b), (c, d) in zip(outline, outline[1:] + outline[:1]):
        if d - b > c - a:
            s.face([(a + offset, b, 0), (c + offset, d, 0),
                    (c + offset, d, height), (a + offset, b, height)])
    s.face([(x + offset, y, height) for x, y in outline])
    for y in (8, 32):
        s.line([(offset + 7, y, height), (offset + 18, y, height)], DETAIL)


def draw(s):
    module(s, 0)
    module(s, 55)
