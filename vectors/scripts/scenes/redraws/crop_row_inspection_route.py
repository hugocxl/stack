from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w5 import crop_furrow

DESCRIPTION = "A single raised row of seedlings has a directional arrow running beside its furrow."


def draw(s):
    crop_furrow(s)
    arrow(s, [(6, 32, 0), (65, 32, 0)], BOLD, head=10)
