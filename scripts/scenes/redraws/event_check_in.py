from scenes.redraws._kit import badge
from scenes.redraws._w3 import admission_marks, ticket

DESCRIPTION = "A perforated admission ticket carries a check badge at its upper stub corner."


def draw(s):
    face = ticket(s)
    admission_marks(face)
    badge(s, "check", 103, 1, 46, 15)
