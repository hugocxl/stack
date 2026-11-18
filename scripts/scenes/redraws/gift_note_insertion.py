from geometry import DETAIL, EDGE
from scenes.redraws._w1 import open_carton_back, open_carton_front

DESCRIPTION = "A small handwritten card peeks out from beneath the front flap of an open ribboned gift carton."


def draw(s):
    carton = (-33, 33, -24, 24, 33)
    open_carton_back(s, *carton)

    def on_note(x, z):
        return x, 24 - (z - 27) * .28, z

    note = [(-17, 27), (19, 27), (19, 64), (-17, 64)]
    s.face([on_note(x, z) for x, z in note], EDGE)
    for z, width in ((55, 24), (48, 21), (41, 15)):
        s.line([on_note(-11 + x, z + offset) for x, offset in
                ((0, 0), (4, 1.2), (8, -.6), (12, .6), (width, 0))], DETAIL)

    open_carton_front(s, *carton, flap_depth=19, flap_drop=-9)
    for x in (-4, 4):
        s.line([(x, 24, 1), (x, 24, 33), (x, 43, 42)], DETAIL)
    for y in (-5, 5):
        s.line([(33, y, 1), (33, y, 33), (52, y, 42)], DETAIL)
