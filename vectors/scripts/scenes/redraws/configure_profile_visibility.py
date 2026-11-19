from geometry import BOLD, oval
from scenes.redraws._w1 import profile_card

DESCRIPTION = "A profile card has an eye symbol printed below its account details."


def draw(s):
    profile_card(s, -34, 0, 0, rows=((34, 22), (27, 16)))
    upper = oval(17, 3, 14, 17, 43, 137, 24)
    lower = oval(17, 26, 14, 17, 223, 317, 24)
    s.line([(x, 0, z) for x, z in [*upper, *lower, upper[0]]], BOLD)
    s.line([(x, 0, z) for x, z in oval(17, 14.5, 3.6, 3.6, count=28)], BOLD)
