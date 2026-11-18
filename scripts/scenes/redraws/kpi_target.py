from geometry import BOLD
from scenes.redraws._w2 import chart_marker, target_face

DESCRIPTION = "A freestanding round target has three concentric scoring rings around a bold center point."


def draw(s):
    p = target_face(s)
    chart_marker(s, p, 0, 59, 3.7, BOLD)
