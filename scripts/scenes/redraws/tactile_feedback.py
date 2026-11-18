from geometry import BOLD
from scenes.redraws._w3 import accessibility_phone, vibration_marks

DESCRIPTION = "One short vibration arc on each side hugs a smartphone."


def draw(s):
    face = accessibility_phone(s)
    vibration_marks(face, (11,), (BOLD,))
