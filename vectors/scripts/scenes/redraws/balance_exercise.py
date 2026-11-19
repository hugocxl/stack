from math import sqrt

from shapely.geometry import MultiPoint

from geometry import DETAIL, EDGE, oval, project
from scenes.redraws._w4 import Surface

DESCRIPTION = "A tilted circular balance board rests on its rounded half-dome rocker."


def draw(s):
    profiles = [(z, 27*sqrt(1 - ((z - 38)/39)**2)) for z in range(39)]
    dome = MultiPoint([project((x, y, z)) for z, r in profiles
                       for x, y in oval(0, 0, r, r, count=40)]).convex_hull
    s.layers.append((dome.boundary, dome, EDGE))

    def deck_point(u, v):
        return (.94*u + .34*v, -.34*u + .94*v, 44 - .32*u)

    deck = Surface(s, deck_point)
    deck.slab(oval(0, 0, 43, 38)[:-1], 7)
    deck.oval(0, 0, 37, 32, DETAIL)
    for u in (-22, 22):
        deck.oval(u, 0, 5, 17, EDGE)
