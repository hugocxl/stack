from scenes.redraws._kit import badge
from scenes.redraws._w5 import handled_food_bag

DESCRIPTION = "A handled takeaway bag bears a cloche emblem and an attached outbound arrow badge."


def draw(s):
    handled_food_bag(s)
    badge(s, "arrow", 45, 22, 35, 11.5)
