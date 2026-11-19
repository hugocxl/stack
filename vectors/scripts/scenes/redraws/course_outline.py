from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, cover_cap

DESCRIPTION = "A standing syllabus binder organizes three lesson headings beside sequential edge tabs."


def draw(s):
    face = Surface(s, (0, 0, 0), rise=(-.2, .98), back=(0, -.98, -.2))
    face.plate(rounded(0, 0, 77, 95, 5), 12)
    for v in (49, 32, 15):
        tab = Surface(s, face.point(0, 0, 3), rise=face.rise, back=face.back)
        tab.plate(rounded(71, v - 4, 15, 9, 2), 2)
    face.rect(9, 6, 63, 83, 2, EDGE)
    cover_cap(face, 25, 75, 24)
    face.rules(39, 75, [25], ink=BOLD)
    face.stroke([(15, 56), (65, 56)])
    for v, width in ((47, 33), (30, 25), (13, 29)):
        face.oval(19, v + 2, 2.7, 2.7, EDGE)
        face.rules(27, v + 2, [width], ink=EDGE)
        face.rules(27, v - 4, [width * .71])
