from scenes.redraws._w3 import interface_monitor, interface_phone, preview_page

DESCRIPTION = "A desktop monitor and a phone show the same page, with the image and text stacked on the narrower screen."


def draw(s):
    monitor = interface_monitor(s)
    preview_page(monitor, 12, 14, 88, 49)
    phone = interface_phone(s, (121, 13, 0), scale=.73)
    preview_page(phone, 9, 13, 28, 54, narrow=True)
