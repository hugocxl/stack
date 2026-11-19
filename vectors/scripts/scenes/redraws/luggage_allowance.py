from scenes.redraws._w5 import baggage_scale

DESCRIPTION = "An upright suitcase rests on a baggage scale with a heavy limit mark on its readout."


def draw(s):
    baggage_scale(s, limit=True)
