from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws._w5 import inbox_base, inbox_front, panel

DESCRIPTION = "Two sheets occupy one side of an import tray with an exclamation triangle on its open corner."


def draw(s):
    inbox_base(s)
    for offset in (7, 0):
        def face(x, z):
            return x + .65*offset, 33 - .57*z - offset, 4 + z + .38*offset

        panel(s, [(28, 0), (58, 0), (58, 36), (50, 44), (28, 44)], face, 2.2)
    s.line([face(50, 44), face(50, 36), face(58, 36)], EDGE)
    for z, end in ((29, 50), (21, 51), (14, 46)):
        s.line([face(34, z), face(end, z)], DETAIL)
    inbox_front(s)
    warning(s, 7, 42, -3, 29)
