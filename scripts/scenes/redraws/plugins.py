from geometry import DETAIL, EDGE, rounded
from scenes.redraws._w3 import Surface

DESCRIPTION = "A keyed plug-in cartridge docks into the matching notched port on a compact housing."


def draw(s):
    port = [(40, 14), (73, 14), (77, 18), (77, 32), (64, 32),
            (64, 40), (49, 40), (49, 32), (36, 32), (36, 18)]
    housing = Surface(s, (0, 0, 0))
    outer = rounded(0, 0, 92, 57, 5)
    housing.plate(outer, 18)

    # The front sheet leaves a clear view into the port.
    s.layers.pop()
    s.face([housing.point(*p, 7) for p in port], DETAIL)
    s.face([housing.point(*p) for p in outer], EDGE,
           openings=[[housing.point(*p) for p in port]])
    housing.rect(8, 12, 11, 6, 2)
    housing.rect(8, 24, 11, 6, 2)

    tongue = Surface(s, (0, 31, 0))
    connector = [(43, 17), (70, 17), (73, 20), (73, 28), (61, 28),
                 (61, 37), (52, 37), (52, 28), (40, 28), (40, 20)]
    tongue.plate(connector, 32)
    for x in (52, 61):
        s.line([tongue.point(x, 37), housing.point(x, 37)], EDGE)

    grip = Surface(s, (0, 45, 0))
    grip.plate(rounded(35, 10, 43, 34, 5), 14)
    grip.rect(41, 18, 31, 16, 3)
    for z in (23, 29):
        grip.rules(49, z, [15], ink=EDGE)
