from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w2 import search_display
from scenes.redraws._w3 import Surface

DESCRIPTION = "A desktop gallery window shows a collection of objects with an outward arrow badge on its frame."


def draw(s):
    search_display(s, 110, 77)
    face = Surface(s, (0, 0, 0))
    for x in (9, 41, 73):
        face.rect(x, 17, 27, 35, 2, EDGE)
        face.rules(x + 5, 10, [17])

    face.oval(22, 34, 7, 10, EDGE)
    face.stroke([(51, 43), (58, 43), (55, 38), (61, 33), (60, 28),
                 (50, 28), (48, 33), (54, 38)], EDGE, closed=True)
    face.stroke([(78, 29), (87, 44), (95, 30), (90, 26)], EDGE, closed=True)
    badge(s, "arrow", 112, 3, 70, 15)
