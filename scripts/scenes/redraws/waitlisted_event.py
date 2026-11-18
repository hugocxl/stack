from scenes.redraws._kit import badge
from scenes.redraws._w3 import admission_marks, ticket

DESCRIPTION = "A perforated admission ticket carries a clock badge above its stub."


def draw(s):
    face = ticket(s)
    admission_marks(face)
    badge(s, "clock", 99, 0, 48, 15)
