from geometry import BOLD, DETAIL, oval
from scenes.redraws._w2 import draft_notebook, face_arrow, rule

DESCRIPTION = "A partially written page on a spiral desk pad has a curved return arrow below its writing."


def written_draft(s):
    point = draft_notebook(s)
    for z, width in ((69, 50), (57, 56), (45, 34)):
        rule(s, point, 13, z, width)
    s.line([point(52, 40), point(52, 50)], DETAIL)
    return point


def draw(s):
    point = written_draft(s)
    turn = oval(54, 25, 17, 12, 36, -90, 18)
    face_arrow(s, point, [*turn, (23, 13)], BOLD, head=10)
