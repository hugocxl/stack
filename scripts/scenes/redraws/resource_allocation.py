from math import cos, radians, sin

from geometry import EDGE, oval

DESCRIPTION = "Three unequal pie-chart segments show how resources are divided."


def draw(s):
    for start, stop in ((190, 280), (280, 341), (341, 550)):
        # Join contiguous visible rim edges to keep each curved side seamless.
        middle = radians((start + stop) / 2)
        x, y = 4.5 * cos(middle), 4.5 * sin(middle)
        arc = oval(x, y, 37, 37, start + 1, stop - 1, 52)
        rim = [(x, y), *arc]
        edges = list(zip(rim, rim[1:] + rim[:1]))
        visible = [b[1] - a[1] > b[0] - a[0] for a, b in edges]
        for index, (a, _) in enumerate(edges):
            if not visible[index] or visible[index - 1]:
                continue
            chain = [a]
            while visible[index % len(edges)]:
                chain.append(edges[index % len(edges)][1])
                index += 1
            s.face([(*point, 0) for point in chain] + [(*point, 13) for point in reversed(chain)], EDGE)
        s.face([(*point, 13) for point in rim], EDGE)
