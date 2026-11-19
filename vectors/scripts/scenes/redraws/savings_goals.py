from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w5 import money_coin

DESCRIPTION = "Inside a glass savings jar, two coin stacks and a loose coin rise toward a single goal line below the slotted lid."


def draw(s):
    radius = 29
    s.ellipse(0, 0, 4, radius, radius, DETAIL, -135, 45)
    s.ellipse(0, 0, 1, radius, radius, EDGE, 0, 180)
    for x, y in oval(0, 0, radius, radius, 135, 315, 1):
        s.line([(x, y, 1), (x, y, 68)], EDGE)
    s.ellipse(0, 0, 1, radius, radius, EDGE, 180, 360)

    for x, y, count in ((9, -8, 5), (-6, 7, 3)):
        foot = oval(x, y, 10, 10, count=40)[:-1]
        for i in range(count):
            s.solid(foot, 3 + i * 5.4, 5.4, crease=False)
        s.ellipse(x, y, 3 + count * 5.4, 7.4, 7.4, DETAIL)
    money_coin(s, -10, 12, 11, 8.5)
    s.ellipse(0, 0, 59, radius, radius, BOLD, -16, 106)
    s.disk(0, 0, 68, 31, 31, 8)
    slot = rounded(-12, -2, 24, 4, 1.8)
    s.line([(x, y, 76) for x, y in slot + slot[:1]], EDGE)
