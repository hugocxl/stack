from geometry import DETAIL, EDGE, rounded
from scenes.redraws._kit import warning
from scenes.redraws._w5 import panel

DESCRIPTION = "A message envelope sits in an open inbox tray with a warning triangle attached to its upper corner."


def draw(s):
    s.box(0, 0, 0, 65, 46, 4, 2.4)
    s.face([(0, 0, 4), (65, 0, 4), (65, 0, 15), (0, 0, 15)], DETAIL)
    s.face([(0, 0, 4), (0, 46, 4), (0, 46, 13), (0, 0, 15)], DETAIL)
    envelope = lambda x, z: (x, 35 - .56 * z, z)
    panel(s, rounded(7, 5, 49, 32, 2), envelope, 2.1, EDGE)
    s.line([envelope(8, 35), envelope(31.5, 20), envelope(54, 35)], EDGE)
    s.face([(65, 0, 4), (65, 46, 4), (65, 46, 13), (65, 0, 15)], EDGE)
    s.face([(0, 46, 4), (65, 46, 4), (65, 46, 13), (42, 46, 13),
            (39, 46, 8), (25, 46, 8), (22, 46, 13), (0, 46, 13)], EDGE)
    warning(s, 54, 22, 25, 24)
