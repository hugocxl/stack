from geometry import DETAIL, EDGE

DESCRIPTION = "Three large active edge nodes connect to one small central network hub."


def draw(s):
    hub = (0, 0)
    edges = [(-32, -32), (37, -15), (-15, 37)]
    for x, y in edges:
        s.line([(*hub, 4), (x, y, 4)], EDGE)
    s.disk(*hub, 0, 5, 5, 7)
    for x, y in edges:
        s.disk(x, y, 0, 14, 14, 7)
        s.ellipse(x, y, 7, 10, 10, DETAIL)
        s.disk(x, y, 7, 4, 4, 3)
