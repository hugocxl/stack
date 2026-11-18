from geometry import BOLD, EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w2 import document_node, level_face

DESCRIPTION = "Three folded-corner document nodes are linked by a branching pair of citation arrows."


def draw(s):
    for dest in (68, 23):
        arrow(s, [level_face(33, 45), level_face(53, 45),
                  level_face(70, dest), level_face(83, dest)],
              BOLD if dest == 68 else EDGE, head=6)
    document_node(s, 6, 29, emphasis=True)
    document_node(s, 85, 50)
    document_node(s, 85, 5)
