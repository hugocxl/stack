from geometry import EDGE, oval
from scenes.redraws._kit import arrow, badge
from scenes.redraws._w3 import Surface

DESCRIPTION = "A large circular retry arrow loops around three empty attempt slots and meets an X badge at its lower corner."


def retry_ring(s, *, start=-62, end=-290):
    """Draw a viewer-facing retry loop with room beside its tail for a badge."""
    face = Surface(s, (0, 0, 40), rise=(0, 1.155), across=(.577, -.577))
    track = [face.point(x, z) for x, z in oval(0, 0, 34, 34, start, end, 64)]
    arrow(s, track, EDGE, head=10)
    return face


def draw(s):
    retry = retry_ring(s)
    for x in (-12, 0, 12):
        retry.oval(x, 0, 3.65, 3.65, EDGE)
    badge(s, "x", *retry.point(23, -27), 13)
