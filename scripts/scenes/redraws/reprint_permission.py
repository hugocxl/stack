from geometry import EDGE, rounded
from scenes.redraws._kit import badge
from scenes.redraws._w4 import landscape, paper

DESCRIPTION = "A print proof with trim marks and a two-column layout carries an open-padlock badge."


def draw(s):
    proof = paper(s, 89, pitch=.22, angle=-29, depth=3)
    proof.slab(rounded(0, 0, 99, 89, 2), 3)
    proof.frame(15, 15, 69, 59, 1)
    proof.rows(22, 24, (54,), ink=EDGE)
    landscape(proof, 22, 33, 25, 30)
    proof.rows(52, 34, (25, 23, 24, 19, 23), step=6)
    for u, v, dx, dy in ((15, 15, -1, -1), (84, 15, 1, -1), (15, 74, -1, 1), (84, 74, 1, 1)):
        proof.line([(u + 3*dx, v), (u + 10*dx, v)], EDGE)
        proof.line([(u, v + 3*dy), (u, v + 10*dy)], EDGE)
    badge(s, "unlock", *proof.at(96, 20), 20)
