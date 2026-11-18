from geometry import BOLD, EDGE, GUIDE
from scenes.redraws._w3 import browser_window, component_art, printed_glyph

DESCRIPTION = "A collapse control points into the editor's narrow sidebar while the main design canvas stays in view."


def draw(s):
    editor = browser_window(s, 112, 78)
    editor.stroke([(73, 0), (73, 63)], EDGE)
    editor.stroke([(12, 10), (59, 10), (59, 50), (12, 50), (12, 10)], GUIDE, dashed=True)
    component_art(editor, 35, 30, 32, 29, EDGE)
    editor.rules(81, 50, [23], ink=EDGE)
    editor.rules(81, 40, [16])
    editor.rect(77, 10, 30, 20, 4, EDGE)
    printed_glyph(editor, "arrow", 91, 20, 13, BOLD)
