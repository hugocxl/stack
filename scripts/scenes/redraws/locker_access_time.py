from scenes.redraws._kit import badge
from scenes.redraws.local_pickup_appointment import pickup_locker

DESCRIPTION = "A closed parcel locker has a clock badge beside its outlined lower access door."


def draw(s):
    front = pickup_locker(s)
    badge(s, "clock", *front.at(72, 20), 13)
