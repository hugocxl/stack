from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w4 import front_surface, upright

DESCRIPTION = "A hook-handled walking cane and an adjustable underarm crutch stand alongside a short fitting ruler."


def draw(s):
    angle = -35
    plane = front_surface(s, angle=angle)

    def rod(points, radius):
        s.tube([plane.at(u, v) for u, v in points], radius)

    rod([*oval(-28, 92, 10, 11, 0, 177, 24)[::-1],
         (-18, 63), (-19, 35), (-20, 7)], 3)
    rod([(-20, 4), (-20, 10)], 4.3)

    rod([(24, 8), (21, 45)], 3.1)
    rod([(24, 4), (24, 10)], 4.5)
    rod([(15, 98), (14, 71), (17, 53), (21, 47),
         (26, 52), (31, 71), (33, 98)], 3)
    rod([(14, 75), (31, 75)], 3.4)
    upright(s, rounded(10, 96, 28, 10, 4), 7, 12, angle=angle)
    face = front_surface(s, angle=angle, y=2)
    for v in (21, 29, 37):
        face.line([(20.5 + (45 - v)*.08, v), (23 + (45 - v)*.08, v)], EDGE)

    ruler = front_surface(s, angle=-17, y=10)
    outline = [(27, 0), (38, 0), (52, 44), (41, 47)]
    ruler.slab(outline, 3)
    for i in range(1, 8):
        u, v = 27 + 1.75*i, 5.5*i
        ruler.line([(u, v), (u + (6 if i % 2 else 4), v - 1.4)], DETAIL)
