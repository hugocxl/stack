from geometry import EDGE
from scenes.redraws._w4 import medical_folder
from scenes.redraws.find_a_clinic import medical_cross

DESCRIPTION = "A medical folder holds three patient records with staggered tabs of different heights."


def draw(s):
    folder = medical_folder(s, sheet_tabs=((7, 62, 21), (29, 76, 32), (63, 63, 21)))
    medical_cross(folder, 44, 26, 12, EDGE)
