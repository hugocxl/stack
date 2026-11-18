from scenes.redraws._kit import badge
from scenes.redraws.mindfulness_attendance import meditation_pass

DESCRIPTION = "A meditation class pass bears a lotus pictogram and a reminder clock badge."


def draw(s):
    face = meditation_pass(s)
    badge(s, "clock", *face.at(74, 43), 12)
