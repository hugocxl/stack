from geometry import EDGE
from scenes.redraws._w1 import lectern, upright_profile

DESCRIPTION = "A speech bubble connects to the gooseneck microphone on a public-hearing lectern."


def draw(s):
    lectern(s)
    outline = [(-16, 66), (-16, 83), (-12, 87), (31, 87), (35, 83),
               (35, 66), (31, 63), (-2, 63), (-14, 65), (-16, 63)]
    upright_profile(s, outline, -7, 3)
    for z, right in ((78, 26), (71, 19)):
        s.line([(-7, -7, z), (right, -7, z)], EDGE)
