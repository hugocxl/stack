from geometry import DETAIL
from scenes.redraws._sf import server, smooth
from scenes.redraws.email_address_changed import envelope

DESCRIPTION = "A sealed envelope arcs along a dashed path into a server."


def draw(s):
    envelope(s, -90, 20, 18, 46, 30)
    s.line([(x, y, z) for x, y, z in smooth([(-44, 20, 40), (-10, 10, 58), (20, 4, 40), (30, 2, 26)], 8)], DETAIL, dashed=True)
    server(s, 20, -20, 0, 52, 36, 20)
    server(s, 20, -20, 20, 52, 36, 20)
