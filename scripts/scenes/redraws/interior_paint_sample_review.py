from scenes.redraws._w2 import face_magnifier
from scenes.redraws.material_samples import swatch_fan

DESCRIPTION = "An open magnifier rests across the foremost banded paint strip in a bound swatch fan."


def draw(s):
    chip = swatch_fan(s, paint=True)

    def lens(u, v):
        return chip(u, v, 3.8)

    face_magnifier(s, lens, 8, 44, 12, direction=(.94, -.34))
