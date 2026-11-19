from geometry import BOLD, DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface, microphone

DESCRIPTION = "A smart display on a round speaker base shows a prominent microphone below a voice trace."


def draw(s):
    s.disk(45, 0, 0, 40, 27, 13)
    s.ellipse(45, 0, 7, 40, 27, DETAIL, start=0, end=90)
    s.box(28, -11, 12, 34, 19, 15, 4)
    panel = Surface(s, (0, 0, 21), rise=(-.22, .98), back=(0, -.98, -.22))
    panel.plate(rounded(0, 0, 90, 64, 8), 9)
    panel.rect(6, 6, 78, 52, 5, EDGE)
    panel.stroke([(31, 49), (37, 49), (41, 53), (45, 45), (49, 54),
                  (53, 49), (59, 49)], EDGE)
    button = Surface(s, panel.point(0, 0, -1.5), rise=panel.rise, back=panel.back)
    button.plate(rounded(28, 10, 34, 31, 13), 1.5)
    microphone(button, 45, 24, 24, BOLD)
