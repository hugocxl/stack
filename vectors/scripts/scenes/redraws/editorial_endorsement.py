from geometry import BOLD
from scenes.redraws._kit import badge
from scenes.redraws._w4 import bezier_path, speech_bubble

DESCRIPTION = "A thick quotation bubble carries a check badge on its upper-right corner."


def draw(s):
    quote = speech_bubble(s, width=86, height=60, angle=4, depth=7)
    mark = bezier_path(
        (10, 21), ((4, 24), (2, 32), (4, 38)),
        ((6, 45), (17, 45), (17, 37)), ((17, 32), (13, 30), (8, 31)),
        ((7, 28), (8, 25), (10, 21)),
    )
    for offset in (10, 27):
        quote.line([(u + offset, v) for u, v in mark], BOLD)
    quote.rows(50, 41, (18, 16, 11), step=-10)
    badge(s, "check", *quote.at(86, 52), 13)
