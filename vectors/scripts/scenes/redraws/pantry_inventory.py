from scenes.redraws._w5 import cupboard_shell, cupboard_trim, pantry_jar

DESCRIPTION = "An open pantry cabinet holds grouped jars and tins on two shelves."


def draw(s):
    cupboard_shell(s, 59, 25, 61, shelves=(27,))
    for x, radius, height in ((12, 6, 14), (29, 8, 18), (46, 6.5, 15)):
        pantry_jar(s, x, 15, 3, radius, height)
    for x, radius, height in ((14, 7, 20), (30, 6, 16), (45, 6, 16)):
        pantry_jar(s, x, 15, 30, radius, height, label=x == 14)
    cupboard_trim(s, 59, 25, 61)
