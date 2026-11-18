from geometry import DETAIL, EDGE
from scenes.redraws._w1 import laptop, prompt

DESCRIPTION = "A laptop terminal shows a build command followed by four aligned rows of log output."


def draw(s):
    y = laptop(s, -36, -10, h=52)
    prompt(s, -25, y, 43, 4)
    s.line([(-8, y, 42), (22, y, 42)], EDGE)
    for z, width in ((32, 31), (26, 35), (20, 25), (14, 30)):
        s.line([(-25, y, z), (-17, y, z)], DETAIL)
        s.line([(-12, y, z), (-12 + width, y, z)], DETAIL)
