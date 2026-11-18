from geometry import BOLD, oval
from scenes.commerce_objects import valve
from scenes.redraws._kit import arrow

DESCRIPTION = "A clockwise arrow curls around the handwheel of a flanged water shutoff valve."


def draw(s):
    valve(s)
    s.disk(0, 0, 32, 3, 3, 2)
    arrow(s, [(x, y, 38) for x, y in oval(0, 0, 20, 20, -211, -25, 36)],
          BOLD, head=6.5)
