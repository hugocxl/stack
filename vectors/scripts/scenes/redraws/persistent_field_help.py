from geometry import BOLD
from scenes.redraws._w3 import Surface, speech_outline
from scenes.redraws.required_field_cues import field

DESCRIPTION = "A help balloon with one short line attaches to the corner of a labeled form field."


def draw(s):
    face = field(s)
    bubble = Surface(s, face.point(0, 0, -2), rise=face.rise, back=face.back)
    bubble.plate(speech_outline(58, 36, 42, 24), 2)
    bubble.rules(66, 49, [25], ink=BOLD)
