from geometry import EDGE
from scenes.commerce_objects import carton
from scenes.redraws._kit import arrow

DESCRIPTION = "An outward arrow leads from an open packing carton at the threshold of an apartment doorway."


class ThresholdCarton:
    """Place the library's packing carton just inside the threshold."""

    def __init__(self, scene):
        self.scene = scene

    def box(self, x, y, z, w, d, h, radius):
        self.scene.box(.71*x + 26, .71*y + 14, .71*z + 3, .71*w, .71*d, .71*h,
                       .71*radius)

    def face(self, points, ink=EDGE):
        self.scene.face([(.71*x + 26, .71*y + 14, .71*z + 3) for x, y, z in points], ink)


def draw(s):
    s.box(-9, 5, 0, 67, 21, 3, 1)
    s.face([(48, 12, 3), (32, -28, 3), (32, -28, 69), (48, 12, 69)])
    s.tube([(35, -21, 35), (35, -21, 40)], 1.2)
    s.box(-6, 12, 3, 9, 10, 71, 1)
    s.box(48, 12, 3, 9, 10, 71, 1)
    s.box(-6, 12, 71, 63, 10, 8, 1)
    carton(ThresholdCarton(s))
    arrow(s, [(39, 33, 3), (39, 42, 3), (36, 56, 3)], EDGE, head=9)
