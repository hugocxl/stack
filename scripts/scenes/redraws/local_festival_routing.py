from geometry import BOLD, DETAIL, EDGE

DESCRIPTION = "A route crosses the folds of a wayfinding map to a festival stage."


def folded_map(s):
    """Open an accordion map on its lower edge and return its fold coordinates."""
    folds = ((0, 0), (29, -13), (58, 0), (87, -13))

    def point(x, v):
        index = min(2, int(x // 29))
        left, y0 = folds[index]
        right, y1 = folds[index + 1]
        return (x, y0 + (y1 - y0) * (x - left) / (right - left) - .24 * v, .97 * v)

    for (left, _), (right, _) in zip(folds, folds[1:]):
        face = [point(left, 0), point(right, 0), point(right, 56), point(left, 56)]
        s.face([(x, y - 1.6, z - .5) for x, y, z in face])
        s.face(face)
    return point


def map_path(s, point, points, ink=BOLD, *, dashed=False):
    """Keep every segment on the paper, including where it crosses a fold."""
    path = [points[0]]
    for (x0, v0), (x1, v1) in zip(points, points[1:]):
        between = [x for x in (29, 58) if min(x0, x1) < x < max(x0, x1)]
        for x in sorted(between, reverse=x1 < x0):
            path.append((x, v0 + (v1 - v0) * (x - x0) / (x1 - x0)))
        path.append((x1, v1))
    s.line([point(*p) for p in path], ink, dashed)


def draw(s):
    point = folded_map(s)
    map_path(s, point, [(7, 12), (18, 12), (22, 29), (34, 29),
                        (42, 19), (55, 19), (62, 24), (72, 24), (72, 31)])
    map_path(s, point, [(61, 31), (84, 31), (84, 50), (61, 50), (61, 31)], EDGE)
    map_path(s, point, [(61, 46), (84, 46)], EDGE)
    for a, b, c in ((69, 66, 64), (76, 79, 81)):
        map_path(s, point, [(a, 46), (b, 39), (c, 36), (b, 31)], EDGE)
    map_path(s, point, [(4, 41), (13, 45), (24, 43)], DETAIL)
    map_path(s, point, [(62, 11), (70, 15), (83, 15)], DETAIL)
