from math import cos, pi, sin

from shapely.geometry import MultiPoint
from shapely.ops import unary_union

from geometry import DETAIL, EDGE, oval, project

DESCRIPTION = "Three bent inlet pipes of different diameters feed a common tank with a graduated sight glass."


def inlet(s, x, y, radius, top):
    bend = radius + 8
    sections = []

    def section(cy, cz, angle, r):
        return [(x + dx, cy + offset*sin(angle), cz + offset*cos(angle))
                for dx, offset in oval(0, 0, r, r, count=40)]

    # A vertical collar turns into an open mouth facing the viewer.
    sections.append([(x + dx, y + dy, 50)
                     for dx, dy in oval(0, 0, radius, radius, count=40)])
    for i in range(13):
        angle = i*pi/24
        cy = y + bend*(1 - cos(angle))
        cz = top + bend*sin(angle)
        sections.append(section(cy, cz, pi/2 - angle, radius))

    mouth_y = y + bend + 9
    mouth_z = top + bend
    mouth = section(mouth_y, mouth_z, 0, radius)
    sections.append(mouth)
    sections = [[project(point) for point in ring] for ring in sections]
    surface = unary_union([MultiPoint(a + b).convex_hull for a, b in zip(sections, sections[1:])])
    s.layers.append((surface.boundary, surface, EDGE))
    s.face(mouth, EDGE)
    s.line(section(mouth_y, mouth_z, 0, radius - 2.2), DETAIL)


def draw(s):
    s.box(0, 0, 0, 110, 65, 44, 6)
    s.box(2, 2, 44, 106, 61, 5, 5)
    for x, radius, z in ((18, 6, 61), (50, 8, 65), (85, 11, 69)):
        s.disk(x, 14, 49, radius + 2.6, radius + 2.6, 5)
        inlet(s, x, 14, radius, z)
    s.line([(u, 65, v) for u, v in oval(77, 22, 6, 14)], EDGE)
    s.line([(71, 65, 21), (83, 65, 21)], EDGE)
    for z in (13, 21, 29):
        s.line([(88, 65, z), (95, 65, z)], DETAIL)
