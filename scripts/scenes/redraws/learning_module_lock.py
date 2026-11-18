from scenes.redraws._kit import badge
from scenes.redraws._w3 import course_card

DESCRIPTION = "A course module card with a mortarboard thumbnail carries a closed padlock badge."


def draw(s):
    face = course_card(s)
    face.rules(12, 20, [43, 34], gap=7)
    badge(s, "lock", 94, 1, 19, 17)
