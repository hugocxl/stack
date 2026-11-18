from scenes.redraws._w1 import intake_arrow, open_carton_back, open_carton_front

DESCRIPTION = "Two incoming paths merge into one downward arrow inside an open shipping carton."


def draw(s):
    carton = (-31, 31, -24, 24, 28)
    open_carton_back(s, *carton)
    branch = [(-25, -4, 64), (-23, -4, 56), (-17, -4, 52),
              (-8, -4, 50), (-3, -4, 47), (0, -4, 42)]
    path = [(25, -4, 89), (23, -4, 79), (17, -4, 69), (8, -4, 58),
            (3, -4, 50), (0, -4, 42), (0, -4, 32)]
    intake_arrow(s, path, head=11, branch=branch)
    open_carton_front(s, *carton)
