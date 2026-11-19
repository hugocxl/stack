from geometry import BOLD
from scenes.redraws._w4 import article_sections, nav_article, nav_path

DESCRIPTION = "A bent navigation arrow runs down the article margin and lands beside the middle section heading."


def draw(s):
    face = nav_article(s)
    article_sections(face)
    nav_path(face, [(52, 77), (68, 77), (68, 45), (49, 45)], BOLD, head=9)
