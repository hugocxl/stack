from geometry import BOLD
from scenes.redraws._w2 import desk_calendar, face_arrow

DESCRIPTION = "A bent handoff arrow sits inside the selected date of a ring-bound desk calendar."


def draw(s):
    point = desk_calendar(s)
    face_arrow(s, point, [(42, 43), (42, 51), (56, 51)], BOLD, head=6)
