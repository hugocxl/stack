from geometry import DETAIL, EDGE, oval

DESCRIPTION = "A low-walled floor plan shows four connected rooms with gaps and arcs for swinging doors."


def door_swing(s, x, y, radius, start, end):
    arc = oval(x, y, radius, radius, start, end, 24)
    s.line([(x, y, 3), (*arc[0], 3)], DETAIL)
    s.line([(u, v, 3) for u, v in arc], DETAIL)


def draw(s):
    s.box(-44, -35, 0, 88, 70, 3, 1)
    for x, angle, back in ((-10, 180, 270), (10, 0, -90)):
        door_swing(s, x, -8, 13, angle, back)
        door_swing(s, x, 8, 13, angle, 90)
    door_swing(s, 8, 33, 15, 270, 180)

    walls = [(-44, -35, 88, 3), (-44, -32, 3, 64), (41, -32, 3, 64),
             (-44, 32, 36, 3), (8, 32, 36, 3),
             (-41, -2, 30, 3), (11, 2, 30, 3)]
    for x in (-11, 8):
        walls.extend((x, y, 3, depth) for y, depth in ((-32, 11), (-8, 16), (21, 11)))
    for x, y, width, depth in walls:
        s.box(x, y, 3, width, depth, 6, .5, EDGE)
