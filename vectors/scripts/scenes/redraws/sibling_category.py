from geometry import DETAIL
from scenes.redraws._sf import folder, screen

DESCRIPTION = "One branch splits to two matching folders standing side by side at the same level."


def draw(s):
    at = screen()
    s.line([at(0, 62), at(0, 46)], DETAIL)
    s.line([at(-40, 34), at(-40, 46), at(40, 46), at(40, 34)], DETAIL)
    for u in (-72, 8):
        folder(s, lambda a, b, u=u: at(u + a, b - 36), 64, 46)
