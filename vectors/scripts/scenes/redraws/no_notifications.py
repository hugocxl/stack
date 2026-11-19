from geometry import DETAIL, EDGE, oval
from scenes.redraws.page_moved import Surface
from scenes.redraws.upload_in_progress import curve

DESCRIPTION = "A dashed bell silhouette has flared sides, a small crown, and a rounded clapper."


def draw(s):
    bell = Surface(s, screen=True)
    outline = curve((-35, 0), [
        ((-38, 4), (-27, 8), (-26, 21)),
        ((-25, 37), (-21, 47), (-8, 51)),
        ((-8, 64), (8, 64), (8, 51)),
        ((21, 47), (25, 37), (26, 21)),
        ((27, 8), (38, 4), (35, 0)),
        ((28, -4), (-28, -4), (-35, 0)),
    ])
    bell.line(outline, EDGE, dashed=True)
    bell.line(oval(0, -3, 10, 12, 180, 360, 30), EDGE, dashed=True)
    bell.line([(-27, 6), (27, 6)], DETAIL, dashed=True)
