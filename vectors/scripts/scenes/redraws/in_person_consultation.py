from geometry import DETAIL
from scenes.redraws.boardroom_reservation import office_chair

DESCRIPTION = "Two chairs face each other across a consultation desk with an inset writing panel."


def draw(s):
    office_chair(s, 5, -24, facing_near=True, arms=True)
    s.box(0, 4, 0, 4, 38, 34, 1)
    s.box(42, 4, 0, 4, 38, 34, 1)
    s.box(4, 10, 16, 38, 3, 18, .5, DETAIL)
    s.box(-2, 2, 34, 50, 42, 5, 2)
    s.line([(5, 10, 39), (32, 10, 39), (32, 32, 39),
            (5, 32, 39), (5, 10, 39)], DETAIL)
    s.line([(18, 10, 39), (18, 32, 39)], DETAIL)
    for y in (16, 21, 26):
        s.line([(8, y, 39), (15, y, 39)], DETAIL)
        s.line([(21, y, 39), (29, y, 39)], DETAIL)
    office_chair(s, 18, 46, facing_near=False)
