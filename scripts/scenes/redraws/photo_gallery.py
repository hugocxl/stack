from scenes.redraws._w4 import photo_print

DESCRIPTION = "Three fanned photographic prints leave the foremost landscape fully visible."


def draw(s):
    photo_print(s, 91, 71, offset=(-11, 3, 6), angle=-6, image=False)
    photo_print(s, 91, 71, offset=(3, 3, 3), angle=-16, image=False)
    photo_print(s, 91, 71, offset=(12, 3, 0), angle=-26)
