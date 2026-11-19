from geometry import EDGE, oval
from scenes.redraws._w3 import sheet

DESCRIPTION = "A long wire paperclip grips the folded corner of a ruled text sheet."


def draw(s):
    page = sheet(s, 72, 81, rise=(-.62, .78), depth=4)
    page.rules(12, 60, [24], ink=EDGE)
    page.rules(12, 47, [39, 45, 35, 41, 22], gap=8)
    # The back leg disappears behind the page and the wire turns over its top edge.
    path = [page.point(49, 69, 3), page.point(49, 82, 3)]
    path += [page.point(49, 82 + v, depth) for depth, v in
             oval(1, 0, 3, 3, 0, 180, 16)]
    path += [page.point(49, 62, -2)]
    path += [page.point(u, v, -2) for u, v in oval(56, 62, 7, 7, 180, 360, 20)]
    path += [page.point(63, 75, -2)]
    path += [page.point(u, v, -2) for u, v in oval(59, 75, 4, 4, 0, 180, 16)]
    path += [page.point(55, 65, -2)]
    s.tube(path, 1.15, EDGE)
