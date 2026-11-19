from geometry import EDGE
from scenes.redraws._kit import arrow
from scenes.redraws._w4 import bezier_path, front_surface, phone_receiver

DESCRIPTION = "A curved return arrow sweeps back toward a telephone handset."


def draw(s):
    phone_receiver(s, z=22)
    plane = front_surface(s, angle=-24)
    sweep = bezier_path((32, 55), ((46, 76), (16, 90), (-13, 79)),
                        ((-26, 74), (-36, 67), (-37, 55)))
    arrow(s, [plane.at(u, v) for u, v in sweep], ink=EDGE, head=9)
