from scenes.redraws._w2 import merge_diagram

DESCRIPTION = "A check badge marks the shared commit where two version branches converge."


def draw(s):
    merge_diagram(s, checked=True)
