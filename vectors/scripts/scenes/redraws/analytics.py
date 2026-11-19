from scenes.redraws._w2 import column_row

DESCRIPTION = "Four solid chart columns of different heights stand in one row on a common baseline."


def draw(s):
    column_row(s, (27, 50, 38, 73))
