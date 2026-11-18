from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws.next_bus_countdown import wheel_side

DESCRIPTION = "A striped clearance bar hangs from a parking gantry just above a car roof."


def car(s):
    near, far = 36, 8
    for x in (14, 57):
        wheel_side(s, x, near - .8, 7.4)

    profile = [(0, 9), (0, 17), (8, 22), (15, 24), (24, 36), (42, 36),
               (53, 25), (66, 22), (71, 18), (71, 9)]
    for (a, z), (b, h) in zip(profile[1:-1], profile[2:]):
        s.face([(a, far, z), (b, far, h), (b, near, h), (a, near, z)], EDGE)
    arches = [(a, near, z) for x in (57, 14) for a, z in oval(x, 9, 8.6, 8.6, 0, 180, 26)]
    s.face([*[(x, near, z) for x, z in profile], *arches], EDGE)
    s.face([(71, far, 9), (71, far, 18), (71, near, 18), (71, near, 9)], EDGE)

    s.face([(44, near, 33.5), (51, near, 25.4), (35, near, 25.4), (35, near, 33.5)])
    s.face([(32, near, 33.5), (25, near, 33.5), (19, near, 25.4), (32, near, 25.4)])
    s.line([(35, near, 25.4), (35, near, 13), (43, near, 13)], DETAIL)
    s.line([(46, near, 27), (46, near, 21.5), (41, near, 21.5)], DETAIL)
    s.face([(45, far + 3, 33), (51, far + 3, 27), (51, near - 3, 27), (45, near - 3, 33)])
    for y in (far + 3, near - 8):
        s.line([(71, y, 15), (71, y + 5, 15)], EDGE)
    s.line([(71, 19, 12), (71, 25, 12)], DETAIL)


def draw(s):
    s.box(29, 0, 0, 4.5, 5, 60, 1)
    car(s)
    s.box(29, 41, 0, 4.5, 5, 60, 1)
    s.box(29, 0, 58, 5, 46, 4, .8)
    for y in (8, 38):
        s.line([(35, y, 58), (35, y, 46)], EDGE)
    s.box(33, 4, 39, 4.5, 38, 8, .8, BOLD)
    for y in (6, 13, 20, 27, 34):
        s.line([(37.5, y, 40.3), (37.5, y + 4, 45.6)], DETAIL)
