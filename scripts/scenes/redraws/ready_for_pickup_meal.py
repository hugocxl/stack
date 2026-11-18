from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w5 import cloche_mark, food_bag_shell, printed_stroke

DESCRIPTION = "A handled takeaway bag bears a cloche emblem and an attached check badge."


def draw(s):
    s.tube([(13, 4, 43), (13, 4, 52), (17, 4, 57),
            (27, 4, 57), (31, 4, 52), (31, 4, 43)], 1.25, DETAIL)
    front = food_bag_shell(s, 44, 23, 45)
    s.tube([(13, 22, 41), (13, 22, 51), (17, 22, 56),
            (27, 22, 56), (31, 22, 51), (31, 22, 41)], 1.5)
    printed_stroke(s, front, [(4, 6), (40, 6)], DETAIL)
    cloche_mark(s, front, 20.5, 17.5, .9)
    badge(s, "check", *front(44, 33), 10.5)
