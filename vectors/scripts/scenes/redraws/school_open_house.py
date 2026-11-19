from scenes.redraws._w3 import school

DESCRIPTION = "A school entrance stands open beneath its bell, with both door leaves swung outward."


def draw(s):
    school(s, doors_open=True)
