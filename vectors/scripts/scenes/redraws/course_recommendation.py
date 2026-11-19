from scenes.redraws._kit import badge
from scenes.redraws._w3 import course_card

DESCRIPTION = "A mortarboard course card carries a star badge beside its title."


def draw(s):
    face = course_card(s)
    face.rules(9, 18, [55, 45], gap=7)
    badge(s, "star", *face.point(97, 54), 16)
