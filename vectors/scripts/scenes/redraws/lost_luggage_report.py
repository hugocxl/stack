from scenes.redraws._kit import badge
from scenes.redraws._w5 import luggage, luggage_tag

DESCRIPTION = "An upright rolling suitcase has a hanging luggage tag with an exclamation badge at its lower edge."


def draw(s):
    luggage(s)
    luggage_tag(s)
    badge(s, "exclaim", 56, 24, 40, 11.5)
