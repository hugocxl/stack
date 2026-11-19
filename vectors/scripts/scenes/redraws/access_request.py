from scenes.redraws._kit import badge
from scenes.redraws._w5 import access_form, credential_rows

DESCRIPTION = "A key heads a clipboard form with two input fields and a plus badge at its corner."


def draw(s):
    face = access_form(s)
    credential_rows(s, face, 10, 27)
    badge(s, "plus", *face(53, 56), 12)
