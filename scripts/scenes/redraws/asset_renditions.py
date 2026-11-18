from scenes.redraws._w4 import photo_print

DESCRIPTION = "Three staggered photographic prints repeat the same landscape at large, medium, and small sizes."


def draw(s):
    photo_print(s, 95, 76, offset=(2, 0, 10), angle=-17)
    photo_print(s, 67, 54, offset=(52, -1, 5), angle=-23)
    photo_print(s, 42, 35, offset=(82, -4, 0), angle=-29)
