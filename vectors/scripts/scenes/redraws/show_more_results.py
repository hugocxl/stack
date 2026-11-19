from geometry import BOLD
from scenes.redraws._w4 import nav_path, nav_phone, nav_result_rows

DESCRIPTION = "An open downward arrow sits below three results on a handheld screen."


def draw(s):
    face = nav_phone(s)
    nav_result_rows(face, 11, 73, (28, 33, 25), step=17)
    nav_path(face, [(33, 28), (33, 11)], BOLD, head=9)
