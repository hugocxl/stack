from geometry import DETAIL, EDGE
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import printed_stroke

DESCRIPTION = "An open takeaway carton holds a meal and bears a donation heart on its front flap."


def draw(s):
    lid = lambda x, z: (x, -.56 * (z - 16), z + 1)
    outline = [(0, 16), (63, 16), (64, 45), (60, 50), (4, 50), (-1, 45)]
    s.face([lid(x, z) for x, z in outline], EDGE)
    printed_stroke(s, lid, [(6, 22), (6, 43), (57, 43), (57, 22)], DETAIL)
    s.face([(0, 0, 17), (63, 0, 17), (60, 7, 0), (5, 7, 0)])
    s.face([(5, 7, 0), (60, 7, 0), (57, 42, 0), (8, 42, 0)], DETAIL)

    # A sandwich and a small portion of round sides sit below the rim.
    bread = [(10, 11), (37, 17), (38, 19), (15, 37), (12, 37), (9, 14)]
    s.solid(bread, 7, 10, crease=False)
    s.face([(x, y, 17) for x, y in bread], EDGE)
    s.line([(12, 37, 11), (15, 37, 11), (38, 19, 11)], DETAIL)
    for x, y in ((49, 18), (53, 28), (43, 30)):
        s.disk(x, y, 6, 4.6, 4.6, 5)
    s.face([(63, 0, 17), (66, 47, 17), (57, 42, 0), (60, 7, 0)])
    front = lambda x, z: (x, 42 + z * .30, z)
    shape = [(8, 0), (57, 0), (66, 17), (40, 17), (37, 20), (27, 20),
             (24, 17), (-1, 17)]
    s.face([front(x, z) for x, z in shape])
    glyph(s, "heart", *front(32, 9), 8.5, EDGE)
