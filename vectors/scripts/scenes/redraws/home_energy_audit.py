from geometry import EDGE, oval
from scenes.redraws._kit import glyph
from scenes.redraws._w1 import cable_sleeve
from scenes.redraws.program_impact import community_house

DESCRIPTION = "A magnifying glass frames the round electricity meter mounted beside a house door."


def draw(s):
    community_house(s)
    s.line([(18, 18, 6), (18, 18, 19)], EDGE)
    cable_sleeve(s, 18, 18, 21, 24, 6, 1.4)
    glyph(s, "bolt", 18, 21, 24, 4.1)
    s.tube([(25.5, 23, 15), (36, 23, 4)], 2.7)
    for radius in (12, 9.4):
        s.line([(x, 23, z) for x, z in oval(18, 24, radius, radius, count=40)], EDGE)
