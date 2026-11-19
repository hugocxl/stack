from scenes.redraws._w1 import solar_stand

DESCRIPTION = "A diagonal shadow falls across several cells of a tilted photovoltaic panel."


def draw(s):
    solar_stand(s, shade=True)
