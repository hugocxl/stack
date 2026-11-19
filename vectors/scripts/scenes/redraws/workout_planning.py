from geometry import BOLD
from scenes.redraws._w4 import dumbbell_mark
from scenes.redraws.clinician_appointment import selected_date

DESCRIPTION = "A desk calendar highlights a workout date with a dumbbell."


def draw(s):
    page, u, v = selected_date(s, 2, 2)
    dumbbell_mark(page, u, v, 8, BOLD)
