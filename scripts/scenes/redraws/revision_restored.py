from geometry import BOLD, oval
from scenes.redraws._w2 import face_arrow
from scenes.redraws._w3 import sheet

DESCRIPTION = "Two offset folded-corner documents show a looping return arrow on the foremost copy."


def draw(s):
    rise = (-.47, .88)
    sheet(s, 74, 83, origin=(-16, -9, 0), rise=rise, depth=4)
    page = sheet(s, 74, 83, rise=rise, depth=5)
    page.rules(11, 63, [43, 34], gap=10)
    turn = oval(40, 27, 17, 16, -140, 138, 36)
    face_arrow(s, page.point, turn, BOLD, head=9)
