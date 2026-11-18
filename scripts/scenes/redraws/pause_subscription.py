from scenes.redraws._kit import badge
from scenes.redraws._w5 import subscription_control

DESCRIPTION = "A recurring-payment controller carries a pause badge beside its currency symbol and renewal dial."


def draw(s):
    face = subscription_control(s)
    badge(s, "pause", *face(77, 41), 12.5)
