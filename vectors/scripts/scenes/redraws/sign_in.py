from scenes.redraws._w1 import session_door

DESCRIPTION = "A bold arrow points inward through an open doorway."


def draw(s):
    session_door(s, entering=True)
