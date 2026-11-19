from geometry import EDGE
from scenes.redraws.update_paused import software_package

DESCRIPTION = "A software package has a code mark on its lid and a downward arrow pointing into its install slot."


def draw(s):
    front = software_package(s)
    front.arrow([(42, 30), (42, 11)], EDGE, head=7)
