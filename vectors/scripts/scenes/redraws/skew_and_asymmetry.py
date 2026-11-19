from geometry import BOLD, EDGE, rounded

DESCRIPTION = "A histogram rises to an early peak and falls into a long series of low bars on the right."


def draw(s):
    for i, height in enumerate((25, 62, 57, 39, 26, 17, 12, 8, 5)):
        x = i * 13
        s.solid(rounded(x, 0, 13, 19, .85), 0, height, ink=BOLD if i == 1 else EDGE)
