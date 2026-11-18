from geometry import EDGE, oval
from scenes.redraws._w2 import closed_outline, printed_glyph, rule, standing_notebook

DESCRIPTION = "A spiral checklist shows a house key above three square checkboxes."


def key_outline(s, point, x, z, size, ink=EDGE):
    """Print the key's bow, shaft, teeth and the opening through its bow."""
    profile = oval(-.48, 0, .37, .33, 25, 335, 36)
    profile += [(.81, -.14), (.91, -.03), (.91, .09), (.67, .09),
                (.67, .28), (.43, .28), (.43, .09), (.23, .09),
                (.23, .23), (.05, .23), (.05, .14)]
    closed_outline(s, point, [(x + u*size, z + v*size) for u, v in profile], ink)
    closed_outline(s, point, oval(x - .50*size, z, .13*size, .13*size), ink)


def checklist(s, point, x, z, width, *, marked):
    for i in range(3):
        y = z - i*15
        closed_outline(s, point, [(x, y), (x + 8, y), (x + 8, y + 8), (x, y + 8)], EDGE)
        if i in marked:
            printed_glyph(s, point, "check", x + 4, y + 4, 4.6, EDGE)
        rule(s, point, x + 15, y + 4, width - i*5)


def draw(s):
    point = standing_notebook(s, 67, 80)
    key_outline(s, point, 33, 57, 19)
    checklist(s, point, 12, 38, 26, marked=(0,))
