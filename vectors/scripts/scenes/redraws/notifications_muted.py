from shapely.geometry import LineString

from geometry import BOLD, knockout_layer, project
from scenes.redraws._kit import _screen, _strokes
from scenes.redraws.notification_read import notification_bell

DESCRIPTION = "A single diagonal slash crosses the face of a notification bell."


def draw(s):
    notification_bell(s)
    (stroke,) = _strokes("slash", 50)
    points = [_screen(0, 0, 0, 1.10*u, 28 + .95*v) for u, v in stroke]
    s.layers.append(knockout_layer(LineString([project(point) for point in points]).buffer(.01)))
    s.line(points, BOLD)
