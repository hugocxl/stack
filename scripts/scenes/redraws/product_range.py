from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w4 import front_surface, upright

DESCRIPTION = "Three matching two-way loudspeakers stand in a row from smallest to largest."


def speaker(s, u, z, scale, *, angle):
    """Build a deep loudspeaker cabinet with a tweeter and recessed woofer."""
    width, height = 34*scale, 52*scale
    upright(s, rounded(u, z, width, height, 4*scale), 0, 17*scale, angle=angle)
    face = front_surface(s, angle=angle, z=z)
    center = u + width/2
    for v, r, ink in ((39.5, 4.6, EDGE), (19, 11, EDGE), (19, 5, DETAIL)):
        face.oval(center, v*scale, r*scale, r*scale, ink)


def draw(s):
    for u, scale in ((0, .67), (39, .89), (88, 1.16)):
        speaker(s, u, 0, scale, angle=-5)
