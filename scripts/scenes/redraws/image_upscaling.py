from scenes.redraws._w2 import face_arrow, photo_print

DESCRIPTION = "A diagonal expansion arrow extends outward from the upper-right corner of a landscape print."


def draw(s):
    point = photo_print(s)
    face_arrow(s, point, [(95, 67), (123, 101)], head=14)
