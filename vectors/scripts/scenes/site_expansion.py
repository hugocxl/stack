"""Authored compositions for website, interface, and workflow moments."""
from functools import cache, partial
from json import loads
from pathlib import Path
from re import sub

from geometry import BOLD, DETAIL, EDGE, GUIDE, oval
from scenes.site_objects import OBJECTS, ObjectScene

ROOT = Path(__file__).resolve().parents[2]
GROUPS = {
    "land": "landing-and-marketing",
    "nav": "navigation-and-information-architecture",
    "account": "account-and-onboarding",
    "state": "feedback-and-empty-states",
    "product": "product-and-interface-capabilities",
    "work": "workflow-and-collaboration",
    "finish": "completion-and-notifications",
}

# Coordinates can cross the viewer's horizontal axis without sharing depth.
LAYOUTS = {
    "pair": ((-25,18,0,1),(28,-13,0,.88)),
    "staged": ((-34,10,0,.86),(1,3,6,.93),(39,-12,0,1)),
    "comparison": ((-35,8,5,1),(35,-9,5,1)),
    "transfer": ((-35,17,0,.93),(0,0,21,.76),(39,-13,0,.96)),
    "lift": ((10,5,0,1.12),(-10,-1,32,1)),
    "fit": ((1,4,0,1.23),(-2,-2,28,.76)),
    "corner": ((-21,-4,0,1.11),(32,23,0,.72)),
    "bench": ((-28,-3,5,1),(25,17,5,.85)),
    "lead": ((-28,10,0,.95),(31,-5,0,.9)),
    "aim": ((-25,18,1,.9),(33,-6,8,1)),
    "recess": ((16,0,0,1.11),(-25,12,0,.68)),
    "arc": ((20,-24,0,.84),(35,12,0,.79),(-29,13,0,.91)),
    "gather": ((18,-17,0,.8),(-27,-8,0,.85),(5,20,2,1.02)),
    "ridge": ((-35,13,0,.81),(4,1,15,.85),(36,-13,28,.91)),
    "face": ((19,-7,0,1.06),(-29,8,5,.84)),
    "gate": ((17,-8,0,1.08),(-22,21,0,.74)),
    "ends": ((-34,12,0,.91),(35,-11,0,.91)),
    "sweep": ((-30,-6,0,.97),(20,16,3,.84)),
    "branch": ((-31,13,0,.94),(28,-25,0,.80),(36,17,0,.80)),
    "fork": ((-26,-19,0,.84),(-23,24,0,.83),(40,-7,0,.96)),
    "support": ((-20,-10,0,1.13),(26,21,14,.83)),
    "edge": ((4,2,0,1.16),(-25,28,4,.72)),
    "vertical": ((7,-17,0,1),(18,23,15,.87)),
    "guide": ((-20,10,0,1.02),(29,-16,12,.81)),
    "aside": ((10,-25,0,1.05),(-11,22,0,.77)),
    "float": ((10,2,5,1.03),(-19,-3,48,.80)),
    "solo": ((0,0,0,1),),
}

VERBS = {
    "pair": "{A} sits beside {b}.",
    "staged": "{A}, {b}, and {c} occupy consecutive stations.",
    "comparison": "{A} and {b} stand on the two sides of a ruled platform.",
    "transfer": "{B} crosses between {a} and {c}.",
    "lift": "{B} is raised above {a}.",
    "fit": "{B} aligns above {a}.",
    "corner": "{B} sits at the near corner of {a}.",
    "bench": "{A} and {b} share a ruled work surface.",
    "lead": "A raised connector links {a} to {b}.",
    "aim": "Two sightlines extend between {a} and {b}.",
    "recess": "{B} rests in front of {a}.",
    "arc": "A curved rail links {a}, {b}, and {c}.",
    "gather": "{A} and {b} surround {c} on a shared base.",
    "ridge": "{A}, {b}, and {c} ascend along a path.",
    "face": "{B} stands in front of {a}.",
    "gate": "{B} approaches {a} from the front.",
    "ends": "A visible gap separates {a} from {b}.",
    "sweep": "A curved guide passes from {a} toward {b}.",
    "branch": "{A} sits at the split leading to {b} and {c}.",
    "fork": "Two rails meet between {a}, {b}, and {c}.",
    "support": "{B} is displayed beside {a}.",
    "edge": "{B} sits just outside the nearest edge of {a}.",
    "vertical": "{B} sits in front of and above {a}.",
    "guide": "An alignment path extends between {a} and {b}.",
    "aside": "{A} sits back from {b}, leaving space between them.",
    "float": "{B} is suspended above {a}, with two dashed guides marking its position.",
    "solo": "{A} is shown in isolation.",
}


def _article(noun):
    return ("an " if noun[0] in "aeiou" else "a ") + noun


def describe(mode, subjects):
    if mode=="solo":
        return _article(OBJECTS[subjects[0]][0]).capitalize()+"."
    phrases = [_article(OBJECTS[subject][0]) for subject in subjects]
    # Plural physical subjects use the definite article.
    for i,subject in enumerate(subjects):
        if subject in {"keys","swatch","vials","seatmap","tabs","steps"}:
            phrases[i] = f"the {OBJECTS[subject][0]}"
    lower = dict(zip("abc",phrases))
    upper = {key.upper(): phrase.capitalize() for key,phrase in lower.items()}
    return VERBS[mode].format(**lower, **upper)


