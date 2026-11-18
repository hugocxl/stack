from scenes.redraws._kit import badge
from scenes.redraws.unsaved_changes import edited_document

DESCRIPTION = "A slash badge covers the eraser end of the pencil on a folded document."


def draw(s):
    page = edited_document(s)
    badge(s, "slash", *page.point(73, 41), 13)
