from scenes.redraws._kit import badge
from scenes.redraws.upload_in_progress import upload_cloud

DESCRIPTION = "A cloud with an upload arrow carries an X badge at its upper edge."


def draw(s):
    badge(s, "x", *upload_cloud(s), 16)