class _Height:
    """Measure a subject before placing a second object above it."""
    def __init__(self):
        self.maximum = 0

    def update(self, z):
        self.maximum = max(self.maximum,z)

    def box(self,x,y,z,w,d,h,*args):
        self.update(z+h)

    disk = ring = box

    def solid(self,foot,z,h,**kwargs):
        self.update(z+h)

    def ellipse(self,x,y,z,*args):
        self.update(z)

    def line(self,points,*args,**kwargs):
        self.update(max(point[2] for point in points))

    face = line

    def tube(self,points,radius,*args):
        self.update(max(point[2] for point in points)+radius)


@cache
def _height(subject):
    scene = _Height()
    OBJECTS[subject][1](ObjectScene(scene,(0,0,0),1,EDGE))
    return scene.maximum


def _draw(scene, mode, subjects):
    anchors = LAYOUTS[mode]
    points = [entry[:3] for entry in anchors]
    basal_height = points[0][2]
    raised = mode in {"lift","fit","float"}
    if raised:
        basal_height += _height(subjects[0])*anchors[0][-1]
        x,y,z = points[1]
        overhead_clearance = {"fit":5, "lift":8, "float":13}[mode]
        points[1] = (x,y,max(z,basal_height+overhead_clearance))

    if mode in {"bench","comparison","gather","staged"}:
        scene.box(-66,-31,0,132,62,5,6,DETAIL)
        if mode == "comparison":
            scene.line([(0,-25,5),(0,25,5)],GUIDE,True)
            for x in range(-49,51,14):
                scene.line([(x,25,5),(x,22,5)],DETAIL)
        elif mode == "bench":
            for x in range(-52,54,13):
                scene.line([(x,-26,5),(x,-22,5)],DETAIL)
    if raised:
        perched = points[1]
        for offset in (-14,14):
            scene.line([(perched[0]+offset,perched[1],basal_height),
                        (perched[0]+offset,perched[1],perched[2])],GUIDE,True)
    if mode in {"aim","guide"}:
        a,b = points
        for spread in (-9,9):
            scene.line([(a[0]+18,a[1]+spread,a[2]+9),(b[0]-14,b[1]+spread,b[2]+10)],
                       DETAIL, mode=="guide")
    if mode in {"lead","transfer","ridge"}:
        connection = [(x,y,z+6) for x,y,z in points]
        if mode == "lead":
            a,b = connection
            connection = [a,(a[0]+14,a[1],a[2]),(b[0]-14,b[1],b[2]),b]
            scene.tube(connection,1.5,DETAIL)
        else:
            scene.line(connection,GUIDE,True)
    if mode in {"branch","fork"}:
        a,b,c = points
        junction = (0,2,5)
        for point in (a,b,c):
            path = [(*point[:2],6),(point[0]*.42,point[1],6),junction]
            scene.tube(path,1.15,DETAIL)
        scene.disk(*junction,3.5,3.5,2,EDGE)
    if mode == "arc":
        orbit = [(x,y,5) for x,y in oval(0,0,36,24,-89,173,53)]
        scene.tube(orbit,1.55,DETAIL)
    if mode == "sweep":
        scene.line([(-35,-12,0),(-5,-20,0),(21,-5,0),(34,14,0),(31,27,0)],GUIDE,True)
    if mode == "gate":
        scene.line([(-40,28,0),(-10,24,0),(16,2,0)],DETAIL,True)
    if mode == "support":
        x,y,h = points[1]
        scene.box(x-19,y-15,0,38,30,h,4,DETAIL)
    if mode == "vertical":
        x,y,h = points[1]
        scene.box(x-16,y-13,0,32,26,h,4,DETAIL)
    if mode == "recess":
        scene.line([(-13,21,0),(27,13,0)],GUIDE,True)

    indices = sorted(range(len(points)),key=lambda i: points[i][0]+points[i][1])
    if raised:
        indices.sort(key=lambda i: points[i][2])
    focus = {"transfer":1,"arc":2,"gather":2,"branch":0,"gate":1}.get(mode,len(points)-1)
    for i in indices:
        at = points[i]
        if (mode in {"bench","comparison","gather","staged"} and at[2]<5):
            at = (*at[:2],5)
        _, draw = OBJECTS[subjects[i]]
        draw(ObjectScene(scene,at,anchors[i][-1],BOLD if i==focus else EDGE))


def _catalog():
    catalog = loads((ROOT/"catalog/use-cases.json").read_text(encoding="utf-8"))
    return {case["id"]: case for group in catalog["groups"] for case in group["cases"]}


def _load_rows():
    existing = _catalog()
    group = None
    for line in Path(__file__).with_name("site_expansion.tsv").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            group = GROUPS[line[1:-1]]
            continue
        fields = line.split("\t")
        if len(fields)==2:
            identifier, composition = fields
            title = existing[identifier]["title"]
            placement = existing[identifier]["placement"]
        else:
            title, placement, composition = fields
            identifier = sub(r"[^a-z0-9]+","-",title.lower()).strip("-")
        mode,*subjects = composition.split()
        if len(subjects)!=len(LAYOUTS[mode]):
            raise ValueError(f"Wrong number of subjects in {identifier}")
        yield (group,identifier,title,placement,describe(mode,subjects),partial(_draw,mode=mode,subjects=subjects))


PACK = list(_load_rows())
