from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A large trackball sits in a rounded pointing-device housing behind two broad click buttons."


def draw(s):
    shell = Surface(s, (0, 71, 6), rise=(-.90, .43), back=(0, -.43, -.90))
    shell.plate(rounded(0, 0, 101, 73, 16), 9)
    shell.rect(8, 4, 40, 19, 7, EDGE)
    shell.rect(53, 4, 40, 19, 7, EDGE)
    shell.oval(50.5, 47, 31, 24, EDGE)
    place = shell.viewer_axes(50.5, 53)
    s.face([shell.point(*place(a, b)) for a, b in oval(0, 0, 24, 24)], BOLD)
    shell.stroke([place(a, b) for a, b in oval(0, 3, 23, 12, 205, 335, 22)], DETAIL)
