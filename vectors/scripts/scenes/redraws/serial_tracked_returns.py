from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._sf import carton

DESCRIPTION = "A carton with a barcode label on its side carries a return badge."


def draw(s):
    front = carton(s, -30, -22, 0, 60, 44, 40)
    s.line([front(10, 8), front(34, 8), front(34, 24), front(10, 24), front(10, 8)], EDGE)
    for i, u in enumerate(range(13, 32, 2)):
        s.line([front(u, 11), front(u, 21 if i % 3 else 22)], EDGE)
    badge(s, "back", 30, 22, 30, 12)
