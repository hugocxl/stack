from geometry import DETAIL, EDGE, oval
from scenes.redraws.page_moved import Surface

DESCRIPTION = "An empty wire shopping cart has a raised handle and four caster wheels."


def draw(s):
    bottom = [(4, 6, 16), (77, 6, 16), (77, 48, 16), (4, 48, 16)]
    rim = [(-7, 0, 48), (86, 0, 55), (86, 54, 55), (-7, 54, 48)]

    def between(a, b, fraction):
        return tuple(start + (end - start) * fraction for start, end in zip(a, b))

    for y in (9, 49):
        for x in (13, 70):
            wheel = Surface(s, (0, y, 0))
            wheel.plate(oval(x, 7, 6.5, 6.5, count=24)[:-1], 3)
            wheel.loop(oval(x, 7, 2, 2, count=12)[:-1], DETAIL)
    s.box(4, 6, 13, 73, 42, 3, 2)
    for i, j in ((0, 1), (3, 0), (1, 2), (2, 3)):
        ink = EDGE if i in (1, 2) else DETAIL
        s.line([bottom[j], rim[j]], EDGE)
        s.line([rim[i], rim[j]], EDGE)
        for t in (.25, .5, .75):
            s.line([between(bottom[i], bottom[j], t), between(rim[i], rim[j], t)], ink)
        for t in (.32, .65):
            s.line([between(bottom[i], rim[i], t), between(bottom[j], rim[j], t)], DETAIL)
    s.line([rim[2], (104, 54, 72), (104, 0, 72), rim[1]], EDGE)
    s.tube([(104, 45, 72), (104, 9, 72)], 2.7, EDGE)
