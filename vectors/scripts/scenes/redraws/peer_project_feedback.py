from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, speech_outline

DESCRIPTION = "A speech balloon attaches to a presentation easel displaying a simple project chart."


def draw(s):
    s.tube([(35, 1, 2), (35, 17, 72)], 1.9, DETAIL)
    s.tube([(6, 33, 2), (35, 17, 76), (64, 33, 2)], 2.2)
    board = Surface(s, (0, 24, 26), rise=(-.18, .98), back=(0, -.98, -.18))
    board.plate(rounded(0, 0, 71, 48, 3), 4)
    board.stroke([(9, 38), (30, 38)], EDGE)
    board.stroke([(13, 28), (13, 11), (61, 11)])
    board.stroke([(18, 15), (29, 23), (42, 19), (57, 34)], BOLD)
    s.tube([board.point(2, 0), board.point(68, 0)], 1.55)
    bubble = Surface(s, (0, 21, 26), rise=board.rise, back=board.back)
    bubble.plate(speech_outline(49, 42, 36, 27), 2)
    bubble.rules(56, 60, [22, 15], gap=7, ink=EDGE)
