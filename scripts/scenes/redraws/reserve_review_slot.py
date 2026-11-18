from scenes.redraws._w2 import desk_calendar, face_magnifier

DESCRIPTION = "A magnifier picks out one outlined time block on a ring-bound desk calendar."


def draw(s):
    point = desk_calendar(s, active=(1, 0))
    face_magnifier(s, point, 49, 21, 14, direction=(.83, -.56))
