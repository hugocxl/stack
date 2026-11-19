from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge, coin
from scenes.redraws._w5 import rect

DESCRIPTION = "A farm tractor has a raised cab and oversized rear tires, with a clock badge beside the rear wheel."


def draw(s):
    coin(s, 17, 2, 16, 16, 8)
    coin(s, 63, 3, 9, 9, 6)
    s.box(10, 3, 13, 58, 24, 11, 2)
    s.box(11, 4, 29, 28, 23, 25, 2)
    s.box(8, 2, 53, 33, 27, 4, 2)
    rect(s, lambda x, z: (x, 27, z), 15, 34, 19, 15, 1, EDGE)
    rect(s, lambda y, z: (39, y, z), 8, 34, 15, 15, 1, EDGE)
    s.box(39, 5, 22, 33, 21, 13, 3)
    s.tube([(51, 10, 34), (51, 10, 46), (54, 10, 46)], 1.5)
    for z in (25, 28, 31):
        s.line([(72, 10, z), (72, 22, z)], DETAIL)
    for x, y, z, radius, width in ((17, 36, 16, 16, 10), (63, 33, 9, 9, 7)):
        coin(s, x, y, z, radius, width)
        for factor, ink in ((.69, EDGE), (.28, DETAIL)):
            s.line([(a, y, b) for a, b in oval(x, z, radius*factor, radius*factor)], ink)
    badge(s, "clock", 6, 39, 37, 11)
