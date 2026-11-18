from geometry import EDGE, oval

DESCRIPTION = "Three matching pairs of headphones have smooth, ribbed and perforated earcups."


def headphones(s, x, finish):
    band = [(a, 0, z) for a, z in oval(x, 29, 13.6, 16, 0, 180, count=28)]
    s.tube(band, 2.45)
    for side in (-1, 1):
        cup_x = x + side * 14
        s.tube([(x + side * 13.6, 0, 29), (cup_x, 0, 17)], 1.6)
        s.box(cup_x - 4.1, -4, 3, 8.2, 8, 19, 3)
        s.box(cup_x - 4.3, 3, 5, 8.6, 2.8, 15, 2.4)
        if finish == "ribbed":
            for z in (9, 12, 15):
                s.line([(cup_x - 2.7, 5.8, z), (cup_x + 2.7, 5.8, z)], EDGE)
        elif finish == "perforated":
            for a, z in ((-1.65, 9), (1.65, 9), (-1.65, 15), (1.65, 15)):
                s.line([(cx, 5.8, cz) for cx, cz in oval(cup_x + a, z, 1.05, 1.05, count=16)], EDGE)


def draw(s):
    for x, finish in ((-47, "smooth"), (0, "ribbed"), (47, "perforated")):
        headphones(s, x, finish)
