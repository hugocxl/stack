from scenes.redraws._w5 import pantry_jar

DESCRIPTION = "A pantry jar has a screw lid and a ruled ingredient label wrapped around its side."


def draw(s):
    pantry_jar(s, 24, 24, 0, 21, 50, label=True)
