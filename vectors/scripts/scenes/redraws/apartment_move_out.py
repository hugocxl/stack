from scenes.redraws._kit import badge
from scenes.redraws._sf import carton, doorway

DESCRIPTION = "A packed carton waits in front of an open apartment doorway, carrying an outward arrow badge."


def draw(s):
    doorway(s, 56, 88, 11, 14)
    carton(s, 6, 14, 0, 44, 34, 30)
    badge(s, "arrow", 50, 48, 18, 12)
