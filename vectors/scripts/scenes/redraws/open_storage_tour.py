from geometry import DETAIL, EDGE, oval, rounded
from scenes.redraws._w3 import Surface, ticket_outline
from scenes.redraws.public_collection_access import cabinet_frame, cabinet_shell

DESCRIPTION = "An admission ticket overlaps the open glass door of a museum cabinet containing a ring sculpture."


def draw(s):
    cabinet_shell(s, width=58)
    for v in (3, 36):
        s.box(3, 3, v, 52, 27, 3, 1)
    s.box(15, 17, 39, 23, 9, 4, 1)
    upper = Surface(s, (0, 25, 0))
    outer = oval(26, 56, 11, 13, count=36)[:-1]
    inner = oval(26, 56, 6.5, 8, count=36)[:-1]
    s.face([upper.point(*p) for p in outer], openings=[[upper.point(*p) for p in inner]])
    cabinet_frame(s, width=58)
    drawer = Surface(s, (0, 31, 0))
    drawer.plate(rounded(5, 7, 48, 27, 2), 1.5)
    drawer.rect(22, 23, 14, 4, 2, EDGE)

    def door(u, v):
        return (.24 * u, 31 + .97 * u, v)

    s.face([door(u, v) for u, v in rounded(0, 3, 39, 79, 2)],
           openings=[[door(u, v) for u, v in rounded(4, 8, 31, 68, 2)]])
    s.line([door(11, 64), door(24, 73)], DETAIL)
    s.line([door(12, 54), door(28, 65)], DETAIL)
    s.line([door(34, 32), door(34, 45)], EDGE)
    ticket = Surface(s, (-12, 61, 10))
    ticket.plate([(u * .34, v * .34) for u, v in ticket_outline()], 2)
    ticket.stroke([(24, 2), (24, 14)], DETAIL, dashed=True)
    ticket.rules(7, 10, [12], ink=EDGE)
    ticket.rules(7, 5, [9], ink=DETAIL)
