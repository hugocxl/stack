from geometry import EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import medical_folder
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A cross-marked medical folder with one patient sheet carries a download arrow badge at its lower corner."


def draw(s):
    folder = medical_folder(s)
    medical_cross(folder, 44, 26, 14, EDGE)
    badge(s, "down", *folder.at(89, 15), 19)
