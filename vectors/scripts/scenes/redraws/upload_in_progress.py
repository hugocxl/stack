from geometry import BOLD, EDGE, oval
from scenes.redraws.page_moved import Surface

DESCRIPTION = "A cloud with an upload arrow carries a circular indicator with a partially drawn progress arc."


def curve(start, sections):
    points = [start]
    for a, b, end in sections:
        for step in range(1, 13):
            t = step / 12
            weights = ((1 - t)**3, 3 * (1 - t)**2 * t, 3 * (1 - t) * t**2, t**3)
            points.append(tuple(sum(w * c for w, c in zip(weights, axis))
                                for axis in zip(start, a, b, end)))
        start = end
    return points


def upload_cloud(s):
    cloud = Surface(s, (0, 8, 34), side=True, rise=-.27)
    outline = curve((20, 0), [
        ((-6, 0), (-5, 34), (19, 36)),
        ((24, 37), (29, 36), (33, 34)),
        ((37, 74), (85, 75), (89, 40)),
        ((113, 47), (128, 32), (122, 15)),
        ((119, 5), (111, 0), (101, 0)),
    ])
    cloud.plate(outline, 9)
    cloud.arrow([(63, 9), (63, 45)], BOLD, 12)
    return cloud.point(111, 51)


def draw(s):
    center = upload_cloud(s)
    face = Surface(s, center, screen=True)
    face.plate(oval(0, 0, 16, 16, count=48)[:-1], 0)
    face.line(oval(0, 0, 9.5, 9.5, 90, 190, 20), EDGE, dashed=True)
    face.arrow(oval(0, 0, 9.5, 9.5, 190, 444, 36), BOLD, head=3.2)
