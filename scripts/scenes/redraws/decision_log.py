from geometry import DETAIL, EDGE
from scenes.redraws._w2 import open_volume, printed_glyph, rule

DESCRIPTION = "An open ruled logbook pairs checked entries with short date fields along its outer columns."


def draw(s):
    left, right = open_volume(s)
    for point, side in ((left, -1), (right, 1)):
        rule(s, point, 8, 56, 31, EDGE)
        for z, length in ((42, 15), (28, 19), (14, 12)):
            rule(s, point, 5, z - 5, 46, DETAIL)
            check = 45 if side == -1 else 11
            content = 18 if side == -1 else 21
            date = 7 if side == -1 else 45
            def reading_order(x, v):
                return point(check + side*x, z + v)

            printed_glyph(s, reading_order, "check", 0, 0, 5.5, EDGE)
            rule(s, point, content, z, length, EDGE)
            rule(s, point, date, z, 5, DETAIL)
