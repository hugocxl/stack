from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A nutrition panel on a gable-top carton emphasizes one nutrient row between heavy section rules."


def draw(s):
    angle = -22
    panel = front_surface(s, angle=angle, y=0)

    def point(u, y, z):
        x, depth, height = panel.at(u, z)
        return x + .375*y, depth + .927*y, height

    s.face([point(0, -31, 0), point(78, -31, 0), point(78, -31, 84),
            point(0, -31, 84)], DETAIL)
    s.face([point(78, 0, 0), point(78, -31, 0), point(78, -31, 84),
            point(78, -15.5, 98), point(78, 0, 84)])
    s.face([point(0, 0, 84), point(78, 0, 84), point(78, -15.5, 98),
            point(0, -15.5, 98)])
    s.face([point(0, -15.5, 98), point(78, -15.5, 98), point(78, -15.5, 103),
            point(0, -15.5, 103)], EDGE)
    s.face([panel.at(0, 0), panel.at(78, 0), panel.at(78, 84), panel.at(0, 84)])
    panel.frame(8, 8, 62, 68, 1, EDGE)
    panel.rows(13, 69, (41,), ink=BOLD)
    panel.rows(13, 63, (28,), ink=DETAIL)
    for z in (56, 29):
        panel.rows(9, z, (60,), ink=BOLD)
    for z in (48, 22, 15):
        panel.rows(13, z, (23,), ink=DETAIL)
        panel.rows(55, z, (10,), ink=DETAIL)
    panel.frame(12, 34, 54, 10, 1, EDGE)
    panel.rows(16, 39, (25,), ink=BOLD)
    panel.rows(53, 39, (9,), ink=BOLD)
