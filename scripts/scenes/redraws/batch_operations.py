from geometry import oval
from scenes.redraws._w2 import face_arrow, request_card

DESCRIPTION = "One continuous arrow sweeps over a fanned stack of operation cards."


def draw(s):
    def plane(x, z):
        return .85*x, -.15*x - .48*z, .83*z

    for offset in (28, 14, 0):
        def point(x, z):
            return plane(x + offset, z + offset*.58)

        request_card(s, point, 76, 60, print_rows=False)

    face_arrow(s, plane, oval(53, 26, 68, 46, 193, 376, 30), head=10)
