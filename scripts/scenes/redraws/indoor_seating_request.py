from geometry import DETAIL, EDGE
from scenes.redraws._w5 import food_table

DESCRIPTION = "A dining table set for two stands inside a restaurant alcove beneath a framed interior window."


def draw(s):
    s.box(0, 0, -3, 80, 60, 3, 1)
    s.box(0, 3, 0, 3, 56, 54, 1)
    wall = lambda x, z: (x, 4, z)
    frame = [wall(0, 0), wall(80, 0), wall(80, 54), wall(0, 54)]
    window = [wall(15, 28), wall(47, 28), wall(47, 47), wall(15, 47)]
    s.face(frame, openings=[window])
    s.face([(x, 1, z) for x, _, z in window], DETAIL)
    s.line([wall(31, 28), wall(31, 47)], EDGE)
    s.line([wall(15, 37), wall(47, 37)], EDGE)
    s.box(13, 3, 26.5, 36, 3.8, 1.8, .7)
    s.face([wall(0, 54), wall(80, 54), (80, 0, 54), (0, 0, 54)])
    s.face([wall(80, 0), wall(80, 54), (80, 0, 54), (80, 0, 0)])
    food_table(s, 16, 13, scale=.84)
