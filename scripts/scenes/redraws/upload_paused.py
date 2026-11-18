from scenes.redraws._kit import badge
from scenes.redraws.upload_in_progress import upload_cloud

DESCRIPTION = "A cloud with an upload arrow carries a pause badge at its upper edge."


def draw(s):
    badge(s, "pause", *upload_cloud(s), 16)
