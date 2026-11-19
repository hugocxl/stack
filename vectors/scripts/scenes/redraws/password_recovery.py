from scenes.redraws._kit import badge
from scenes.redraws._w1 import account_key
from scenes.systems_shapes import lock

DESCRIPTION = "A notched key with a refresh badge lies across the front of a padlock."


def draw(s):
    lock(s, -21, -26, 0, w=42, d=21, h=31)
    account_key(s, -25, 17, 1, .92)
    badge(s, "refresh", -35, 17, 12, 12)
