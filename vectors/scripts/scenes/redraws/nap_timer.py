from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import coin, glyph
from scenes.redraws._w4 import Surface, bezier_path, printed_glyph

DESCRIPTION = "A twin-bell alarm clock stands beside a rectangular pillow stitched with a crescent moon."


def draw(s):
    far_left, far_right = (-44, -15, 6), (33, -16, 6)
    near_left, near_right = (-44, 31, 6), (36, 29, 6)
    back = bezier_path(far_left, ((-21, -8, 17), (11, -8, 16), far_right))
    side = bezier_path(far_right, ((28, -2, 14), (28, 15, 15), near_right))
    front = bezier_path(near_right, ((17, 23, 17), (-22, 24, 17), near_left))
    end = bezier_path(near_left, ((-37, 19, 12), (-37, -3, 12), far_left))
    seam = bezier_path(near_left, ((-26, 31, 0), (18, 28, 0), near_right))
    s.face([*front, *seam[1:-1]], DETAIL)
    s.face([*back, *side[1:], *front[1:], *end[1:-1]], EDGE)
    s.line(bezier_path(near_right, ((32, 16, 1), (33, -1, 2), far_right)), DETAIL)
    s.line([(-35, 22, 11), (-27, 19, 14), (-20, 18, 15)], DETAIL)
    s.line([(28, -9, 10), (21, -5, 15), (14, -4, 16)], DETAIL)
    pillow = Surface(s, lambda u, v: (u, v, 15))
    printed_glyph(pillow, "moon", -11, 6, 13, EDGE)

    x, y, z = 46, 29, 26
    for dx in (-13, 13):
        s.tube([(x + dx*.77, y - 4, 12), (x + dx, y - 2, 1)], 2)
        s.tube([(x + dx*.75, y - 6, 38), (x + dx, y - 6, 48)], 1.6)
        bell = oval(x + dx, y - 6, 8, 6)[:-1]
        crown = oval(x + dx, y - 6, 5, 3.8)[:-1]
        s.solid(bell, 47, 6, crown)
    face = coin(s, x, y, z, 21, depth=11)
    s.line([(u, face, v) for u, v in oval(x, z, 16.5, 16.5)], DETAIL)
    glyph(s, "clock", x, face, z, 15)
