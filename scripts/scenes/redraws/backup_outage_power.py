from scenes.redraws._w1 import lightning

DESCRIPTION = "A standby battery has two top terminals and a lightning bolt centered on its broad side."


def draw(s):
    s.box(-31, -18, 0, 62, 36, 35, 4)
    s.box(-32, -19, 34, 64, 38, 5, 4)
    for x, radius in ((-20, 5), (20, 4)):
        s.disk(x, -2, 39, radius, radius, 6)

    lightning(s, 0, 18.02, 17, 12)
