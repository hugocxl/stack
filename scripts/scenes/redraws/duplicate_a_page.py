from scenes.redraws._w3 import browser_window, preview_page

DESCRIPTION = "Two identical browser pages overlap in a stack with their matching headers and content blocks offset."


def draw(s):
    for origin in ((26, -13, 18), (0, 0, 0)):
        page = browser_window(s, 94, 76, origin=origin)
        preview_page(page, 9, 8, 76, 47)
