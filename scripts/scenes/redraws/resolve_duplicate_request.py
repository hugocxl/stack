from geometry import BOLD
from scenes.redraws._w2 import face_arrow, request_card

DESCRIPTION = "A single curved merge arrow points from one tabbed request card to a lower matching card."


def draw(s):
    def plane(x, z):
        return .72*x, -.28*x - .51*z, .92*z

    def original(x, z):
        return plane(x, z + 26)

    def retained(x, z):
        return plane(x + 76, z)

    request_card(s, original, 56, 56)
    request_card(s, retained, 56, 56)
    face_arrow(s, plane, [(41, 85), (63, 84), (78, 79), (91, 70), (99, 55)], BOLD, head=10)
