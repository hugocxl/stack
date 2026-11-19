from geometry import DETAIL, oval, rounded
from scenes.redraws._kit import glyph

DESCRIPTION = "An insulated carrier cradles a lidded drink in a recessed cup holder and has an outward arrow on its front."


def draw(s):
    s.box(1, 1, 0, 48, 35, 25, 4)
    s.tube([(9, 5, 24), (9, 5, 42), (14, 5, 47),
            (34, 5, 47), (39, 5, 42), (39, 5, 24)], 1.9)
    s.face([(x, y, 25) for x, y in rounded(0, 0, 50, 37, 3)],
           openings=[[(x, y, 25) for x, y in oval(25, 21, 12, 11)[:-1]]])
    s.solid(oval(25, 21, 7, 6)[:-1], 25, 7,
            top=oval(25, 21, 8.5, 7.5)[:-1], crease=False)
    s.disk(25, 21, 32, 9.5, 8.5, 2)
    s.ellipse(25, 21, 34, 5, 4.5, DETAIL, 135, 225)
    s.line([(4, 36, 20), (46, 36, 20)], DETAIL)
    glyph(s, "arrow", 26, 36, 10, 13)
