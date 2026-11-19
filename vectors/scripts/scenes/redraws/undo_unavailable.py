from shapely.geometry import LineString

from geometry import BOLD, EDGE, project
from scenes.redraws._kit import _screen, _strokes, arrow, badge
from scenes.redraws._w3 import flat, keycap
from scenes.redraws.upload_in_progress import curve

DESCRIPTION = "A tapered keyboard keycap with a curved undo arrow carries a slash badge on its upper-right edge."


def strike(s, center, radius, clearance=1.8):
    """Interrupt lines underneath the shared slash so the mark reads cleanly."""
    for stroke in _strokes("slash", radius):
        path = [_screen(*center, u, v) for u, v in stroke]
        mask = LineString([project(point) for point in path]).buffer(clearance)
        s.layers.append((LineString(), mask, EDGE))
        s.line(path, BOLD)


def draw(s):
    size = 42
    keycap(s, 0, 0, size)
    crown = flat(s, 0, size, 8)
    place = crown.viewer_axes(size / 2, size / 2)
    bend = curve((6, -7), [((23, -7), (23, 4), (8, 4))])
    points = [crown.point(*place(u, v)) for u, v in [*bend, (-19, 4)]]
    arrow(s, points, BOLD, head=8)
    badge(s, "slash", *crown.point(*place(27, 12.5)), 11.5)
