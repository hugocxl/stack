"""Physical illustrations for shopping, finance, services, buildings and food."""

from functools import partial
from pathlib import Path
import json
import re

from geometry import BOLD, DETAIL, EDGE, GUIDE
from scenes.commerce_objects import OBJECTS as SPECIALISTS
from scenes.commerce_custom import CUSTOM
from scenes.site_objects import OBJECTS as COMMON, ObjectScene

OBJECTS = {**COMMON, **SPECIALISTS}
GROUPS = {
    "commerce": "commerce-and-fulfillment",
    "finance": "billing-and-finance",
    "service": "service-booking-and-marketplaces",
    "building": "real-estate-design-and-construction",
    "civic": "climate-energy-and-civic-services",
    "food": "food-hospitality-and-agriculture",
}

# Positions are in world coordinates. In the paired layouts the far and
# near contours have room to breathe even when both subjects are tall.
ARRANGEMENTS = {
    "pair": ((-37,12,0,.95),(37,-12,0,1.06)),
    "desk": ((-37,8,6,.98),(36,-10,6,.97)),
    "route": ((-43,13,0,.86),(42,-13,0,1)),
    "compare": ((-38,14,5,.84),(38,-13,5,.96)),
    "lift": ((-18,9,5,1.05),(32,-14,29,.62)),
    "sequence": ((-52,15,0,.84),(1,0,0,.84),(51,-15,0,.87)),
    "fit": ((-5,3,4,1.03),(26,-32,50,.73)),
    "station": ((-35,13,0,1),(36,-13,0,.88),(48,45,0,.62)),
    "grid": ((-31,-32,4,.86),(29,-32,4,.86),(-31,29,4,.86),(29,29,4,.86)),
}

TEMPLATES = {
    "pair": "{a} sits apart from {b}.",
    "desk": "{a} and {b} share one work surface.",
    "route": "A marked route connects {a} to {b}.",
    "compare": "{a} and {b} occupy separate measuring bays.",
    "lift": "{b} is raised beside {a}.",
    "sequence": "{a}, {b}, and {c} make three successive stages.",
    "fit": "{b} is suspended over {a}, aligned along a dotted sightline.",
    "station": "{a}, {b}, and {c} meet at one station.",
    "grid": "{a}, {b}, {c}, and {d} sit on adjoining pads.",
}


def draw_scene(s, arrangement, objects):
    poses = ARRANGEMENTS[arrangement]
    if arrangement == "desk":
        s.box(-70,-39,0,139,78,5,6,DETAIL)
        s.line([(0,-29,5),(0,30,5)], GUIDE)
    elif arrangement == "compare":
        for x,y,_,_ in poses:
            s.box(x-28,y-24,0,56,48,4,4,DETAIL)
            s.line([(x-17,y+18,4),(x+17,y+18,4)], GUIDE)
    elif arrangement == "route":
        s.line([(-47,17,.2),(-14,17,.2),(15,-17,.2),(48,-17,.2)], EDGE, dashed=True)
        for x,y in ((-18,17),(18,-17)):
            s.disk(x,y,0,2.2,2,1.4,DETAIL)
    elif arrangement == "sequence":
        s.line([(-54,16,-.5),(0,0,-.5),(56,-16,-.5)], DETAIL, dashed=True)
    elif arrangement == "fit":
        s.box(-34,-31,0,58,66,4,4,DETAIL)
        s.line([(23,-29,9),(23,-29,45)], GUIDE, dashed=True)
        s.line([(38,-16,9),(38,-16,45)], GUIDE, dashed=True)
    elif arrangement == "grid":
        s.box(-62,-62,0,124,124,4,6,DETAIL)
        for x,y in ((-60,-60),(4,-60),(-60,4),(4,4)):
            faint = ObjectScene(s,(x,y,4),1,DETAIL)
            faint.frame(0,0,0,55,55,4,GUIDE)
    items = list(zip(objects,poses))
    # In depth ties, keep the remote objects in front of their faint guides,
    # then draw adjacent objects in a stable order to preserve physical edges.
    for index,(name,(x,y,z,scale)) in sorted(enumerate(items),key=lambda item: sum(item[1][1][:2])):
        _, draw = OBJECTS[name]
        draw(ObjectScene(s,(x,y,z),scale,BOLD if index==0 else EDGE))


def load_pack():
    root = Path(__file__).resolve().parents[2]
    catalog = json.loads((root/"catalog/use-cases.json").read_text(encoding="utf-8"))
    known = {case["id"]:case for group in catalog["groups"] for case in group["cases"]}
    lines = (Path(__file__).parent/"commerce_recipes.txt").read_text(encoding="utf-8").splitlines()
    group = None
    for row,line in enumerate(lines,1):
        if not line or line.startswith("#"):
            continue
        if line.startswith("["):
            group = GROUPS[line.strip("[]")]
            continue
        try:
            title, arrangement, props, placement = line.split("|")
            identifier = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
            if identifier in known:
                title, placement = (known[identifier][key] for key in ("title","placement"))
            objects = props.split()
            if len(objects)!=len(ARRANGEMENTS[arrangement]):
                raise ValueError("wrong number of objects")
            nouns = [OBJECTS[name][0] for name in objects]
            nouns = [("an " if noun[:1] in "aeiou" else "a ")+noun for noun in nouns]
            visual = TEMPLATES[arrangement].format(**dict(zip("abcd",nouns)))
            draw = partial(draw_scene,arrangement=arrangement,objects=objects)
            visual, draw = CUSTOM.get(identifier,(visual[:1].upper()+visual[1:],draw))
            yield group,identifier,title,placement,visual,draw
        except (KeyError,ValueError) as error:
            raise ValueError(f"Commerce recipe {row}: {line}") from error


PACK = list(load_pack())
