from math import sqrt

from geometry import BOLD

DESCRIPTION = "A mushroom emergency-stop button rises from a square housing and carries an outlined stop square."


def draw(s):
    center = 39
    s.box(0, 0, 0, 78, 78, 14, 7)
    s.disk(center, center, 14, 23, 23, 13)
    s.disk(center, center, 27, 34, 34, 12)
    corners = [(-11, -11), (11, -11), (11, 11), (-11, 11), (-11, -11)]
    # Compensate for the top face's foreshortening so the printed square reads upright.
    s.line([(center + (u + 2*v)/sqrt(3), center + (-u + 2*v)/sqrt(3), 39)
            for u, v in corners], BOLD)
