from geometry import EDGE
from scenes.redraws._w4 import article_sections, link_emblem, nav_article

DESCRIPTION = "A bound article shows a chain link directly beside the middle section heading."


def draw(s):
    face = nav_article(s)
    article_sections(face)
    face.line([(47, 45), (51, 45)], EDGE)
    link_emblem(face, 63, 46, 14)
