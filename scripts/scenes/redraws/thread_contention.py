from scenes.redraws._kit import warning
from scenes.redraws._w1 import pipe_junction

DESCRIPTION = "Two broad pipes merge into one narrow pipe, with a warning triangle beside the bottleneck."


def draw(s):
    pipe_junction(s)
    warning(s, 32, 2, 55, 21)
