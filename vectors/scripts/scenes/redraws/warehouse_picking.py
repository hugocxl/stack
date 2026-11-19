from geometry import DETAIL, EDGE, oval
from scenes.redraws._w1 import software_package, upright_profile

DESCRIPTION = "A raised forklift lifts a taped carton clear of the upper shelf of a stock rack."


def draw(s):
    # The rack faces the forklift, leaving the lifted carton visible in the aisle.
    for x, y in ((-38, -29), (-38, 35), (-12, -29), (-12, 35)):
        s.box(x, y, 0, 3, 3, 50, .5)
    for z in (5, 30):
        s.box(-38, -29, z, 30, 67, 3, 1)
    s.box(-34, 8, 8, 19, 24, 16, 1)
    s.box(-35, -24, 33, 20, 22, 16, 1)

    for x in (28, 53):
        for y in (12, 37):
            s.face([(a, y, b) for a, b in oval(x, 8, 8, 8, count=28)[:-1]], EDGE)
            s.line([(a, y, b) for a, b in oval(x, 8, 3.3, 3.3, count=18)], DETAIL)
    cab = [(19, 11), (19, 23), (36, 23), (43, 21), (63, 21), (63, 11),
           (61, 11), (58, 15), (48, 15), (45, 11),
           (36, 11), (33, 15), (23, 15), (20, 11)]
    upright_profile(s, cab, 37, 25)
    s.box(35, 17, 23, 11, 15, 5, 1)
    s.box(44, 17, 25, 4, 15, 11, 1)
    s.tube([(26, 22, 23), (28, 22, 32)], .8, DETAIL)
    s.ellipse(28, 22, 32, 3.5, 3.5, EDGE)
    for y in (15, 34):
        s.tube([(23, y, 23), (23, y, 53), (51, y, 53), (55, y, 18)], 1.25, EDGE)
    s.box(22, 13.8, 51.5, 29, 21.5, 3, .8)

    for y in (16, 29):
        s.box(16, y, 7, 4, 4, 52, .7)
        s.box(-18, y, 36, 38, 4, 3, .6)
    s.box(14, 15, 37, 3, 19, 6, .7)
    software_package(s, -6, 24, 39, .48, show_code=False)
