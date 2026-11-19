from scenes.redraws._w5 import subscription_control

DESCRIPTION = "A recurring-payment controller has a circular renewal dial and two sliding switches below a currency mark."


def draw(s):
    subscription_control(s, settings=True)
