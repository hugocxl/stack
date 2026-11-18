from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import landscape, paper

DESCRIPTION = "A landscape test print has a calibration strip with differently patterned swatches along its margin."


def draw(s):
    proof = paper(s, 78, pitch=.84, run=.36, angle=-20, depth=6)
    proof.slab(rounded(0, 0, 112, 78, 3), 6)
    landscape(proof, 9, 9, 70, 54)
    proof.frame(86, 9, 18, 59, 1, EDGE)
    for v in (24, 38, 52):
        proof.rows(86, v, (18,), ink=EDGE)
    for shift in (0, 4):
        proof.line([(90 + shift, 21), (98 + shift, 13)], DETAIL)
        proof.rows(90, 29 + shift, (10,))
        proof.line([(91 + shift, 58), (91 + shift, 64)], DETAIL)
    proof.line([(91, 42), (99, 48)], DETAIL)
    proof.line([(99, 42), (91, 48)], DETAIL)
