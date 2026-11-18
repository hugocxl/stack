from geometry import DETAIL, EDGE
from scenes.redraws._kit import badge
from scenes.redraws._w4 import front_surface

DESCRIPTION = "A meditation class pass bears a lotus pictogram and an attendance check badge."


def meditation_pass(s):
    """Use one thick, notched class pass for the two meditation states."""
    face = front_surface(s, angle=-31, z=5, lean=.45)
    face.slab([(3, 0), (77, 0), (82, 4), (82, 21), (77, 25), (82, 29),
               (82, 46), (77, 50), (3, 50), (0, 47), (0, 29), (5, 25),
               (0, 21), (0, 3)], 5)
    face.line([(63, 5), (63, 45)], DETAIL, dashed=True)
    face.outline([(32, 17), (27, 22), (26, 29), (32, 38),
                  (38, 29), (37, 22)], EDGE)
    face.line([(32, 17), (23, 18), (16, 23), (13, 31), (21, 30), (26, 27)], EDGE)
    face.line([(32, 17), (41, 18), (48, 23), (51, 31), (43, 30), (38, 27)], EDGE)
    face.line([(23, 12), (41, 12)], DETAIL)
    return face


def draw(s):
    face = meditation_pass(s)
    badge(s, "check", *face.at(74, 43), 12)
