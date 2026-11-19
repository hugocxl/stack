from geometry import BOLD, oval
from scenes.redraws._w5 import luggage, luggage_tag, pin_outline

DESCRIPTION = "A location pin is printed on a tag hanging from the handle of a rolling suitcase."


def draw(s):
    luggage(s)
    face = luggage_tag(s)
    outline = pin_outline(46.5, 51, 5.8)
    s.line([face(x, z) for x, z in outline + outline[:1]], BOLD)
    s.line([face(x, z) for x, z in oval(46.5, 51, 2.15, 2.15, count=20)], BOLD)
