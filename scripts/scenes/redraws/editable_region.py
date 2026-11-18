from geometry import EDGE
from scenes.redraws._w3 import browser_window, pen_on, selection_handle

DESCRIPTION = "A pencil touches the outlined editable content block inside a browser page."


def draw(s):
    page = browser_window(s, 109, 76)
    page.rules(10, 50, [43], ink=EDGE)
    page.rules(10, 42, [83])
    page.rect(10, 10, 59, 24, 2, EDGE)
    page.rules(17, 26, [41, 30], gap=8)
    selection_handle(page, 10, 10, 5)
    selection_handle(page, 10, 34, 5)
    pen_on(page, 61, 22, length=55, pencil=True)
