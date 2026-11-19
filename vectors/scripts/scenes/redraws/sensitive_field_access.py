from scenes.redraws._kit import badge
from scenes.redraws._w5 import field_dots, field_form

DESCRIPTION = "A clipboard form has a padlock badge attached to its masked input field."


def draw(s):
    face = field_form(s)
    field_dots(s, face)
    badge(s, "lock", *face(56, 26.5), 11.5)
