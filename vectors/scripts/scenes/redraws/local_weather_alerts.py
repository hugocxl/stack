from geometry import BOLD, oval
from scenes.redraws._kit import warning
from scenes.redraws._w1 import upright_profile

DESCRIPTION = "A storm cloud gives off a lightning bolt and carries an exclamation triangle."


def draw(s):
    cloud = [
        *oval(-24, 43, 18, 16, 270, 108, 24),
        *oval(0, 48, 24, 24, 156, 31, 30),
        *oval(25, 43, 17, 16, 111, -90, 26),
    ]
    bolt = [(-5, 32), (-18, 13), (-6, 13), (-11, -7), (10, 20), (-1, 20), (5, 32)]
    upright_profile(s, [(x - 5, z) for x, z in bolt], 3, 3, BOLD)
    upright_profile(s, cloud, 5, 8)
    warning(s, 31, 11, 24, 31)
