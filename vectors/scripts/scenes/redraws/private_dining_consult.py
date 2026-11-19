from scenes.redraws._w5 import dining_table, food_speech, place_setting

DESCRIPTION = "A dining table set for two has an attached speech balloon over its far corner."


def draw(s):
    dining_table(s)
    top = lambda x, y: (x, y, 33)
    place_setting(s, top, 19, 13, 7)
    place_setting(s, top, 48, 32, 7)
    food_speech(s, 58, 9, 40)
