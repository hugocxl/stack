from geometry import BOLD, DETAIL, EDGE
from scenes.redraws._w5 import folded_sheet, rect

DESCRIPTION = "A folded-corner file shows a boxed filename selection with a tall editing caret."


def draw(s):
    face = folded_sheet(s, 58, 60, lean=.52)
    rect(s, face, 7, 29, 44, 14, 1.5, EDGE)
    s.line([face(11, 34.5), face(31, 34.5)], EDGE)
    s.line([face(11, 38), face(23, 38)], DETAIL)
    s.line([face(36, 27), face(36, 45)], BOLD)
    s.line([face(33, 27), face(39, 27)], BOLD)
    s.line([face(33, 45), face(39, 45)], BOLD)
    for z, end in ((19, 34), (11, 41)):
        s.line([face(9, z), face(end, z)], DETAIL)
