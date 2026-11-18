from geometry import EDGE, oval
from scenes.redraws._w3 import Surface, book, cover_cap, play

DESCRIPTION = "A closed course book has a graduation cap and a round play button on its cover."


def draw(s):
    cover = book(s, 80, 88, 13)
    cover_cap(cover, 40, 64, 35)
    cover.rules(24, 35, [33, 23], gap=7)
    button = Surface(s, cover.point(62, 22, -2.5), rise=(-1, 0), back=(0, 0, -1))
    button.plate(oval(0, 0, 16, 16, count=40)[:-1], 2.5, EDGE)
    play(button, 0, 0, 13, aligned=True)
