from scenes.redraws._kit import badge
from scenes.redraws._w4 import magazine

DESCRIPTION = "A bound magazine with a landscape cover carries a circular renewal arrow badge."


def draw(s):
    cover = magazine(s)
    badge(s, "refresh", *cover.at(78, 80), 18)
