from scenes.redraws._kit import badge
from scenes.redraws.material_samples import swatch_fan

DESCRIPTION = "A check badge overlaps the upper corner of the foremost chip in a bound finish swatch fan."


def draw(s):
    chip = swatch_fan(s)
    badge(s, "check", *chip(16, 67, 3), 11)
