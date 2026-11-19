from geometry import DETAIL, EDGE

DESCRIPTION = "A thick prefabricated facade panel with a fitted window meets its mounting column at two slotted connections."


def draw(s):
    s.box(-33, -7, 0, 17, 15, 65, .6)
    s.box(-36, -10, 65, 20, 18, 7, .7)
    for z in (13, 55):
        s.box(-16, -1, z, 12, 5, 5, .6)
        s.line([(-12, 4, z + 1.5), (-12, 4, z + 3.5)], DETAIL)

    def face(y, left, right, bottom, top):
        return [(left, y, bottom), (right, y, bottom), (right, y, top), (left, y, top)]

    s.face(face(0, -7, 57, 0, 65), openings=(face(0, 5, 41, 23, 54),))
    s.face([(-7, 0, 65), (57, 0, 65), (57, 10, 65), (-7, 10, 65)])
    s.face([(57, 0, 0), (57, 10, 0), (57, 10, 65), (57, 0, 65)])
    s.face(face(10, -7, 57, 0, 65), openings=(face(10, 4, 45, 21, 55),))
    s.face(face(9.7, 4, 45, 21, 55), DETAIL, openings=(face(9.7, 8, 41, 25, 51),))
    s.face(face(7, 8, 41, 25, 51), DETAIL)
    s.box(23, 7, 25, 3, 3, 26, .5)
    s.box(2, 10, 20, 45, 2, 2.3, .5)
