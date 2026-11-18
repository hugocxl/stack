from geometry import DETAIL, EDGE, oval
from scenes.redraws._w5 import dining_table, place_setting

DESCRIPTION = "A farm picnic table with built-in benches is set with two plates and a bowl of fresh produce."


def draw(s):
    dining_table(s, picnic=True)
    top = lambda x, y: (x, y, 33)
    for y in (14, 32):
        s.line([top(4, y), top(66, y)], DETAIL)
    for x, y in ((17, 15), (52, 33)):
        place_setting(s, top, x, y, 6.7, utensils=False)
    s.solid(oval(36, 23, 7, 5)[:-1], 33, 5,
            top=oval(36, 23, 12, 9)[:-1], crease=False)
    s.ellipse(36, 23, 38, 12, 9, EDGE)
    for x, y, r in ((32, 20, 3.4), (41, 21, 3.6), (36, 26, 4.3)):
        s.disk(x, y, 38, r, r, 3)
        s.line([(x, y, 41), (x + 1.7, y, 43)], DETAIL)
