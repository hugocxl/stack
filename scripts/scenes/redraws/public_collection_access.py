from geometry import EDGE
from scenes.redraws._w3 import Surface
from scenes.redraws.artifact_conservation import museum_vase

DESCRIPTION = "A museum archive cabinet exposes a vase on its extended specimen drawer."


def cabinet_shell(s, width=67, height=85, depth=31):
    """Draw the interior back and visible inner side of an open cabinet."""
    s.box(0, 0, 0, width, 4, height, 1)
    s.face([(0, 4, 0), (0, depth, 0), (0, depth, height), (0, 4, height)])


def cabinet_frame(s, width=67, height=85, depth=31):
    """Close the cabinet shell around its unobstructed display opening."""
    s.face([(width, 0, 0), (width, depth, 0), (width, depth, height), (width, 0, height)])
    s.face([(0, 0, height), (width, 0, height), (width, depth, height), (0, depth, height)])
    front = Surface(s, (0, depth, 0))
    s.face([front.point(*p) for p in [(0, 0), (width, 0), (width, height), (0, height)]],
           openings=[[front.point(*p) for p in [(4, 5), (width-4, 5), (width-4, height-5), (4, height-5)]]])


def draw(s):
    cabinet_shell(s, width=76, height=61, depth=27)
    s.box(3, 3, 10, 70, 24, 3, 1)
    cabinet_frame(s, width=76, height=61, depth=27)
    lower = Surface(s, (0, 27, 0))
    lower.rect(5, 6, 66, 7, 1)
    lower.rules(32, 9.5, [12], ink=EDGE)

    s.box(6, 17, 14, 64, 37, 4, 1)
    s.box(6, 17, 18, 3, 35, 5, .6)
    museum_vase(s, 34, 39, 18, scale=.54)
    s.box(67, 17, 18, 3, 35, 5, .6)
    s.box(5, 52, 13, 66, 4, 11, 1.2)
    front = Surface(s, (0, 56, 0))
    front.rect(29, 16.5, 18, 4, 2, EDGE)
