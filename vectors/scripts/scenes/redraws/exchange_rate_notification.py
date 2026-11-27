from geometry import knockout_layer, oval, project
from shapely.geometry import Polygon

from scenes.redraws._kit import _screen
from scenes.redraws._sf import coin_face, screen
from scenes.redraws.notification_read import notification_bell

DESCRIPTION = "A notification bell carries a currency coin at its lower right, announcing a rate change."


def draw(s):
    notification_bell(s)
    at = screen(*_screen(0, 0, 0, 34, 8))
    s.layers.append(knockout_layer(Polygon([project(at(u, v)) for u, v in oval(0, 0, 15, 15, count=48)])))
    coin_face(s, at, 14, 3)
