from scenes.redraws._w1 import container_cube, seal

DESCRIPTION = "A ribbon seal is attached to the emblem plate on a ribbed software container."


def draw(s):
    container_cube(s)
    seal(s, 0, 24, 27, 9)
