from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w2 import chart_line, closed_outline, upright_face

DESCRIPTION = "A thick tool picker presents three choices with a check badge beside the wrench."


def draw(s):
    def point(x, z):
        return .76*x, -.24*x - .15*z, z

    upright_face(s, point, rounded(0, 0, 103, 61, 7), 11)
    for x in (7, 35, 63):
        closed_outline(s, point, rounded(x, 11, 25, 37, 3), DETAIL)
    hammer = [(13, 38), (29, 38), (29, 32), (24, 32), (24, 20), (20, 20),
              (20, 32), (13, 32), (13, 38)]
    driver = [(40, 21), (46, 29), (48, 27), (55, 38), (57, 37), (51, 25),
              (53, 23), (46, 16), (40, 21)]
    chart_line(s, point, hammer, EDGE)
    chart_line(s, point, driver, EDGE)
    wrench = [(68, 21), (76, 34), (75, 39), (79, 44), (82, 44), (80, 39),
              (84, 37), (88, 41), (88, 37), (84, 33), (80, 32), (73, 19), (68, 21)]
    chart_line(s, point, wrench, EDGE)
    badge(s, "check", *point(104, 57), 11)
