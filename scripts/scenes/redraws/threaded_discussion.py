from geometry import EDGE
from scenes.redraws.community_forum import balloon

DESCRIPTION = "Three progressively indented speech balloons are joined by two elbow-shaped reply connectors."


def draw(s):
    replies = ((0, 77, 78), (22, 35, 67), (44, -7, 56))
    for (x, z, width), (reply_x, reply_z, _) in zip(replies, replies[1:]):
        tail = x + width * .15
        s.line([(tail, 0, z - 28 * .33), (tail, 0, reply_z + 14),
                (reply_x, 0, reply_z + 14)], EDGE)

    for x, z, width in replies:
        face = balloon(s, (x, 0, z), width, 28, depth=3)
        face.rules(13, 17, [width - 30], ink=EDGE)
