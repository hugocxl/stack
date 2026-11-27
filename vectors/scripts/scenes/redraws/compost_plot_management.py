from geometry import DETAIL, EDGE

DESCRIPTION = "An open slatted compost bin holds a rounded mound of leaves."


def draw(s):
    W, D, H = 76, 60, 26
    s.face([(0, 0, 0), (0, 0, H), (W, 0, H), (W, 0, 0)], EDGE)
    s.face([(0, 0, 0), (0, D, 0), (0, D, H), (0, 0, H)], EDGE)
    from scenes.redraws._sf import turned
    turned(s, [(.4, 18), (26, 18), (30, 26), (24, 40), (12, 49), (.4, 51)], W/2, D/2, 0, steps=4)
    for (a, b) in (((W/2 - 8, D/2 - 4, 50), (W/2 + 2, D/2 - 2, 52)), ((W/2 + 6, D/2 + 6, 47), (W/2 + 14, D/2 + 2, 45))):
        s.line([a, b], DETAIL)
    s.face([(W, 0, 0), (W, D, 0), (W, D, H), (W, 0, H)], EDGE)
    s.face([(0, D, 0), (W, D, 0), (W, D, H), (0, D, H)], EDGE)
    for z in (9, 18):
        s.line([(0, D, z), (W, D, z), (W, 0, z)], DETAIL)
