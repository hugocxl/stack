from geometry import BOLD
from scenes.redraws._w4 import medical_folder
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A medical folder with a large cross shows the top edge of a patient sheet."


def draw(s):
    folder = medical_folder(s)
    medical_cross(folder, 44, 26, 15, BOLD)
