from scenes.redraws._kit import warning
from scenes.redraws._w5 import avatar_mark, credential_rows, device

DESCRIPTION = "A phone shows masked sign-in fields and a warning triangle attached to its account pictogram."


def draw(s):
    face = device(s, w=45, h=74)
    avatar_mark(s, face, 17, 51, 1.55)
    credential_rows(s, face, 10, 30)
    s.line([face(17, 14), face(28, 14)])
    x, y, z = face(39, 45)
    warning(s, x, y + 4, z, 23)
