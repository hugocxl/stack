from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, component_art, visibility_art

DESCRIPTION = "A slashed eye on a raised visibility control marks a component outlined with dashes."


def draw(s):
    canvas = Surface(s, (0, 0, 0), rise=(-.55, .84), back=(0, -.84, -.55))
    canvas.plate(rounded(0, 0, 91, 64, 4), 6)
    canvas.stroke([(13, 11), (78, 11), (78, 53), (13, 53), (13, 11)], EDGE, dashed=True)
    component_art(canvas, 43, 29, 35, 27)
    control = Surface(s, canvas.point(78, 56), across=(.707, -.707))
    control.plate(rounded(-24, -14, 48, 28, 13), 3)
    visibility_art(control, 0, 0, 14, hidden=True)
