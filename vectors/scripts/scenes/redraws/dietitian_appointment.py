from geometry import BOLD, EDGE
from scenes.redraws.clinician_appointment import selected_date

DESCRIPTION = "A desk calendar highlights a selected date with a bowl and spoon."


def draw(s):
    page, u, v = selected_date(s, 1, 1)
    page.outline([(u - 7, v - 1), (u + 7, v - 1), (u + 5, v + 3),
                  (u + 2, v + 5), (u - 2, v + 5), (u - 5, v + 3)], BOLD)
    page.line([(u + 1, v - 1), (u + 5, v - 5)], EDGE)
