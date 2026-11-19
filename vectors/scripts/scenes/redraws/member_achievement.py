from geometry import BOLD
from scenes.redraws._w3 import printed_glyph
from scenes.redraws.lifetime_member_recognition import ribbon_medal

DESCRIPTION = "A ribbon medallion displays one large embossed star."


def draw(s):
    printed_glyph(ribbon_medal(s), "star", 0, 0, 25, BOLD)
