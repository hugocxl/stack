from geometry import BOLD, EDGE
from scenes.redraws._w3 import Surface, credential, flat

DESCRIPTION = "A compact badge printer feeds a slotted credential through its front output slot."


def draw(s):
    s.box(0, 0, 17, 91, 53, 50, 8)
    top = flat(s, 0, 53, 67)
    top.rect(11, 8, 69, 33, 4, EDGE)
    top.oval(70, 19, 3, 3, EDGE)
    s.box(10, 9, 15, 70, 41, 5, 3)
    front = Surface(s, (0, 53, 17))
    front.rect(11, 12, 70, 10, 3, BOLD)
    front.rules(14, 36, [22])
    # The upper edge stays within the printer's output slit.
    credential(s, origin=(14, 55, -9), w=63, h=45, slot=True)
