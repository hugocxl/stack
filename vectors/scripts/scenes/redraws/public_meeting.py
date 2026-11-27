from scenes.redraws._w3 import classroom_chair

DESCRIPTION = "A lectern faces two short rows of chairs at a public meeting."


def draw(s):
    s.box(-12, -62, 0, 26, 18, 40, 2)
    s.box(-15, -65, 40, 32, 24, 4, 2)
    s.tube([(4, -50, 44), (6, -46, 54)], .9)
    for row in range(2):
        for i in range(3):
            classroom_chair(s, -40 + i*28, 8 + row*30, 1.25)
