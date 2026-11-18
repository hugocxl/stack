from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface, question

DESCRIPTION = "A tabletop poll card shows a question and three response bars with vote ticks."


def draw(s):
    s.face([(16, 2, 0), (92, 2, 0), (92, 31, 23), (16, 31, 23)])
    face = Surface(s, (0, 53, 4), rise=(-.45, .89), back=(0, -.89, -.45))
    face.plate(rounded(0, 0, 108, 77, 5), 7)
    question(face, 17, 62, 13, EDGE)
    face.rules(31, 65, [57, 37], gap=6)
    face.rules(10, 51, [87])

    for v, width, count in ((37, 57, 5), (23, 37, 3), (9, 21, 1)):
        face.oval(15, v + 4, 3.5, 3.5)
        face.rect(25, v, width, 8, 2, EDGE)
        for i in range(count):
            x = 33 + i * 9
            face.stroke([(x, v + 1), (x, v + 7)])
