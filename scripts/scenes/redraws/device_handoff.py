from geometry import BOLD
from scenes.redraws._kit import arrow
from scenes.redraws._w3 import interface_phone, preview_page, video_device

DESCRIPTION = "A single arrow carries the same page from a laptop display to a phone."


def draw(s):
    laptop = video_device(s)
    preview_page(laptop, 13, 14, 85, 48)
    phone = interface_phone(s, (136, 11, 0), scale=.73)
    preview_page(phone, 9, 13, 28, 54, narrow=True)
    arrow(s, [laptop.point(108, 49, -4), (117, 0, 51), phone.point(4, 53, -4)], BOLD, head=12)
