from scenes.redraws.task_created import task_status

DESCRIPTION = "A barred-circle badge overlaps the status corner of a task card with a checkbox."


def draw(s):
    task_status(s, "slash")
