from scenes.redraws._kit import badge
from scenes.redraws._w5 import zip_file

DESCRIPTION = "An exported archive file with a zipper carries a check badge on its lower corner."


def draw(s):
    zip_file(s)
    badge(s, "check", 53, -3, 9, 12)
