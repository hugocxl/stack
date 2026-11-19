from geometry import BOLD, DETAIL, EDGE, oval
from scenes.redraws.bus_shelter_directory import bus_pictogram

DESCRIPTION = "A bus-stop sign on a post displays a bus above a route strip with three stop markers."


def draw(s):
    s.box(22, 0, 0, 4.5, 4.5, 82, 1.2)
    s.box(0, 3, 38, 49, 4, 48, 3)
    bus_pictogram(s, 24.5, 7, 68, 1.38, BOLD)
    face = lambda x, z: (x, 7, z)
    s.line([face(1, 54), face(48, 54)], DETAIL)
    s.line([face(8, 46), face(41, 46)], EDGE)
    for x in (8, 24.5, 41):
        s.face([face(a, z) for a, z in oval(x, 46, 2.65, 2.65, count=20)[:-1]], EDGE)
