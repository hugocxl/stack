"""Authored orthographic figure recipes for technical and inclusive websites."""

from functools import partial
from pathlib import Path
import json
import re

from geometry import BOLD, DETAIL, EDGE, GUIDE
from scenes import systems_shapes, systems_situations

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name("systems_recipes")
GROUPS = {
    "development": "developer-and-infrastructure",
    "data": "data-and-intelligence",
    "ai": "assistive-and-generative-features",
    "trust": "trust-privacy-and-governance",
    "accessibility": "accessibility-language-and-inclusion",
}
LITERALS = {"B":BOLD, "E":EDGE, "D":DETAIL, "G":GUIDE, "Y":True, "N":False}


def _value(value):
    if value in LITERALS:
        return LITERALS[value]
    if re.fullmatch(r"-?\d+",value) and not value.startswith("0"):
        return int(value)
    if value == "0":
        return 0
    if re.fullmatch(r"-?\d*\.\d+", value):
        return float(value)
    return value


def _draw(s, commands):
    for function, args in commands:
        function(s,*args)


def _recipe(line, location):
    commands=[]
    for call in line.split(";"):
        name, *args = call.split()
        if name.startswith("_") or not callable(function:=getattr(systems_shapes,name,None)):
            raise ValueError(f"{location}: unknown primitive {name}")
        commands.append((function, tuple(_value(value) for value in args)))
    return partial(_draw, commands=commands)


RELATIONSHIPS = {
    "exchange": "{0} and {1} sit at opposite ends of a routed connection.",
    "convert": "{0} approaches a transfer frame and {1} sits on the outgoing side.",
    "flow": "{0}, {1}, and {2} occupy consecutive stops on one lead.",
    "compare": "{0} and {1} occupy corresponding sides of a comparison bed.",
    "bench": "{0} is laid out alongside {1} on a shared working surface.",
    "lift": "{1} lifts above {0} with quiet alignment guides.",
    "gate": "{0} and {1} sit on opposite sides of a calibrated gate.",
    "split": "A route splits from {0} into separate branches for {1} and {2}.",
    "merge": "A route converges from {0} and {1} toward {2}.",
    "shelter": "{0} occupies a partly open containment tray beside {1}.",
    "dock": "{0} aligns with an empty docking tray while {1} is staged alongside.",
    "index": "{2} is raised from a fitted rack that holds {0} and {1}.",
    "stations": "{0}, {1}, and {2} form three assigned stops on one station rail.",
    "handover": "{1} crosses the open gap between {0} and {2}.",
    "watched": "{0} sits opposite {1}, with a lead between them.",
    "independent": "{0} and {1} occupy separate beds within one perimeter.",
    "isolated": "{1} is separated from its neighbors, {0} and {2}, by a marked perimeter.",
    "protected": "A solid shield intervenes between {0} and {1}.",
    "outside": "{0} remains apart while {1} sits in an outlined placement area.",
    "alignment": "{0} and {1} sit on a shared calibration bed at different registers.",
    "orbit": "{1} and {2} orbit a central {3}.",
    "feedback": "A curved feedback route links {0} with {1}.",
    "relay": "{1} sits along the path from {0} to {2}.",
    "inspect": "{0} occupies a recessed area, with {1} raised above the inspection line.",
    "replace": "{1} is poised above an open seat beside {0}.",
    "queue": "{0}, {1}, and {2} wait along an ordered bench.",
    "boundary": "A raised shutter separates {0} from {1}.",
    "surface": "{0} and {1} are shown together on a fitted working plate.",
    "elevation": "A compact stepped structure sets {0} below a raised {4}.",
    "pivot": "A moving arm sits between {0} and {1}.",
    "conduit": "{0} and {1} exchange a signal across a narrow conduit.",
}
OBJECT_LABELS = {
    "chip":"microchip", "processor":"processor module", "port":"terminal block",
    "bars":"bar-graph display", "spectrum":"spectrum display", "spark":"trend display",
    "matrix":"matrix display", "terminal":"command terminal", "photo_flat":"photo print",
    "gridrack":"gridded tray", "note":"lined note", "file":"upright file panel", "template":"tabbed template",
    "passkey":"double-notched key", "audio_clip":"clip waveform", "outline_map":"line drawing",
    "gate_mark":"marked gate", "calipers":"calibration frame", "railoff":"detached link",
    "wave":"waveform display", "pulse":"pulse display", "stop":"stop panel",
    "approval":"approval panel", "meter":"dial gauge", "quantile":"rising distribution plot",
    "scatter":"scattered measurements", "warning":"warning panel", "play":"playback screen",
    "photo":"framed landscape", "building":"framed cityscape", "coast":"framed coast",
    "archive":"file rack", "pattern":"pattern sheet", "plan":"plan sheet",
    "balance":"pan balance", "frames":"stack of frames",
}


def _situation(group, fields):
    title, placement, relationship, kinds = fields
    kinds = kinds.split()
    nouns = [OBJECT_LABELS.get(kind, kind) for kind in kinds]
    articles = [noun if noun.endswith("measurements") else
                ("an " if noun.startswith(tuple("aeiou")) else "a ")+noun for noun in nouns]
    visual = RELATIONSHIPS[relationship].format(
        *(articles + [""] * (3-len(articles)) + [nouns[0], nouns[1]])
    )
    visual = visual[0].upper()+visual[1:]
    slug = re.sub(r"[^a-z0-9]+","-",title.lower()).strip("-")
    draw = partial(systems_situations.composition, relationship=relationship, objects=kinds)
    return group,slug,title,placement,visual,draw


def _load():
    catalog = json.loads((ROOT/"catalog/use-cases.json").read_text())
    by_id = {entry["id"]: (group["id"], entry["title"], entry["placement"])
             for group in catalog["groups"] for entry in group["cases"]}
    entries=[]
    for path in sorted(SOURCE.glob("*.txt")):
        if path.stem.split("-")[0] not in GROUPS:
            continue
        domain=GROUPS[path.stem.split("-")[0]]
        for number,line in enumerate(path.read_text().splitlines(),1):
            if not line.strip() or line.startswith("#"):
                continue
            fields = [field.strip() for field in line.split("|")]
            if path.stem.endswith("-situations"):
                entries.append(_situation(domain,fields))
                continue
            if len(fields)==3:
                case_id, visual, recipe=fields
                source_group, title, placement=by_id[case_id]
                if domain!=source_group:
                    raise ValueError(f"{path.name}:{number}: wrong case domain for {case_id}")
            else:
                case_id,title,placement,visual,recipe=fields
            assembly=_recipe(recipe,f"{path.name}:{number}")
            entries.append((domain,case_id,title,placement,visual,assembly))
    if len(entries)!=len({entry[1] for entry in entries}):
        raise ValueError("Systems figure IDs must be unique.")
    return entries


PACK = _load()
