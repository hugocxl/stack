from scenes.redraws._w2 import browser_page
from scenes.redraws._w4 import Surface, landscape

DESCRIPTION = "A browser lightbox centers an enlarged landscape inside an otherwise empty recessed viewport."


def draw(s):
    at = browser_page(s, 116, 76, depth=9)
    window = Surface(s, lambda u, v: at(u, 76 - v))
    window.frame(6, 20, 104, 50, 2)
    landscape(window, 25, 25, 66, 40)
