from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w5 import panel, plane_mark, train_mark

DESCRIPTION = "Two notched travel tickets showing a train and an airplane protrude from a single stitched wallet pocket."


def draw(s):
    face = lambda x, z: (x, -z*.50, z)
    panel(s, rounded(0, 0, 67, 41, 3.5), face, 6)

    for x, z, offset in ((2, 55, 0), (35, 46, 3.1)):
        ticket = lambda a, b: (a, -b*.50 + offset, b)
        outline = [(x, 13), (x + 29, 13), (x + 29, z), (x + 20, z),
                   (x + 17, z - 3), (x + 14, z), (x, z)]
        s.face([ticket(a, b) for a, b in outline], EDGE)
        if offset:
            plane_mark(s, ticket, x + 15, z - 13, .68)
        else:
            train_mark(s, ticket, x + 14.5, z - 16, .69)

    front = lambda x, z: (x, -z*.50 + 5.5, z)
    pocket = [(0, 3), (3, 0), (64, 0), (67, 3), (67, 29), (48, 29),
              (44, 25), (23, 25), (19, 29), (0, 29)]
    s.face([front(a, b) for a, b in pocket])
    s.line([front(a, b) for a, b in [(4, 24), (4, 5), (63, 5), (63, 24)]], DETAIL, dashed=True)
