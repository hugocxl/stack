from geometry import DETAIL, EDGE, oval

DESCRIPTION = "A populated data table stands behind a small flask of sample liquid."


def draw(s):
    x, y = -16, 0
    s.box(x - 26, y - 5, 0, 75, 5, 54, 2)
    for z in (8, 18, 28, 38, 46):
        s.line([(x - 20, y, z), (x + 42, y, z)], EDGE if z == 38 else DETAIL)
    for column in (-20, 2, 22, 42):
        s.line([(x + column, y, 8), (x + column, y, 46)], DETAIL)
    for z, lengths in ((42, (11, 8, 9)), (33, (7, 9, 6)), (23, (11, 5, 8)), (13, (9, 7, 5))):
        for column, length in zip((-16, 6, 26), lengths):
            s.line([(x + column, y, z), (x + column + length, y, z)], EDGE)

    # The lip is seen from above and the liquid surface wraps around the flask.
    foot = oval(37, 9, 11, 11)[:-1]
    shoulder = oval(37, 9, 4.5, 4.5)[:-1]
    s.solid(foot, 0, 22, shoulder, crease=False)
    s.disk(37, 9, 22, 4.5, 4.5, 10)
    s.ellipse(37, 9, 32, 2.9, 2.9, DETAIL)
    s.ellipse(37, 9, 9, 8.3, 8.3, EDGE, -8, 98)
