from geometry import BOLD, EDGE
from scenes.redraws._w3 import clipboard, microphone

DESCRIPTION = "A clipped consent form carries a microphone pictogram above its terms and a signature line."


def draw(s):
    form = clipboard(s, w=76, h=98)
    microphone(form, 22, 63, 22, EDGE)
    form.rules(36, 72, (24, 19), gap=7, ink=EDGE)
    form.rules(15, 47, (45, 39, 46, 32), gap=5.5)
    form.rules(15, 16, (46,))
    form.stroke([(19, 18), (26, 25), (30, 26), (31, 22), (28, 17),
                 (26, 19), (33, 22), (36, 19), (42, 22), (44, 20),
                 (54, 23)], BOLD)
