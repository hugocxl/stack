"""Register illustration packs and connect them to the authored catalog."""
from importlib import import_module

MODULES = ("site_expansion", "systems_expansion", "commerce_expansion", "editorial_expansion")


def packs():
    for name in MODULES:
        qualified = f"scenes.{name}"
        try:
            module = import_module(qualified)
        except ModuleNotFoundError as error:
            if error.name != qualified:
                raise
            continue
        yield from module.PACK


def attach_artwork(catalog, entries):
    groups = {group["id"]: group for group in catalog["groups"]}
    cases = {
        case["id"]: (group["id"], case)
        for group in catalog["groups"] for case in group["cases"]
    }
    for group_id, identifier, title, placement, visual, _ in entries:
        asset = f"figures/{identifier}.svg"
        if identifier in cases:
            existing_group, case = cases[identifier]
            if existing_group != group_id or case.get("asset"):
                raise ValueError(f"Conflicting illustration for {identifier}")
            case.update(visual=visual, asset=asset)
        else:
            case = dict(id=identifier, title=title, placement=placement, visual=visual,
                        priority="extended", asset=asset)
            groups[group_id]["cases"].append(case)
            cases[identifier] = group_id, case
