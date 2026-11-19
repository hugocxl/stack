from geometry import DETAIL, EDGE
from scenes.redraws._w5 import harvest_crate, rect

DESCRIPTION = "A full harvest crate has a clipped batch label with two ruled lines on its front slat."


def draw(s):
    harvest_crate(s)
    face = lambda x, z: (x, 34.6, z)
    rect(s, face, 28, 2.5, 21, 18, 1.5)
    s.tube([face(36, 19.5), (36, 33, 22), (42, 33, 22), face(42, 19.5)], .8)
    s.line([face(32, 13), face(45, 13)], EDGE)
    s.line([face(32, 8), face(42, 8)], DETAIL)
