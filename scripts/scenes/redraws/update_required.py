from scenes.redraws._kit import warning
from scenes.redraws.update_paused import software_package

DESCRIPTION = "A software package with a code mark and install slot carries a warning triangle at its right corner."


def draw(s):
    software_package(s)
    warning(s, 91, 10, 26, 35)
