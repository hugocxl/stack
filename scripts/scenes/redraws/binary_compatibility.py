from geometry import BOLD
from scenes.redraws._kit import badge
from scenes.redraws._w1 import file_card

DESCRIPTION = "A two-level binary signal crosses the face of an executable file with a check badge."


def draw(s):
    file_card(s, -30, 0, w=60, h=65, depth=8)
    signal = [(-24, 24), (-17, 24), (-17, 41), (-7, 41), (-7, 24),
              (4, 24), (4, 41), (19, 41), (19, 24), (24, 24)]
    s.line([(x, 0, z) for x, z in signal], BOLD)
    badge(s, "check", 34, 0, 17, 13)
