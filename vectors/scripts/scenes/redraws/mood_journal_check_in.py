from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import open_book
from scenes.redraws.evening_routine import printed_glyph
from scenes.redraws.hydration_history import date_mark

DESCRIPTION = "An open mood journal records a dated check-in with a heart in a thought bubble and a rating slider."


def draw(s):
    left, right = open_book(s)
    date_mark(left, 12, 12, 1.15)
    left.rows(29, 13, (21,))
    left.outline([(15, 38), (16, 34), (19, 31), (24, 30), (28, 26), (34, 25),
                  (40, 27), (43, 31), (48, 32), (51, 36), (51, 41),
                  (48, 45), (43, 46), (38, 50), (32, 50), (27, 47),
                  (21, 47), (17, 44)], EDGE)
    left.oval(21, 53, 2.7, 2.7, EDGE)
    left.oval(16, 59, 1.7, 1.7, DETAIL)
    printed_glyph(left, "heart", 33, 37, 12, BOLD, down=True)
    right.rows(73, 14, (33, 25), step=7, ink=EDGE)
    right.rows(73, 32, (37, 33, 37, 25), step=7, ink=DETAIL)
    right.frame(73, 59, 38, 6, 2)
    right.oval(102, 62, 3, 3, EDGE)
