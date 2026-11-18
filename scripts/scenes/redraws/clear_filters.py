from scenes.redraws._kit import badge
from scenes.redraws._w4 import nav_funnel

DESCRIPTION = "A filter funnel carries an X badge near the bottom of its taper."


def draw(s):
    nav_funnel(s)
    badge(s, "x", 24, 12, 26, 18)
