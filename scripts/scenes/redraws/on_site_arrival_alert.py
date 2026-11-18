from geometry import DETAIL, EDGE, oval
from scenes.redraws._kit import badge
from scenes.redraws._w4 import Surface, side_wheel, wrench_mark

DESCRIPTION = "A service van with a separate cab silhouette carries an alert badge at the front of its roof."


def service_van(s, *, tracking=False):
    """The field-service van, with a cargo panel, windscreen, and inset tires."""
    near, far = 34, 0
    axles = (16, 69)
    for x in axles:
        side_wheel(s, x, far + 5, 10, 9)
        side_wheel(s, x, near, 10, 10)

    profile = [(0, 10), (0, 42), (4, 48), (56, 48), (65, 44),
               (76, 30), (84, 27), (87, 22), (87, 10)]
    for (a, z), (b, h) in zip(profile[1:-1], profile[2:]):
        s.face([(a, far, z), (a, near, z), (b, near, h), (b, far, h)])
    arches = [(a, near, z) for x in reversed(axles)
              for a, z in oval(x, 10, 11.8, 11.8, 0, 180, 24)]
    s.face([*[(x, near, z) for x, z in profile], *arches])
    s.face([(87, far, 10), (87, near, 10), (87, near, 22), (87, far, 22)])
    for y in (4, 24):
        s.face([(87, y, 15), (87, y + 6, 15), (87, y + 6, 19), (87, y, 19)], DETAIL)

    s.face([(66.5, 3, 42.09), (74.5, 3, 31.91), (74.5, 31, 31.91), (66.5, 31, 42.09)])
    side = Surface(s, lambda u, v: (u, near, v))
    side.outline([(58, 39.5), (65, 39.5), (72, 30), (58, 30)], EDGE)
    side.line([(55, 44), (55, 14), (57, 14)], DETAIL)
    side.rows(58, 25, (5,))
    side.frame(11, 23, 37, 22, 2)
    if tracking:
        side.rows(37, 28, (6,), ink=EDGE)
        pin = [*oval(26, 35.5, 7, 7, -32, 212, count=32), (26, 25)]
        side.outline(pin, EDGE)
        side.oval(26, 35.5, 2.4, 2.4, EDGE)
    else:
        wrench_mark(side, 29, 32.5, .41)


def draw(s):
    service_van(s)
    badge(s, "exclaim", 61, 6, 55, 13)
