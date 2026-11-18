from geometry import DETAIL, EDGE

DESCRIPTION = "One wall of a house cutaway transitions from exposed studs to newly installed siding."


def draw(s):
    s.box(-39, -25, 0, 78, 50, 4, 1)
    s.box(-39, -25, 4, 5, 50, 37, 1)
    s.box(-34, -25, 4, 73, 5, 37, 1)
    s.face([(-41, -25, 40), (-41, 0, 62), (6, 0, 62), (6, -25, 40)])
    s.face([(-41, 0, 62), (6, 0, 62), (6, 27, 40), (-41, 27, 40)])
    s.tube([(-40, -25, 40), (-40, 0, 62), (-40, 26, 40)], 1.5)
    s.tube([(39, -25, 41), (39, 0, 62), (39, 25, 41)], 1.5)
    s.tube([(6, 0, 62), (39, 0, 62)], 1.4)
    s.box(-39, 20, 4, 78, 5, 4, .5)
    s.box(-39, 20, 36, 78, 5, 5, .5)
    for x in (-39, -23, -7, 9, 24, 34):
        s.box(x, 20, 8, 5, 5, 28, .8)

    for z, start in ((4, -13), (12, -13), (20, -6), (28, -6), (36, 7)):
        s.face([(start, 25.25, z), (39, 25.25, z), (39, 25.25, z + 8),
                (start, 25.25, z + 8)], EDGE)
    s.line([(39.1, 25, 4), (39.1, 25, 39), (39.1, 10, 39)], DETAIL)
