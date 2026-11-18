from geometry import BOLD, DETAIL, EDGE, oval, rounded
from scenes.redraws._kit import coin
from scenes.redraws._w4 import upright

DESCRIPTION = "A folded-corner document with ruled lines carries an open-padlock badge."


def draw(s):
    upright(s, [(0, 0), (65, 0), (65, 66), (46, 85), (0, 85)], 0, 4)
    s.line([(46, 0, 85), (46, 0, 66), (65, 0, 66)], EDGE)
    s.line([(9, 0, 69), (33, 0, 69)], EDGE)
    for z, width in ((53, 44), (43, 40), (33, 44), (23, 30), (13, 21)):
        s.line([(9, 0, z), (9 + width, 0, z)], DETAIL)

    y = coin(s, 62, 4, 21, 20)
    body = [(x, y, z) for x, z in rounded(51, 10, 22, 12, 2)]
    s.line([*body, body[0]], BOLD)
    shackle = [(x, y, z) for x, z in oval(62, 29, 8, 9, 180, 25, 24)]
    s.line([(54, y, 22), *shackle], BOLD)
    s.line([(62, y, 18), (62, y, 14)], EDGE)
