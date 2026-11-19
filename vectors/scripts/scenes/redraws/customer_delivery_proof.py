from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "A checked photo print shows a delivered parcel on a doorstep."


def draw(s):
    def print_point(u, v, depth=0):
        return (u * .78 + depth, -u * .42 + depth - v * .08, v)

    def frame(points, depth, ink=EDGE):
        s.face([print_point(u, v, depth) for u, v in points], ink)

    def stroke(points, ink=EDGE):
        s.line([print_point(u, v) for u, v in points], ink)

    corners = [(-39, 0), (39, 0), (39, 63), (-39, 63)]
    frame(corners, -4)
    for a, b in ((corners[1], corners[2]), (corners[2], corners[3])):
        s.face([print_point(*a, -4), print_point(*b, -4), print_point(*b), print_point(*a)], EDGE)
    frame(corners, 0)
    stroke([(-33, 12), (33, 12), (33, 57), (-33, 57), (-33, 12)], DETAIL)
    stroke([(-27, 26), (-27, 53), (1, 53), (1, 26), (-27, 26)])
    stroke([(-32, 26), (-23, 22), (17, 22)], DETAIL)
    stroke([(-8, 39), (-5, 39)], EDGE)

    frame([(0, 31), (15, 38), (28, 31), (13, 23)], .1)
    frame([(13, 23), (28, 31), (28, 20), (13, 14)], .1)
    frame([(0, 31), (13, 23), (13, 14), (0, 20)], .1)
    stroke([(8, 35), (21, 27), (21, 23)], DETAIL)
    badge(s, "check", *print_point(34, 10, 2), 9.5)
