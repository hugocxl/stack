from shapely.geometry import MultiPoint

from geometry import EDGE, oval, project
from scenes.redraws._w5 import food_speech

DESCRIPTION = "A covered catering platter has a question bubble beside its lid handle."


def draw(s):
    s.disk(29, 22, 0, 31, 24, 4)
    s.disk(29, 22, 4, 27, 20, 3)
    # A continuous projected contour keeps the lid free of seams.
    rings = [(7, 27, 20), (13, 25, 18.5), (19, 20, 15),
             (24, 13, 10), (26, 5, 4)]
    outline = MultiPoint([project((x, y, z)) for z, rx, ry in rings
                          for x, y in oval(29, 22, rx, ry)]).convex_hull
    s.layers.append((outline.boundary, outline, EDGE))
    s.ellipse(29, 22, 7.1, 27, 20, EDGE, -45, 135)
    s.tube([(24, 22, 25), (24, 22, 30), (27, 22, 32),
            (31, 22, 32), (34, 22, 30), (34, 22, 25)], 1.2)
    food_speech(s, 51, 24, 42, question=True)
