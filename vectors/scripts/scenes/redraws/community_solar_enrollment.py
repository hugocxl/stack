from scenes.redraws._kit import badge
from scenes.redraws._w1 import solar_stand

DESCRIPTION = "A plus badge sits on the lower corner of a tilted solar panel on footed supports."


def draw(s):
    solar_stand(s)
    badge(s, "plus", 38, 16, 17, 12)
