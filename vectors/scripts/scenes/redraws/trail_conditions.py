from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws.garage_vacancy_queue import post

DESCRIPTION = "A posted trail marker with a mountain and switchback carries an exclamation triangle."


def draw(s):
    post(s, 19, 0, 51, width=5)
    s.box(-4, -2.5, 33, 47, 5, 32, 2)
    y = 2.5
    s.line([(2, y, 47), (12, y, 59), (19, y, 50), (26, y, 56), (34, y, 47)], EDGE)
    s.line([(20, y, 47), (15, y, 45), (21, y, 43), (15, y, 40), (24, y, 36.5)], DETAIL)
    warning(s, 48, 5.5, 46, 26)
