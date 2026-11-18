from geometry import BOLD, EDGE, oval
from scenes.redraws._kit import glyph
from scenes.redraws._w5 import harvest_crate, panel

DESCRIPTION = "A produce crate carries a tied traceability tag printed with a return arrow."


def draw(s):
    harvest_crate(s)
    s.tube([(41, 32, 22), (44, 33, 27), (48, 36, 23), (51, 38, 19)], 1.05)
    face = lambda x, z: (x, 38, z)
    panel(s, [(30, 3), (58, 3), (58, 15), (51, 23), (39, 23), (30, 15)], face, 2)
    s.line([(x, 38, z) for x, z in oval(50, 19, 1.6, 1.6, count=24)], EDGE)
    glyph(s, "back", 44, 38, 11.3, 10, BOLD)
