from scenes.redraws._kit import badge
from scenes.redraws.changes_saved import edited_document

DESCRIPTION = "A pencil crosses the ruled page of a tilted editing pad with an X badge on its lower corner."


def draw(s):
    page = edited_document(s)
    badge(s, "x", *page.point(70, 10, -4), 15)
