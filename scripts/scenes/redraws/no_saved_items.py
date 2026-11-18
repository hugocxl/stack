from geometry import BOLD
from scenes.redraws._w3 import Surface

DESCRIPTION = "A single dashed bookmark outline stands on end with a deep V-notch in its lower edge."


def draw(s):
    ribbon = Surface(s, (0, 0, 0), rise=(-.25, .97), across=(.90, -.37))
    outline = [(0, 0), (0, 48), (2, 50), (29, 50), (31, 48), (31, 0), (15.5, 13)]
    ribbon.stroke(outline, BOLD, closed=True, dashed=True)
