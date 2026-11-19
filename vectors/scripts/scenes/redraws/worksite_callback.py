from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import standing_card

DESCRIPTION = "A phone shows a hard hat on its screen and a hooked return-call arrow curling around its lower corner."


def draw(s):
    phone = standing_card(s, 56, 98, angle=-23, lean=.37, depth=8)
    phone.frame(4, 6, 48, 86, 4)
    phone.frame(19, 85, 18, 3, 1.4)
    phone.line(oval(28, 52, 15, 14, 0, 180, count=26), EDGE)
    phone.frame(9, 48, 38, 4, 1.9, EDGE)
    phone.line([(25, 64), (25, 70), (31, 70), (31, 64)], EDGE)
    phone.line([(19, 53), (19, 60)], EDGE)
    phone.line([(37, 53), (37, 60)], EDGE)
    curve = oval(43, 22, 21, 16, -65, 93, count=26)
    arrow(s, [phone.at(u, v) for u, v in curve] + [phone.at(29, 38)], BOLD, head=8)
