from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w3 import accessibility_phone, vibration_marks

DESCRIPTION = "Three waves of increasing reach and weight radiate from each side of a smartphone."


def draw(s):
    face = accessibility_phone(s)
    vibration_marks(face, (8, 17, 26), (DETAIL, EDGE, BOLD))
