from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A surveyed parcel has a bold property boundary and a crosshair at every corner."


def draw(s):
    foot = [(0, 10), (26, 0), (97, 0), (106, 19), (106, 69),
            (78, 80), (0, 74)]
    s.solid(foot, 0, 7, crease=False)
    s.line([(x, y, 7) for x, y in [*foot, foot[0]]], EDGE)

    # Road edge and one building footprint give the parcel its map context.
    s.line([(14, 8, 7), (23, 27, 7), (23, 70, 7)], DETAIL)
    s.line([(20, 5, 7), (29, 25, 7), (29, 72, 7)], DETAIL)
    corners = [(36, 14), (85, 12), (93, 57), (37, 64)]
    s.line([(x, y, 7) for x, y in [*corners, corners[0]]], BOLD)
    s.line([(53, 27, 7), (70, 27, 7), (70, 37, 7), (76, 37, 7),
            (76, 46, 7), (53, 46, 7), (53, 27, 7)], DETAIL)
    for x, y in corners:
        s.line([(x - 5, y, 7), (x + 5, y, 7)], EDGE)
        s.line([(x, y - 5, 7), (x, y + 5, 7)], EDGE)
