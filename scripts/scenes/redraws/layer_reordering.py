from geometry import BOLD, DETAIL
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import design_layer

DESCRIPTION = "One design sheet is raised above two matching sheets beside an upward reorder arrow."


def draw(s):
    design_layer(s, (0, 0, 4), ink=DETAIL)
    design_layer(s, (1, 14, 10))
    top = design_layer(s, (4, 28, 44))
    top.oval(42, 31, 13, 12, DETAIL)
    arrow(s, [(126, -21, 29), (126, -21, 78)], BOLD, head=11)
