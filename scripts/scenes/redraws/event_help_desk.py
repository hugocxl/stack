from geometry import BOLD, rounded
from scenes.redraws._w4 import reception_counter

DESCRIPTION = "An attendee help counter has a service bell, a chair behind it, and a large information pictogram on its front."


def draw(s):
    front = reception_counter(s)
    front.oval(38, 22, 15, 16, BOLD)
    front.oval(38, 30, 1.8, 1.8, BOLD)
    front.outline(rounded(35.8, 13, 4.4, 12, 1), BOLD)
