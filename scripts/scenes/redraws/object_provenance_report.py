from geometry import EDGE
from scenes.redraws._w3 import spiral_notebook
from scenes.redraws.object_condition_report import vase_outline

DESCRIPTION = "A spiral accession record places a vase drawing above three ownership entries on a vertical timeline."


def draw(s):
    face = spiral_notebook(s, w=72, h=86)
    vase_outline(face, 37, 60, 32)
    face.rules(14, 42, [48])
    face.stroke([(20, 13), (20, 36)], EDGE)
    for v, long in ((36, 30), (25, 24), (14, 28)):
        face.rules(16, v, [8], ink=EDGE)
        face.rules(29, v + 2, [long], ink=EDGE)
        face.rules(29, v - 3, [15])
