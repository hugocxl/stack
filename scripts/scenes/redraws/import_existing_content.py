from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w1 import screen_point, standing_folder

DESCRIPTION = "A downward arrow points into an open project folder holding a stack of documents."


def draw(s):
    standing_folder(s, documents=True)
    origin = (15, 8, 45)
    arrow(s, [screen_point(*origin, 0, v) for v in (25, -5)], BOLD, head=11)
