from scenes.redraws._kit import badge
from scenes.redraws._w1 import clipboard, task_rows

DESCRIPTION = "A refresh badge overlaps a standing checklist on a clipboard."


def draw(s):
    clipboard(s)
    task_rows(s, (-22, 28, 24), (-22, 17, 28), (-22, 6, 21))
    badge(s, "refresh", 29, 0, 40, 12)
