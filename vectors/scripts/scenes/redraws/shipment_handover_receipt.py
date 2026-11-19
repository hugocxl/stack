from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w1 import carrier_van

DESCRIPTION = "A shipping receipt with a delivery van header and a handwritten signature carries a check badge beside its signature line."


def draw(s):
    def point(x, z):
        return x, -.37 * z, z

    bottom = [(x, 0 if index % 2 == 0 else 3) for index, x in enumerate(range(-28, 29, 4))]
    top = [(x, 71 if index % 2 == 0 else 68) for index, x in enumerate(range(28, -29, -4))]
    rim = bottom + top

    s.face([(x, y - 2, z) for x, y, z in (point(*p) for p in rim)], EDGE)
    s.face([point(*p) for p in rim], EDGE)
    # Stamp the carrier pictogram onto the inclined paper instead of an upright plate.
    class ReceiptSurface:
        def line(self, points, ink):
            s.line([point(x, z) for x, _, z in points], ink)

    carrier_van(ReceiptSurface(), -23, 0, 42, 29)
    for z, length in ((39, 42), (33, 33), (27, 38)):
        s.line([point(-22, z), point(-22 + length, z)], DETAIL)

    s.line([point(*p) for p in [(-22, 12), (-19, 12.5), (-16, 14.2), (-14, 17),
                               (-14, 19), (-16, 20), (-18, 18.2), (-18, 15.2),
                               (-16, 12.6), (-13, 12), (-10, 14), (-8, 14.8),
                               (-7, 13.5), (-5, 12.7), (-2, 13.3), (4, 14.2), (10, 14)]], EDGE)
    s.line([point(-22, 9), point(21, 9)], DETAIL)
    badge(s, "check", 26, -3, 11, 10)
