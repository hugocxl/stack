from scenes.redraws._w2 import photo_print, sparkle

DESCRIPTION = "A large four-point generation sparkle overlaps the upper corner of a landscape print."


def draw(s):
    p = photo_print(s)
    sparkle(s, p, 8, 75, 20)
