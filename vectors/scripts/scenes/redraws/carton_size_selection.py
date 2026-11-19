from scenes.redraws._w1 import caliper, open_carton_back, open_carton_front

DESCRIPTION = "The jaws of a large caliper touch the opposite ends of an open carton."


def draw(s):
    carton = (-35, 35, -23, 23, 29)
    open_carton_back(s, *carton)
    open_carton_front(s, *carton, flap_depth=9, flap_drop=8)
    caliper(s, -35, 35, -1, 59, 28)
