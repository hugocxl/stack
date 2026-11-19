from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w1 import code_rows
from scenes.systems_shapes import bezel

DESCRIPTION = "A backup-code card carries an open-padlock badge beside two rows of grouped code marks."


def draw(s):
    s.box(-37, -6, 0, 74, 6, 46, 3)
    bezel(s, -29, 0, 7, 48, 27, DETAIL, 2.5)
    code_rows(s, -24, 0, 24, count=2, step=12)
    badge(s, "unlock", 34, 0, 37, 15)
