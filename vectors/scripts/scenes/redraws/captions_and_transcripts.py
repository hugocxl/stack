from geometry import EDGE, rounded
from scenes.redraws._w3 import Surface
from scenes.redraws.caption_placement import video_frame

DESCRIPTION = "A video player carries an onscreen caption bar and a transcript drawer that opens below the screen."


def draw(s):
    across = (.94, -.34)
    housing = Surface(s, (0, -1, 0), across=across, back=(-.34, -.94, 0))
    housing.plate(rounded(0, 0, 115, 21, 4), 17)
    housing.rect(9, 3, 97, 11, 3, EDGE)

    apron = Surface(s, housing.point(10, 9, -32), across=across, back=housing.back)

    def transcript(x, v):
        return apron.point(x, 0, v)

    s.face([transcript(0, 0), transcript(94, 0), transcript(94, 33), transcript(0, 33)])
    for v, length in ((28, 55), (19, 46), (10, 61)):
        s.line([transcript(8, v), transcript(14, v)], EDGE)
        s.line([transcript(23, v), transcript(23 + length, v)], EDGE)
    s.line([transcript(18, 5), transcript(18, 30)])
    apron.plate(rounded(0, -8, 94, 8, 2), 2)
    apron.rect(39, -6, 16, 3, 1, EDGE)
    video_frame(s, (0, 0, 18))
