from geometry import EDGE, rounded
from scenes.redraws._w2 import closed_outline, rule
from scenes.redraws.project_planning import lane_card, planning_board

DESCRIPTION = "Three task cards fill every slot of a Kanban column capped by a three-position limit rail."


def draw(s):
    point = planning_board(s, lanes=1)
    # The cap displays three positions, echoed by the three occupied slots below.
    closed_outline(s, point, rounded(9, 79, 38, 13, 2), EDGE)
    for x in (17, 28, 39):
        closed_outline(s, point, rounded(x - 3.5, 82, 7, 7, 1), EDGE)
        rule(s, point, x - 1.5, 85.5, 3)
    for z in (12, 33, 54):
        lane_card(s, point, 0, z)
