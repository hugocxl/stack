from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A gabled model home with a front door and picture window carries a clock badge near its roof."


def gabled_home(s, x=0, y=0, z=0, scale=1, *, entry_visible=True):
    """Draw a compact gabled home with a visible side window and eaves."""
    def p(u, v, h):
        return x + u * scale, y + v * scale, z + h * scale

    def line(points, ink=DETAIL):
        s.line([p(*point) for point in points], ink)

    s.box(*p(-23, -18, 0), 46 * scale, 36 * scale, 30 * scale, .7 * scale)
    if entry_visible:
        line([(-16, 18, 0), (-16, 18, 21), (-4, 18, 21), (-4, 18, 0)], EDGE)
        line([(-7, 18, 9), (-7, 18, 11)], DETAIL)
        line([(3, 18, 11), (3, 18, 23), (16, 18, 23), (16, 18, 11), (3, 18, 11)], EDGE)
        line([(9.5, 18, 11), (9.5, 18, 23)])
    else:
        line([(-14, 18, 10), (-14, 18, 23), (16, 18, 23),
              (16, 18, 10), (-14, 18, 10)], EDGE)
        line([(1, 18, 10), (1, 18, 23)])
    line([(23, -10, 11), (23, 7, 11), (23, 7, 22), (23, -10, 22), (23, -10, 11)], EDGE)

    s.face([p(23, -18, 30), p(23, 0, 48), p(23, 18, 30)], EDGE)
    s.face([p(-25, -21, 29), p(-25, 0, 51), p(25, 0, 51), p(25, -21, 29)], EDGE)
    s.face([p(-25, 0, 51), p(-25, 21, 29), p(25, 21, 29), p(25, 0, 51)], EDGE)
    line([(-25, 21, 29), (25, 21, 29), (25, 21, 27), (-25, 21, 27), (-25, 21, 29)], EDGE)


def draw(s):
    gabled_home(s)
    badge(s, "clock", 26, -14, 46, 12)
