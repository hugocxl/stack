from geometry import DETAIL, EDGE
from scenes.redraws._kit import arrow, badge
from scenes.redraws._w2 import laptop
from scenes.redraws._w4 import Surface

DESCRIPTION = "An open laptop shows a kettlebell swing diagram in a video with a play badge."


def draw(s):
    point = laptop(s, width=100, height=65)
    screen = Surface(s, point)
    screen.outline([(24, 21), (19, 24), (17, 30), (19, 37),
                    (25, 42), (23, 47), (26, 51), (40, 51),
                    (44, 47), (42, 42), (47, 38), (49, 32),
                    (47, 25), (41, 21)], EDGE)
    screen.line([(28, 42), (28, 47), (39, 47), (39, 42), (28, 42)], EDGE)
    arrow(s, [point(54, 27), point(64, 31), point(71, 38),
              point(73, 43), point(73, 51)], EDGE, head=6)
    screen.line([(13, 15), (87, 15)], DETAIL)
    badge(s, "play", *point(90, 19), 12)
