from math import cos, radians, sin

from geometry import EDGE, oval

DESCRIPTION = "A solid pie chart separates three unequal portfolio slices along visible radial cuts."


def pie_slices(s, slices, *, radius=43, depth=12):
    """Draw the visible walls and top of each separated pie slice."""
    def points(start, end, gap):
        mid = radians((start + end) / 2)
        cx, cy = gap * cos(mid), gap * sin(mid)
        return [(cx, cy), *oval(cx, cy, radius, radius, start, end, 38)]

    def surface(x, y):
        return x, y, depth + 12 - .14 * (x + y)

    def draw_slice(outline):
        top = [surface(x, y) for x, y in outline]
        wall = []
        for a, b in zip(top, top[1:] + top[:1]):
            if b[1] - a[1] > b[0] - a[0]:
                if not wall:
                    wall.append(a)
                wall.append(b)
            elif wall:
                draw_wall(wall)
                wall = []
        if wall:
            draw_wall(wall)
        s.face(top, EDGE)

    def draw_wall(top):
        bottom = [(x, y, z - depth) for x, y, z in reversed(top)]
        s.face(top + bottom, EDGE)

    # The far slices go first so the front slice hides their cut walls.
    for start, end, gap in slices:
        draw_slice(points(start, end, gap))
    return surface


def draw(s):
    pie_slices(s, ((172, 264, 5), (264, 358, 10), (-2, 172, 4)))
