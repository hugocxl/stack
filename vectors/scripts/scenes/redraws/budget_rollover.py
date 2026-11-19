from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import calendar_header, ledger_rows, money_coin, open_ledger, printed_stroke, rect

DESCRIPTION = "An open budget ledger carries a dollar coin and an arrow from one calendar month to the next."


def draw(s):
    left, right = open_ledger(s)
    for page, x in ((left, 8), (right, 48)):
        calendar_header(s, lambda u, v: page(u, 20 - v), x, 1, 1.05)
        printed_stroke(s, page, [(x + 20, 13), (x + 29, 13)], EDGE)
    ledger_rows(s, left, 8, rows=(26, 32, 38))
    printed_stroke(s, left, [(8, 44), (37, 44)], EDGE)
    rect(s, right, 55, 26, 23, 13, 1.4, EDGE)
    printed_stroke(s, right, [(61, 32.5), (73, 32.5)], DETAIL)
    arrow(s, [left(24, 50), left(42, 48), right(47, 41), right(50, 35), right(54, 33)], BOLD, head=5.7)
    x, y, z = left(14, 53)
    money_coin(s, x, y + 5, z + 1, 9.5)
