from geometry import EDGE, oval
from scenes.redraws._w5 import harvest_crate, pin_outline

DESCRIPTION = "A produce crate carries a prominent location pin printed on a front label."


def draw(s):
    harvest_crate(s)
    pin = lambda x, z: (x, 34.3, z)
    s.face([pin(x, z) for x, z in pin_outline(38, 17, 8)])
    s.line([pin(x, z) for x, z in oval(38, 17, 3.2, 3.2)], EDGE)
