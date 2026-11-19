from shapely.geometry import Polygon
from shapely.ops import unary_union

from geometry import BOLD, DETAIL, EDGE, oval, project, rounded
from scenes.redraws._kit import _screen, _strokes, arrow

DESCRIPTION = "A browser window with an address bar shows a bent forward arrow."


class Surface:
    """Local drawing coordinates on an upright, leaning, or viewer-facing surface."""

    def __init__(self, scene, origin=(0, 0, 0), *, lean=0, rise=0, side=False, screen=False):
        self.scene = scene
        self.origin = origin
        self.lean = lean
        self.rise = rise
        self.side = side
        self.screen = screen

    def point(self, u, v, depth=0):
        x, y, z = self.origin
        if self.screen:
            return _screen(x, y, z, u, v, back=depth)
        offset = self.lean * v + depth
        height = z + v + self.rise * u
        if self.side:
            return x - offset, y - u, height
        return x + u, y - offset, height

    def line(self, points, ink=DETAIL, dashed=False):
        # The third coordinate is unused when this surface is passed to arrow().
        self.scene.line([self.point(*point[:2]) for point in points], ink, dashed)

    def loop(self, points, ink=EDGE, dashed=False):
        self.line([*points, points[0]], ink, dashed)

    def frame(self, u, v, width, height, radius=2, ink=DETAIL):
        self.loop(rounded(u, v, width, height, radius), ink)

    def plate(self, points, depth, ink=EDGE):
        """Extrude an outline while preserving recessed or scalloped edges."""
        front = [self.point(u, v) for u, v in points]
        back = [self.point(u, v, depth) for u, v in points]
        ends = [[project(point) for point in face] for face in (front, back)]
        sides = [
            Polygon((ends[0][i - 1], a, b, ends[1][i - 1]))
            for i, (a, b) in enumerate(zip(*ends))
        ]
        silhouette = unary_union([Polygon(end) for end in ends] + [p for p in sides if p.area > .01])
        self.scene.layers.append((silhouette.boundary, silhouette, ink))
        self.scene.face(front, ink)

    def arrow(self, points, ink=EDGE, head=5):
        arrow(self, [(u, v, 0) for u, v in points], ink, head)

    def glyph(self, kind, u, v, radius, ink=EDGE):
        for stroke in _strokes(kind, radius):
            self.line([(u + a, v + b) for a, b in stroke], ink)


def draw(s):
    page = Surface(s, (0, 20, 3), lean=.31)
    page.plate(rounded(0, 0, 104, 68, 6), 6)
    page.line([(0, 49), (104, 49)], EDGE)
    page.frame(25, 54, 69, 8, 3)
    for x in (9, 15):
        page.loop(oval(x, 58, 1.3, 1.3, count=10)[:-1], DETAIL)
    page.arrow([(29, 12), (29, 20), (30, 24), (33, 27), (37, 28), (73, 28)], BOLD, 11)
