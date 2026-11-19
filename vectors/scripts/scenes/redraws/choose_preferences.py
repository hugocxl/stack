from geometry import DETAIL, EDGE, oval, rounded

DESCRIPTION = "A sloped settings console has three stacked toggle switches in different positions."


def draw(s):
    def face(u, z):
        return (11 - .19 * z, -u, z)

    s.face([face(-27, 0), (-17, 27, 0), (-17, 27, 55), face(-27, 58)], EDGE)
    s.face([face(-27, 58), (-17, 27, 55), (-17, -27, 55), face(27, 58)], EDGE)
    s.face([face(u, z) for u, z in ((-27, 0), (27, 0), (27, 58), (-27, 58))], EDGE)

    for z, knob in ((14, 15), (29, 2), (44, 15)):
        track = rounded(-4, z - 5, 25, 10, 5)
        s.line([face(u, v) for u, v in [*track, track[0]]], EDGE)
        s.line([face(u, v) for u, v in oval(knob, z, 3.1, 3.1, count=24)], EDGE)
        s.line([face(-20, z), face(-11, z)], DETAIL)
