from geometry import DETAIL
from scenes.redraws._kit import badge
from scenes.redraws._w5 import device, device_profile, rect

DESCRIPTION = "A laptop and phone show signed-in profiles, and a check badge identifies the current device."


def draw(s):
    s.box(0, -10, 0, 62, 36, 4.5, 3.4)
    s.box(0, -12, 4, 62, 6, 44, 3.4)
    face = lambda x, z: (x, -6, z)
    rect(s, face, 5, 10, 52, 33, 3, DETAIL)
    device_profile(s, face, 23, 30, .88)
    for y in (-.4, 5.6):
        s.line([(8, y, 4.5), (54, y, 4.5)], DETAIL)
    phone = device(s, x=54, y=23, w=29, h=49)
    device_profile(s, phone, 14.5, 28, .8)
    badge(s, "check", *phone(28, 42), 10)
