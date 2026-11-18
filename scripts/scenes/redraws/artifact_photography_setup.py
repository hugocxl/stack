from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._w3 import Surface
from scenes.redraws.artifact_conservation import museum_vase

DESCRIPTION = "A tripod camera points its lens at a small museum vase."


def draw(s):
    for foot in ((12, 8, 0), (34, 9, 0), (-7, 25, 0)):
        s.tube([(15, 13, 44), foot], 1.6)
    s.tube([(15, 13, 44), (15, 13, 59)], 2.7)
    camera = Surface(s, (-5, 17, 51), rise=(.57, .82), back=(0, -.82, .57))
    camera.plate(rounded(0, 0, 40, 25, 3), 19)
    camera.plate([(12, 24), (17, 30), (28, 30), (32, 24)], 12)
    camera.rect(30, 17, 6, 4, 1, EDGE)
    for depth, radius, length in ((0, 11, 5), (-5, 10, 7)):
        lens = Surface(s, camera.point(20, 12, depth - length), rise=camera.rise, back=camera.back)
        lens.plate(oval(0, 0, radius, radius, count=36)[:-1], length)
    lens.oval(0, 0, 7.3, 7.3, BOLD)
    lens.oval(0, 0, 4.5, 4.5, DETAIL)
    museum_vase(s, 15, 75, 0, scale=.60)
