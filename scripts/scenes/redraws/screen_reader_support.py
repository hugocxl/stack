from geometry import BOLD, EDGE, rounded
from scenes.redraws._w3 import Surface, reader_page, speaker_art

DESCRIPTION = "A thick text folio carries a raised loudspeaker tab on its upper corner."


def draw(s):
    page = reader_page(s)
    page.rules(11, 49, [42, 53, 47, 53, 35], gap=8)
    tab = Surface(s, page.point(0, 0, -4), rise=page.rise, back=page.back)
    tab.plate(rounded(52, 51, 42, 31, 7), 6, EDGE)
    speaker_art(tab, 73, 66, 24, BOLD)
