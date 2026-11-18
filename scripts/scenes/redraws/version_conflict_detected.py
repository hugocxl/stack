from geometry import DETAIL, EDGE
from scenes.redraws._kit import warning
from scenes.redraws.replace_file_failed import file_page

DESCRIPTION = "Two overlapping revisions with different edits carry a warning triangle on their common edge."


def draw(s):
    earlier = file_page(s, (26, -23, 15), side=True)
    earlier.line([(12, 48), (35, 48)])
    earlier.line([(12, 40), (45, 40)], EDGE, dashed=True)
    earlier.line([(12, 30), (41, 30)])
    latest = file_page(s, (29, 7, 0), side=True)
    for z, width in ((48, 23), (37, 35), (27, 22), (17, 30)):
        latest.line([(10, z), (10 + width, z)], EDGE if z == 37 else DETAIL)
    x, y, z = latest.point(53, 48)
    warning(s, x + 3, y + 2, z - 23, 30)
