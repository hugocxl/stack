from geometry import EDGE
from scenes.redraws._w4 import front_surface
from scenes.redraws.product_range import speaker

DESCRIPTION = "A branching family tree links an original loudspeaker to two differently sized descendant models."


def draw(s):
    tree = front_surface(s, angle=-23)
    tree.line([(52, 66), (52, 57)], EDGE)
    tree.line([(21, 38), (21, 57), (83, 57), (83, 43)], EDGE)
    speaker(s, 40, 66, .71, angle=-23)
    speaker(s, 10, 6, .64, angle=-23)
    speaker(s, 70, 3, .77, angle=-23)
