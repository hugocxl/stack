from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface
from scenes.redraws.peer_feedback import conversation

DESCRIPTION = "A tripod studio easel displays a mountain sketch with a speech bubble attached to the canvas."


def draw(s):
    s.tube([(37, 0, 1), (35, 31, 74)], 2.8)
    for x in (2, 68):
        s.tube([(x, 45, 2), (35, 25, 99)], 2.6)
    canvas = Surface(s, (0, 42, 29), rise=(-.27, .96), back=(0, -.96, -.27))
    canvas.plate(rounded(0, 0, 70, 60, 2), 4)
    canvas.oval(42, 43, 5.5, 5.5, EDGE)
    canvas.stroke([(9, 16), (24, 38), (36, 22), (43, 30), (56, 16)], BOLD)
    canvas.stroke([(18, 29), (22, 27), (26, 31), (30, 29)], EDGE)
    canvas.stroke([(10, 11), (49, 11)])
    s.box(-3, 39, 24, 77, 9, 5, 1)
    comment = Surface(s, (55, 38, 57))
    conversation(comment, 0, 0, 36, 26)
