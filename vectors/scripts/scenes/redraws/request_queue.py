from scenes.redraws._w1 import request_card

DESCRIPTION = "Three standing request cards form a queue with a wider gap before the front card."


def draw(s):
    for x, y in ((-28, -23), (-28, -11), (-26, 12)):
        request_card(s, x, y)
