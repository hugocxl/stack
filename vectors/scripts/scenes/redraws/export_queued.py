from scenes.redraws._kit import badge
from scenes.redraws._w5 import zip_file

DESCRIPTION = "An export archive file with a zipper carries a clock badge on its lower corner."


def draw(s):
    zip_file(s)
    badge(s, "clock", 53, -3, 9, 12)
