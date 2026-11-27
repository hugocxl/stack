from scenes.redraws._kit import badge
from scenes.redraws._sf import carton

DESCRIPTION = "A closed shipping carton carries a return badge as it comes back in."


def draw(s):
    carton(s, -30, -22, 0, 60, 44, 40)
    badge(s, "back", 30, 22, 30, 12)
