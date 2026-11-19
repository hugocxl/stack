from geometry import DETAIL, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws.flight_connection_help import airplane
from scenes.redraws.garage_vacancy_queue import post

DESCRIPTION = "Two upright carry-ons queue beneath an airplane gate sign beside a floor arrow pointing towards the gate."


def carry_on(s, x, y, w):
    for a in (x + 2, x + w - 4):
        s.box(a, y + 8, 0, 2.8, 2.4, 3, .7)
    s.tube([(x + 4, y + 5, 20), (x + 4, y + 5, 30),
            (x + w - 3, y + 5, 30), (x + w - 3, y + 5, 20)], 1.05)
    s.box(x, y, 2, w, 12, 19, 2.7)
    for a in (4, w - 4):
        s.line([(x + a, y + 12, 6), (x + a, y + 12, 16)], DETAIL)


def draw(s):
    post(s, 3, 5, 52, width=3.6)
    s.box(-4, 2, 41, 46, 5, 25, 2)
    airplane(s, 19, 7, 54, .79, vertical=True)
    arrow(s, [(63, 40, .1), (22, 36, .1)], EDGE, head=5.5)
    carry_on(s, 31, 16, 15)
    carry_on(s, 57, 20, 17)
