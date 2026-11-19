from shapely.affinity import rotate, translate
from shapely.geometry import LineString, box
from shapely.ops import unary_union

from geometry import EDGE
from scenes.redraws._kit import badge

DESCRIPTION = "Two interlocking chain links carry a check badge at the end of the chain."


def chain_link(center, angle):
    axis = LineString([(-15, 0), (15, 0)])
    ring = axis.buffer(13, quad_segs=16).difference(axis.buffer(8, quad_segs=16))
    return translate(rotate(ring, angle, origin=(0, 0)), *center)


def draw(s):
    left = chain_link((-18, 11), -34)
    right = chain_link((18, -12), -34)
    # Alternate the overlap so each link passes both in front of and behind the other.
    upper = box(-70, -65, 70, 0)
    visible = unary_union([
        left.boundary.difference(right.intersection(upper).buffer(.17)),
        right.boundary.difference(left.difference(upper).buffer(.17)),
    ])
    s.layers.append((visible, unary_union([left, right]), EDGE))
    badge(s, "check", 29, -22, 21, 10)
