from geometry import DETAIL, EDGE
from scenes.redraws._w2 import face_magnifier

DESCRIPTION = "An open magnifier frames the exposed post and roof joint of a timber house frame."


def timber_frame(s, x=0, y=0, z=0, scale=1, *, simplified=False):
    """Build a gabled frame with posts, wall plates, rafters and a ridge beam."""
    def p(u, v, h):
        return x + u * scale, y + v * scale, z + h * scale

    def beam(u, v, h, w, d, height):
        s.box(*p(u, v, h), w * scale, d * scale, height * scale, .4 * scale)

    def rafter(u):
        for v, other_v in ((-21, 0), (0, 21)):
            left = [(u - 1.65, v, 37 if v else 54),
                    (u - 1.65, other_v, 37 if other_v else 54)]
            right = [(a + 3.3, b, c) for a, b, c in left]
            s.face([p(*left[0]), p(*left[1]), p(*right[1]), p(*right[0])], EDGE)
            s.face([p(*right[0]), p(*right[1]), p(right[1][0], right[1][1], right[1][2] - 3.4),
                    p(right[0][0], right[0][1], right[0][2] - 3.4)], EDGE)

    studs = (-25, -2, 21) if simplified else (-25, -10, 6, 21)
    rafters = (-23, 0) if simplified else (-23, -8, 8)

    # Far wall, then transverse work, then the visible front wall.
    for u in studs:
        beam(u, -19, 0, 4, 4, 33)
    beam(-25, -19, 33, 50, 4, 4)
    beam(-25, -15, 0, 4, 30, 3)
    beam(-25, -15, 32, 4, 30, 4)
    beam(21, -15, 0, 4, 30, 3)
    beam(21, -15, 33, 4, 30, 4)
    beam(-25, -1.7, 50.5, 50, 3.4, 3.4)
    for u in rafters:
        rafter(u)
    for u in studs:
        beam(u, 15, 0, 4, 4, 33)
    beam(-25, 15, 0, 50, 4, 3)
    beam(-25, 15, 33, 50, 4, 4)
    rafter(23)
    if not simplified:
        s.line([p(22, 19, 29), p(22, 19, 33), p(25, 19, 33)], DETAIL)


def draw(s):
    timber_frame(s)

    def lens(u, v):
        return 26 + .577 * u - .385 * v, 20 - .577 * u - .385 * v, 36 + .77 * v

    face_magnifier(s, lens, 0, 0, 15, direction=(.84, -.54))
