from scenes.redraws._kit import warning
from scenes.redraws._w1 import turbine

DESCRIPTION = "A wind turbine carries an exclamation triangle beside its nacelle."


def draw(s):
    turbine(s, 0, 0, 0, 62)
    warning(s, 17, -10, 52, 30)
