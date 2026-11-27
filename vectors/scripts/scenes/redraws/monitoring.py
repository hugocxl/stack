from geometry import BOLD, DETAIL
from scenes.redraws._sf import display

DESCRIPTION = "A display on a stand traces a live pulse across a faint baseline grid."


def draw(s):
    face = display(s, 112, 70)
    for v in (22, 35, 48):
        s.line([face(12, v), face(100, v)], DETAIL, dashed=True)
    trace = [(12, 35), (38, 35), (44, 46), (50, 18), (57, 56), (63, 30), (68, 35), (100, 35)]
    s.line([face(u, v) for u, v in trace], BOLD)
