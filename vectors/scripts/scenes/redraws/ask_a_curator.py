from scenes.redraws._sf import BACK, bubble, plate, question, screen, vase

DESCRIPTION = "A museum vase stands beside a thick speech bubble holding a question mark."


def draw(s):
    vase(s, -20, 0, 0, 1.25)
    at = screen()
    b = lambda u, v: at(u + 26, v + 46)
    plate(s, b, bubble(52, 40, 14, (.2, 8, 9)), 6, BACK)
    question(s, lambda u, v: b(26 + u, 20 + v), 16)
