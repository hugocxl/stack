from geometry import EDGE
from scenes.redraws._w3 import Surface
from scenes.redraws.artifact_conservation import museum_vase

DESCRIPTION = "An open museum cabinet displays an urn and a faceted mineral on separate fitted shelves."


def draw(s):
    s.box(0, 0, 0, 74, 7, 113, 1)
    s.box(0, 7, 0, 5, 31, 113, 1)
    s.box(69, 7, 0, 5, 31, 113, 1)
    s.box(5, 7, 6, 64, 31, 5, 1)
    s.box(5, 7, 51, 64, 31, 5, 1)

    cabinet = Surface(s, (0, 38, 0))
    mineral = [(18, 11), (15, 21), (20, 30), (25, 28), (28, 39), (37, 45),
               (43, 36), (43, 25), (49, 30), (54, 23), (53, 16), (44, 11)]
    s.face([(x, 30, z) for x, z in mineral])
    s.line([(37, 30, 45), (34, 30, 36), (35, 30, 13)], EDGE)
    s.line([(28, 30, 39), (34, 30, 36), (43, 30, 36)])
    s.line([(20, 30, 30), (23, 30, 23), (24, 30, 12)])
    s.line([(49, 30, 30), (48, 30, 23), (45, 30, 12)])

    museum_vase(s, 26, 28, 56, scale=.61)
    s.box(0, 0, 113, 74, 38, 6, 2)

    lower = [(x, z) for x, z in ((5, 11), (69, 11), (69, 51), (5, 51))]
    upper = [(x, z) for x, z in ((5, 56), (69, 56), (69, 113), (5, 113))]
    s.face([cabinet.point(*p) for p in [(0, 1), (74, 1), (74, 114), (0, 114)]],
           openings=[[cabinet.point(*p) for p in opening] for opening in (lower, upper)])
