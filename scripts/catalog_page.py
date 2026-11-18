"""Render the use-case catalog and validate its links to published figures."""
import json
import re
from html import escape


def render_catalog(root, available):
    catalog = json.loads((root/"catalog/use-cases.json").read_text(encoding="utf-8"))
    seen_ids, linked_assets, sections = set(), set(), []
    for group in catalog["groups"]:
        entries = []
        for case in group["cases"]:
            identifier = case["id"]
            if identifier in seen_ids or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier):
                raise ValueError(f"Invalid or repeated use-case ID {identifier}")
            seen_ids.add(identifier)
            asset = case.get("asset")
            if asset:
                if asset not in available:
                    raise ValueError(f"Unknown asset for {identifier}: {asset}")
                linked_assets.add(asset)
            title, placement, visual = (escape(case[k]) for k in ("title","placement","visual"))
            label = f'<a href="{escape(asset)}">Open SVG</a>' if asset else '<span>Planned</span>'
            entries.append(
                f'<li id="{identifier}" data-asset="{bool(asset):d}">'
                f'<div><h3>{title}</h3><p>{placement}</p><p>{visual}</p></div>{label}</li>'
            )
        sections.append(
            f'<section id="group-{escape(group["id"])}"><h2>{escape(group["title"])}</h2>\n'
            f'<ul>\n'+ "\n".join(entries) + "\n</ul></section>"
        )
    if missing := available - linked_assets:
        raise ValueError(f"Figures missing from the use-case catalog: {', '.join(sorted(missing))}")
    template = (root/"scripts/catalog.html").read_text(encoding="utf-8")
    return (
        template.replace("<!-- GROUPS -->", "\n".join(sections))
        .replace("{{case_count}}", str(len(seen_ids)))
        .replace("{{figure_count}}", str(len(linked_assets)))
    )
