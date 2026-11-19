from scenes.redraws._w1 import session_door

DESCRIPTION = "A bold arrow points outward through an open doorway."


def draw(s):
    session_door(s, entering=False)
