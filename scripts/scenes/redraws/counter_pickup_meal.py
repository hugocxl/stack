from scenes.redraws._w5 import cloche_mark, handled_food_bag, rect

DESCRIPTION = "A handled meal bag rests on a pickup counter marked with a serving cloche."


def draw(s):
    s.box(0, 0, 0, 67, 30, 24, 2)
    s.box(-2, -1, 23, 71, 33, 5, 2)
    handled_food_bag(s, 15, 7, 28, scale=.78, emblem=False)
    face = lambda x, z: (x, 30, z)
    rect(s, face, 21, 4, 26, 16, 2)
    cloche_mark(s, face, 34, 9, .77)
