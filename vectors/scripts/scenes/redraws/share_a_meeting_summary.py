from shapely.geometry import LineString, Polygon

from geometry import BOLD, EDGE, project
from scenes.redraws._w2 import face_arrow
from scenes.redraws.meeting_notes import note_groups, notes_sheet

DESCRIPTION = "A share arrow rises from an open box that overlaps the right edge of a bulleted meeting summary."


def draw(s):
    point = notes_sheet(s)
    note_groups(s, point)

    x, y, z = point(88, 58)

    def icon(u, v):
        return x + (u + 12)*.5, y - (u + 12)*.5, z + v

    box = [(-17, 6), (-17, -16), (24, -16), (24, 6)]
    corners = [project(icon(u, v)) for u, v in box]
    opening = [project(icon(-1, 6)), *corners, project(icon(13, 6))]
    s.layers.append((LineString(opening), Polygon(corners), EDGE))
    face_arrow(s, icon, [(6, -8), (6, 23)], BOLD, head=8)
