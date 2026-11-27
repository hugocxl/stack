from scenes.redraws._kit import badge
from scenes.redraws.undo_unavailable import strike
from scenes.redraws.unsaved_changes import edited_document

DESCRIPTION = "A folded document with an editing pencil carries a slashed sync badge."


def draw(s):
    page = edited_document(s)
    center = page.point(66, 58)
    badge(s, "refresh", *center, 14)
    strike(s, center, 12)
