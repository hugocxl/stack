from scenes.redraws._w1 import flatbed_truck, roller_bridge

DESCRIPTION = "A short roller conveyor bridges the open beds of two freight trucks at deck height."


def draw(s):
    flatbed_truck(s, 13, 0, 1)
    roller_bridge(s, -13, 13, 0)
    flatbed_truck(s, -13, 0, -1)
