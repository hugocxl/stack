from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import currency_mark, standing_card

DESCRIPTION = "A standing quote request form has a currency amount field and an outward send arrow badge."


def draw(s):
    form = standing_card(s, 81, 83, angle=-23, lean=.57, depth=6)
    form.rows(11, 68, (43,), ink=EDGE)
    form.rows(11, 56, (58, 42), step=-9)
    form.frame(11, 13, 52, 23, 3, EDGE)
    currency_mark(form, 24, 24)
    form.rows(36, 21, (17,))
    badge(s, "arrow", *form.at(71, 27), 15)
