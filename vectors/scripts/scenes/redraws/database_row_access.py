from scenes.redraws._kit import badge
from scenes.redraws._w5 import dataset_table

DESCRIPTION = "A table engraved on a thick block has one outlined row ending in a padlock badge."


def draw(s):
    face = dataset_table(s, selected=15)
    badge(s, "lock", *face(61, 19), 12)
