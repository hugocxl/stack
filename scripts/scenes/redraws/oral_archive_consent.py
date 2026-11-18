from geometry import BOLD, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w3 import clipboard, microphone

DESCRIPTION = "A signed release on a clipboard bears a microphone pictogram and a check badge."


def draw(s):
    face = clipboard(s, w=79, h=87)
    microphone(face, 39, 53, 32, EDGE)
    face.rules(18, 33, [43, 32], gap=7)
    face.rules(18, 12, [42], ink=EDGE)
    face.stroke([(21, 14), (26, 21), (28, 15), (33, 18), (34, 14), (41, 16)], BOLD)
    badge(s, "check", *face.point(75, 69, -2), 14)
