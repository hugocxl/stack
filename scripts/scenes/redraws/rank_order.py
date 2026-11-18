from geometry import BOLD, EDGE, oval

DESCRIPTION = "A three-level winners’ podium shows one pip on the highest tier, two on the next and three on the lowest."


def draw(s):
    for index, (height, count) in enumerate(((36, 2), (57, 1), (23, 3))):
        x = index * 29
        s.box(x, 0, 0, 29, 36, height, 1.1, BOLD if count == 1 else EDGE)
        for i in range(count):
            center = x + 14.5 + (i - (count - 1) / 2) * 7.3
            s.line([(u, 36, v) for u, v in oval(center, height / 2, 2.15, 2.15, count=20)], EDGE)
