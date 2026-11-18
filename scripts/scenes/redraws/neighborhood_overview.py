from geometry import DETAIL, EDGE
from scenes.commerce_objects import house


class HousePlot:
    """Place the same gabled house on each lot."""
    def __init__(self, scene, x, y, scale):
        self.scene, self.x, self.y, self.scale = scene, x, y, scale

    def point(self, point):
        x, y, z = point
        return self.x + x*self.scale, self.y + y*self.scale, 3 + z*self.scale

    def box(self, x, y, z, width, depth, height, radius):
        self.scene.box(*self.point((x, y, z)), width*self.scale, depth*self.scale,
                       height*self.scale, radius*self.scale)

    def face(self, points, ink=EDGE):
        self.scene.face([self.point(p) for p in points], ink)

    def line(self, points, ink=DETAIL):
        self.scene.line([self.point(p) for p in points], ink)


DESCRIPTION = "Three gabled houses line a single sidewalk that turns a street corner."


def draw(s):
    lot = [(-53, -34), (48, -34), (48, 7), (6, 7), (6, 49), (-53, 49)]
    for a, b in zip(lot, lot[1:] + lot[:1]):
        if b[1] > a[1] or b[0] < a[0]:
            s.face([(*a, 0), (*b, 0), (*b, 3), (*a, 3)])
    s.face([(*p, 3) for p in lot])
    s.line([(-53, 40, 3), (-2, 40, 3), (-2, 0, 3), (48, 0, 3)], EDGE)
    s.line([(-53, 56, 0), (14, 56, 0), (14, 16, 0), (48, 16, 0)], DETAIL)
    for x, y, end in ((-31, -18, 0), (24, -17, 0), (-23, 24, 40)):
        scale = .68 if y == 24 else .73
        front = y + 15*scale
        for side in (-3, 3):
            s.line([(x + side, front, 3), (x + side, end, 3)], DETAIL)
        house(HousePlot(s, x, y, scale))
