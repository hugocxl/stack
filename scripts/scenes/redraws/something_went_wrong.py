from scenes.redraws._kit import warning

DESCRIPTION = "A single upright warning triangle surrounds a large exclamation mark."


def draw(s):
    warning(s, 0, 0, 0, 90)
