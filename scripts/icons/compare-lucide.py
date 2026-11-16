#!/usr/bin/env python3
"""Rebuild the pinned 2026-11-16 coverage report without geometry dependencies.

Usage: python3 scripts/icons/compare-lucide.py [--inventory METADATA.json] [--check]
The checked-in inventory contains upstream metadata only, never SVG paths.
"""
import argparse
import runpy
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--inventory', type=Path, default=Path(__file__).with_name('lucide-1.73.0.json'))
parser.add_argument('--check', action='store_true', help='Fail if checked-in reports differ; write nothing.')
args = parser.parse_args()
upstream = json.loads(args.inventory.read_text())
lucide = upstream['icons']
catalog_bytes = (ROOT / 'catalog.json').read_bytes()
catalog = json.loads(catalog_bytes)
local = {x['name']: x for x in catalog}

# These mappings are editorial judgments about meaning, not geometry equality.
# Explicit mappings override upstream's historical aliases when the local
# drawing has a different meaning/orientation from the upstream alias.
equivalents = {
    'audio-waveform': ('waveform', 'Audio amplitude waveform.'),
    'bike': ('bicycle', 'Same bicycle concept under a different noun.'),
    'chart-column': ('chart-bar', 'Local recipe draws vertical columns; Lucide chart-bar is horizontal.'),
    'chevrons-right-left': ('chevrons-in', 'Two inward-facing horizontal chevrons.'),
    'circle-dollar-sign': ('dollar', 'Local dollar sign has an enclosing circle.'),
    'circle-pause': ('pause-circle-fill', 'Circular pause control; historical local fill suffix is retained.'),
    'columns-2': ('columns', 'Two-column layout.'),
    'eighth-notes': ('music', 'Pair of connected eighth notes.'),
    'face-neutral': ('meh', 'Neutral facial expression.'),
    'face-slightly-frowning': ('frown', 'Frowning facial expression.'),
    'face-slightly-smiling': ('smile', 'Smiling facial expression.'),
    'file-archive': ('file-zip', 'Compressed/archive file with a zipper.'),
    'file-down': ('file-download', 'Document with downward transfer arrow.'),
    'file-music': ('file-audio', 'Local audio document uses a musical note, not headphones.'),
    'file-play': ('file-video', 'Local video document uses a play triangle.'),
    'file-spreadsheet': ('file-table', 'Document containing a cell grid.'),
    'file-up': ('file-upload', 'Document with upward transfer arrow.'),
    'fingerprint-pattern': ('fingerprint', 'Fingerprint identity pattern.'),
    'flask-conical': ('flask', 'Conical laboratory flask.'),
    'folder-archive': ('folder-zip', 'Compressed/archive folder with zipper.'),
    'folder-down': ('folder-download', 'Folder with downward transfer arrow.'),
    'folder-up': ('folder-upload', 'Folder with upward transfer arrow.'),
    'funnel': ('filter', 'Same filtering funnel.'),
    'gauge': ('gauge-medium', 'Analog gauge with needle; local also offers low/high/max states.'),
    'git-commit-horizontal': ('git-commit', 'Commit node on a horizontal branch.'),
    'house': ('home', 'Same home/house concept.'),
    'letter-b': ('bold', 'Local bold control draws a B; upstream retains bold as an alias for letter-b.'),
    'list-indent-decrease': ('outdent', 'Decrease text indentation.'),
    'list-indent-increase': ('indent', 'Increase text indentation.'),
    'list-sort-ascending': ('sort-ascending', 'List ordering upward/ascending.'),
    'list-sort-descending': ('sort-descending', 'List ordering downward/descending.'),
    'loader-circle': ('spinner', 'Circular loading progress indicator.'),
    'luggage': ('suitcase', 'Wheeled travel suitcase.'),
    'message-square': ('message', 'Local message uses a rounded rectangular speech bubble.'),
    'message-square-check': ('message-check', 'Rectangular speech bubble with check.'),
    'message-square-heart': ('message-heart', 'Rectangular speech bubble with heart.'),
    'message-square-more': ('message-dots', 'Rectangular speech bubble with ellipsis.'),
    'message-square-plus': ('message-plus', 'Rectangular speech bubble with plus.'),
    'message-square-text': ('message-text', 'Rectangular speech bubble with text lines.'),
    'mic': ('microphone', 'Same microphone concept.'),
    'mic-off': ('microphone-off', 'Microphone disabled with diagonal strike.'),
    'octagon-exclamation-point': ('octagon-alert', 'Octagonal warning with exclamation point.'),
    'paw-print': ('paw', 'Animal paw print.'),
    'radio-receiver': ('radio', 'Local recipe draws a radio receiver box with antenna.'),
    'rotate-ccw': ('rotate-left', 'Counterclockwise rotation arrow.'),
    'rotate-ccw-clock': ('history', 'Clock/history with counterclockwise arrow.'),
    'rotate-cw': ('rotate-right', 'Clockwise rotation arrow.'),
    'rows-2': ('rows', 'Two-row layout.'),
    'server': ('server-rack', 'Server rack with multiple storage units.'),
    'shield-exclamation-point': ('shield-alert', 'Shield containing an exclamation point.'),
    'shopping-basket': ('basket', 'Shopping basket with handle.'),
    'sliders-horizontal': ('sliders', 'Local recipe draws horizontal adjustment tracks.'),
    'smartphone': ('phone-android', 'Generic handheld touchscreen phone; local name is platform-specific.'),
    'square-check': ('checkbox', 'Checked square control.'),
    'square-dashed-text': ('text-select', 'Text-selection region.'),
    'square-letter-p': ('parking', 'Parking P inside a square.'),
    'swatch-book': ('swatch', 'Fanned color swatches.'),
    'text-align-center': ('align-center', 'Centered text lines.'),
    'text-align-end': ('align-right', 'Right-aligned text in a left-to-right interface; direction-sensitive.'),
    'text-align-justify': ('align-justify', 'Justified text lines.'),
    'text-align-start': ('align-left', 'Left-aligned text in a left-to-right interface; direction-sensitive.'),
    'toggle-left': ('toggle-off', 'Toggle thumb on the left.'),
    'toggle-right': ('toggle-on', 'Toggle thumb on the right.'),
    'train-front': ('train', 'Front-facing railway train; do not assume tram-specific coverage.'),
    'tree-pine': ('tree', 'Local tree has the tiered conifer silhouette.'),
    'triangle-exclamation-point': ('triangle-alert', 'Triangular warning with exclamation point.'),
    'type': ('font', 'Typographic A / font control.'),
    'volume-2': ('volume', 'Local speaker uses two sound waves.'),
    'volume-x': ('volume-off', 'Local disabled speaker uses an X, not a slash.'),
    'x': ('close', 'Diagonal close/cancel cross.'),
    'arrow-left-right': ('swap-horizontal', 'Opposing horizontal direction/transfer arrows.'),
    'arrow-up-down': ('swap-vertical', 'Opposing vertical direction/transfer arrows.'),
    'circle-play': ('play-circle', 'Circular play control.'),
    'circle-question-mark': ('circle-help', 'Question mark in a circle.'),
    'circle-stop': ('stop-circle', 'Circular stop control.'),
    'circle-exclamation-point': ('circle-alert', 'Exclamation point in a circle.'),
}

collisions = {
    'pi': 'Local pi is a retained Pi brand mark, not the mathematical constant.',
    'chart-bar': 'Local chart-bar has vertical columns; the Lucide canonical name means horizontal bars.',
}
caveats = {
    'play': 'Local default artwork includes a circle; Lucide plain play is an unframed triangle.',
    'pause': 'Local default artwork includes a circle; Lucide plain pause is unframed.',
    'video': 'Local video drawing is a film/player pictogram; Lucide uses a camcorder. Review camera-toggle use separately.',
    'radio': 'Local drawing is a radio receiver; Lucide canonical radio is a broadcast/signal symbol.',
    'volume': 'Local volume includes two sound waves; Lucide volume is the no-wave speaker. Use the explicit volume-2 mapping for state precision.',
    'volume-off': 'Local artwork uses an X; Lucide volume-off uses a strike. The local artwork maps more precisely to volume-x.',
}
# Count strong semantic equivalents only. Historical alias names do not override
# reviewed local meaning (file-headphone, tram-front, mic-signal, sliders-vertical).
rejected_aliases = {
    'file-headphone': 'Local file-audio uses a music note, not a headphone; mapped to file-music instead.',
    'mic-signal': 'Local podcast is a person/broadcast motif; current Lucide mic-signal specifically depicts a broadcasting microphone.',
    'sliders-vertical': 'Local sliders recipe has horizontal tracks; mapped to sliders-horizontal instead.',
    'tram-front': 'Local train has no reviewed tram-specific distinction; mapped to train-front instead.',
}

def categories(name, seen=()):
    assert name not in seen, ('category inheritance cycle', name)
    result = []
    for category in lucide[name].get('categories', []):
        expanded = categories(category.split(':', 1)[1], seen + (name,)) if category.startswith('$extends:') else [category]
        for item in expanded:
            if item not in result:
                result.append(item)
    return result

records = []
for name in sorted(lucide):
    upstream_aliases = lucide[name].get('aliases', [])
    alias_matches = [a['name'] for a in upstream_aliases if a['name'] in local]
    cats = categories(name)
    record = {'lucide_name': name, 'categories': cats, 'primary_category': cats[0] if cats else 'uncategorized',
              'lucide_aliases': upstream_aliases, 'local_upstream_alias_matches': alias_matches}
    if name in collisions:
        record.update(status='missing', local_name=None, name_collision=collisions[name])
    elif name in local:
        record.update(status='contextual-match' if name in caveats else 'exact-name', local_name=name)
        if name in caveats:
            record['caveat'] = caveats[name]
            record['implementation_batch'] = '00'
    elif name in equivalents:
        target, reason = equivalents[name]
        assert target in local, target
        record.update(status='semantic-equivalent', local_name=target, reason=reason,
                      equivalence_basis='upstream-alias-and-editorial-review' if target in alias_matches else 'editorial-review')
    else:
        record.update(status='missing', local_name=None)
        if name in rejected_aliases:
            record['rejected_upstream_alias_reason'] = rejected_aliases[name]
    records.append(record)

by_name = {x['lucide_name']: x for x in records}
priority_names = '''alarm-clock-check alarm-clock-off archive-x arrow-down-to-line arrow-up-to-line asterisk baby backpack badge badge-info badge-minus badge-plus badge-x bell-check bell-dot bell-minus bluetooth-connected bluetooth-searching book-check book-heart book-lock book-minus book-plus book-search book-text book-x bookmark-minus bookmark-off bookmark-x brackets briefcase-medical calculator calendar-minus calendar-off calendar-search calendar-sync captions captions-off chart-bar chart-column-stacked chart-scatter clipboard-clock clipboard-copy clipboard-list clipboard-minus clipboard-paste clipboard-pen clipboard-plus clipboard-x clock-check clock-plus cloud-check cloud-sync code-xml cog copy-check copy-plus copy-x database-backup database-check database-cog database-minus database-plus database-search database-x delete door-closed ear ear-off equal ethernet-port file-clock file-cog file-database file-diff file-exclamation-point file-key file-pen file-question-mark file-scan file-terminal file-type file-user files folder-clock folder-cog folder-git folder-key folder-pen folder-sync folder-tree folder-user grip grip-horizontal grip-vertical hand-heart handshake heading-3 heading-4 headset highlighter id-card image-minus image-off images languages layout-list layout-template library lightbulb-off link-2 list-checks list-clock list-filter list-minus list-plus list-tree list-x loader locate locate-fixed mail-clock mail-dot mail-minus mail-search mail-x map-pin-off map-pin-plus map-pin-x memory-stick message-square-code message-square-lock message-square-off message-square-reply message-square-x monitor-cog monitor-off mouse-pointer mouse-pointer-click move newspaper nfc package-check package-minus package-open package-plus package-search package-x panel-left-close panel-left-open phone-incoming phone-missed phone-off phone-outgoing pi pin-off power-off regex reply reply-all router save-all save-check scan-barcode scan-qr-code scan-text screen-share screen-share-off search-check search-code search-x send-horizontal separator-horizontal separator-vertical server-cog server-off settings-2 share share-2 shield-ban shield-cog shield-minus shield-off shield-plus shield-user signal signal-high signal-low signal-medium signal-zero sliders-vertical speaker spell-check square-minus square-plus square-x star-half star-off syringe table-cells-merge table-cells-split tag-plus tags timer-off timer-reset touchpad touchpad-off trash-off unfold-vertical user-cog user-lock user-minus user-search user-shield video-off voicemail volume-1 webcam webhook wifi-high wifi-low wifi-zero zap-off'''.split()
priority_names = sorted({n for n in priority_names if by_name[n]['status'] == 'missing'})

batch_defs = [
    ('01', 'Product foundations and critical states', 'Most reusable missing interface concepts and state families; complete as reviewed 20–40 icon slices.'),
    ('02', 'Documents, communication, identity and planning', 'Finish application workflows and preserve shape/state distinctions.'),
    ('03', 'Design, typography, layout, mathematics and navigation', 'Includes complete letter/digit and shape families; avoid treating decorative variants as new user needs.'),
    ('04', 'Development, devices, connectivity and analytics', 'Complete developer tools, device states, network and chart families.'),
    ('05', 'Health, accessibility, science and sports', 'Review specialist meanings and accessibility recognition at small sizes.'),
    ('06', 'Commerce, buildings, transport, travel and home', 'Add common physical-world nouns before uncommon currency and equipment variants.'),
    ('07', 'Food, nature, weather, animals and recreation', 'Complete broad consumer coverage, then specialist/seasonal variants.'),
    ('08', 'Remaining reference-specific variants', 'Resolve remaining canonical names only when a clear distinct meaning or discoverability benefit exists.'),
]
groups = {
    '02': {'files', 'communication', 'mail', 'account', 'people', 'security', 'notifications', 'time', 'social'},
    '03': {'design', 'text', 'layout', 'math', 'letters-digits', 'shapes', 'arrows', 'navigation', 'cursors'},
    '04': {'development', 'devices', 'connectivity', 'charts', 'multimedia', 'photography'},
    '05': {'medical', 'accessibility', 'science', 'sports'},
    '06': {'shopping', 'finance', 'buildings', 'transportation', 'travel', 'home', 'tools'},
    '07': {'food-beverage', 'nature', 'weather', 'animals', 'gaming', 'emoji', 'seasons', 'sustainability'},
}
for record in records:
    if record['status'] != 'missing':
        continue
    name = record['lucide_name']
    batch = '01' if name in priority_names else next((key for key, group in groups.items() if record['primary_category'] in group), '08')
    record['implementation_batch'] = batch

counts = collections.Counter(x['status'] for x in records)
missing_by_category = {}
for category in sorted({x['primary_category'] for x in records}):
    subset = [x for x in records if x['primary_category'] == category]
    missing = [x['lucide_name'] for x in subset if x['status'] == 'missing']
    missing_by_category[category] = {'reference_count': len(subset), 'covered_count': sum(x['status'] in {'exact-name', 'semantic-equivalent'} for x in subset), 'contextual_count': sum(x['status'] == 'contextual-match' for x in subset), 'missing_count': len(missing), 'missing_names': missing}
batches = [{'id': key, 'title': title, 'rationale': rationale,
            'count': sum(x.get('implementation_batch') == key for x in records),
            'names': [x['lucide_name'] for x in records if x.get('implementation_batch') == key]}
           for key, title, rationale in batch_defs]
covered = counts['exact-name'] + counts['semantic-equivalent']
extension_names = [name for name in runpy.run_path(str(ROOT / 'scripts/icons/expansion.py'))['NAMES'] if name in local]
assert all(name in lucide for name in extension_names), 'Extension names must exist in the pinned reference'
extension_covered = sum(by_name[name]['status'] == 'exact-name' for name in extension_names)
data = {
    'schema_version': 1, 'audit_date': '2026-11-16',
    'reference': {'project': 'Lucide core', 'version': upstream['release']['tag_name'], 'commit': upstream['release']['target_commitish'],
                  'published_at': upstream['release']['published_at'], 'release_url': upstream['release']['html_url'],
                  'inventory_url': f'https://github.com/lucide-icons/lucide/tree/{upstream["release"]["tag_name"]}/icons',
                  'archive_url': upstream['release']['tarball_url'], 'archive_sha256': upstream['archive_sha256'],
                  'metadata_sha256': hashlib.sha256(json.dumps(lucide, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
                  'unit': 'One canonical icons/*.json entry. Excludes aliases as independent icons, Lab, and package exports.'},
    'local_snapshot': {'catalog_path': 'catalog.json', 'catalog_sha256': hashlib.sha256(catalog_bytes).hexdigest(), 'catalog_count': len(catalog),
                       'original_ui_count': sum(x['origin'] == 'original' for x in catalog), 'legacy_brand_count': sum(x['origin'] == 'legacy' for x in catalog)},
    'methodology': {'exact_name': 'Same canonical name, excluding known semantic collisions and contextual shape/state mismatches. Does not certify artwork quality.',
                    'semantic_equivalent': 'Editorially reviewed alternate local name with the same principal intent. No API alias is created by this report. Many-to-one mappings are permitted and disclosed.',
                    'missing': 'No strong existing equivalent established; includes known same-name collisions. Similar category, shared tags and broad metaphors are insufficient.',
                    'contextual_match': 'Same name with a reviewed shape/state mismatch. Not included in strong coverage; needs original drawing correction or a distinct explicit variant.',
                    'categories': 'Recursively resolve Lucide $extends: categories, deduplicate in source order. Primary category is the first resolved category, used only for disjoint totals.',
                    'limitations': 'This is a coverage and naming audit, not full visual verification. Contextual matches require separate artwork/state correction and are excluded from strong coverage. Directional text equivalents are LTR only.'},
    'summary': {'reference_canonical_count': len(lucide), 'reference_alias_count': sum(len(x.get('aliases', [])) for x in lucide.values()),
                'literal_name_intersection': len(set(local) & set(lucide)), 'excluded_name_collisions': len(collisions),
                'exact_name_count': counts['exact-name'], 'semantic_equivalent_count': counts['semantic-equivalent'], 'covered_reference_names': covered,
                'coverage_percent': round(covered / len(lucide) * 100, 2), 'missing_count': counts['missing'], 'contextual_match_count': counts['contextual-match'], 'strong_coverage_gap': counts['missing'] + counts['contextual-match'],
                'exact_name_caveat_count': len(caveats), 'local_names_used_for_coverage': len({x['local_name'] for x in records if x['status'] in {'exact-name', 'semantic-equivalent'}}),
                'strict_new_local_names_for_canonical_parity': counts['missing'], 'new_style_drawings_at_three_styles': counts['missing'] * 3, 'contextual_style_corrections_at_three_styles': counts['contextual-match'] * 3},
    'baseline_before_extension': {'catalog_count': 550, 'original_ui_count': 469, 'legacy_brand_count': 81, 'literal_name_intersection': 339, 'exact_name_count': 331, 'semantic_equivalent_count': 76, 'contextual_match_count': 6, 'covered_reference_names': 407, 'coverage_percent': 19.81, 'missing_count': 1642, 'strong_coverage_gap': 1648},
    'extension_progress': {'added_names': extension_names, 'added_canonical_count': extension_covered, 'visual_review_status': '29 delivered names passed the separate expansion audit. Handshake was deferred after ambiguous 16-point review.', 'deferred_names': ['handshake'], 'deferral_reason': 'Final handshake prototype did not resolve as interlocking hands at 16 points and was removed rather than accepted.'},
    'implementation_batches': batches, 'missing_by_primary_category': missing_by_category, 'icons': records,
}
output = ROOT / 'docs/lucide-coverage-2026-11-16.json'
json_text = json.dumps(data, indent=2, ensure_ascii=False)+'\n'

lines = [
    '# Lucide coverage audit — 2026-11-16', '',
    f'IconsCXL covers **{covered:,} of {len(lucide):,} Lucide canonical names ({covered/len(lucide)*100:.1f}%)** at a strong naming/meaning level: **{counts["exact-name"]:,} exact names** and **{counts["semantic-equivalent"]:,} reviewed alternate names**. **{counts["missing"]:,} canonical names remain missing**, and **{counts["contextual-match"]} contextual matches require correction** ({counts["missing"] + counts["contextual-match"]:,} reference names without strong coverage). This is a large multi-batch expansion, not a nearly complete library. It also does not establish visual quality parity.', '',
    f'The local snapshot contains {len(catalog)} names: {data["local_snapshot"]["original_ui_count"]} original UI names and {data["local_snapshot"]["legacy_brand_count"]} retained brand names. Brands are valuable additional coverage but do not reduce the Lucide core gap. Existing compatibility names and multiple local variants do not count as independent Lucide concepts.', '',
    '## Pinned reference and reproducibility', '',
    f'- Official [Lucide 1.73.0 release]({upstream["release"]["html_url"]}), published {upstream["release"]["published_at"]}. Verified against GitHub’s latest-release API on the audit date.',
    f'- Commit: `{upstream["release"]["target_commitish"]}`.',
    '- Inventory: one canonical `icons/*.json` entry in the [tagged upstream tree](https://github.com/lucide-icons/lucide/tree/1.73.0/icons). Lab is excluded. Package-export aliases are not counted as independent drawings.',
    f'- Reference contains {len(lucide):,} canonical entries and {data["summary"]["reference_alias_count"]:,} alias records.',
    f'- Local `catalog.json` SHA-256: `{data["local_snapshot"]["catalog_sha256"]}`.',
    f'- Downloaded upstream archive SHA-256: `{upstream["archive_sha256"]}`.',
    f'- Metadata-only inventory SHA-256: `{data["reference"]["metadata_sha256"]}` (UTF-8 JSON, sorted keys, compact separators).',
    '- Reproduce with `python3 scripts/icons/compare-lucide.py`; verify without writing with `--check`. Use `--inventory METADATA.json` to supply another metadata snapshot with the same schema. The default [checked-in inventory](../scripts/icons/lucide-1.73.0.json) contains the pinned upstream metadata only.',
    '- [Machine-readable report](lucide-coverage-2026-11-16.json) contains every canonical name, all upstream aliases, resolved categories, status, local mapping, caveats, and one implementation batch for every missing name. Snapshot hashes intentionally become stale when the catalog changes; rerun the comparison after implementation.', '',
    'Only names, alias metadata and categories are used as the reference. No Lucide path data is distributed or adopted. New geometry must be authored under [DESIGN.md](DESIGN.md) and [STYLE.md](../scripts/icons/STYLE.md).', '',
    '## Delivered first extension slice', '',
    f'The catalog grew from **550 to {len(catalog)} names** with {len(extension_names)} original additions: ' + ', '.join(f'`{name}`' for name in extension_names) + '. Their three styles are generated by the shared authoring pipeline; visual acceptance is recorded separately in the dated design audit. `handshake` was deferred after its final 16-point review remained ambiguous, and its three prototype SVGs were removed. It remains in the missing backlog; failed review evidence is preserved in `audit-2026-11-16-expansion.json`.', '',
    f'Before this slice, strong coverage was **407 / 2,055 (19.8%)**, with 1,642 missing canonical names and six contextual mismatches. The slice adds {extension_covered} canonical concepts, reaching **{covered:,} / {len(lucide):,} ({covered/len(lucide)*100:.1f}%)**, with {counts["missing"]:,} missing names and the same six contextual mismatches. This is measurable initial progress; the full reference backlog remains explicit.', '',
    '## Counting rules and cautions', '',
    'An exact-name match is a discoverability/name match, not a visual sign-off. A semantic equivalent is an existing alternate local name with the same principal intent. It is not a shipped API alias: documentation or explicit compatibility aliases would still be needed for users migrating from Lucide. Several canonical variants can map to one local drawing; the JSON discloses that relationship. Similar tags or a generic metaphor do not establish coverage.', '',
    f'The literal intersection is {data["summary"]["literal_name_intersection"]} names. Two collisions and six contextual matches are excluded from strong coverage:', '',
    '- `pi`: IconsCXL retains a Pi brand mark; Lucide means the mathematical constant. Add an original mathematical symbol under an unambiguous API name and preserve the existing brand API.',
    '- `chart-bar`: IconsCXL draws vertical columns. It maps to Lucide `chart-column`; a horizontal bar chart is still missing. Preserve compatibility when clarifying names.', '',
    'Contextual name matches excluded from strong coverage (six drawing/state corrections):', '',
]
for name, reason in caveats.items():
    lines.append(f'- `{name}`: {reason}')
lines += ['', 'Historical upstream aliases are evidence, not automatic matches. `file-headphone`/`file-audio`, `mic-signal`/`podcast`, `sliders-vertical`/`sliders` and `tram-front`/`train` were rejected because current local recipes depict different details. Left/right text-alignment mappings cover left-to-right interfaces; logical start/end behavior still needs direction-aware selection.', '',
          'Lucide categories overlap and sometimes inherit through `$extends:` references. This report resolves inheritance recursively and assigns each name to its first resolved category only for disjoint totals; all categories remain in JSON. A category label does not imply specialist fitness, medical or accessibility validation.', '',
          '## Reviewed alternate names', '', '| Lucide canonical name | Existing IconsCXL name | Reason |', '| --- | --- | --- |']
for record in records:
    if record['status'] == 'semantic-equivalent':
        lines.append(f'| `{record["lucide_name"]}` | `{record["local_name"]}` | {record["reason"]} |')
lines += ['', '## Prioritized implementation program', '',
          f'One original name for every remaining canonical entry would require **{counts["missing"]:,} additions** and up to **{counts["missing"]*3:,} new style drawings** across default, Solid and Stroke, before rendering and review. That would take the local catalog to approximately **{len(catalog)+counts["missing"]:,} names**. Six contextual name/state mismatches also require corrections or explicit new variants (up to 18 style corrections). Some reference variants may share an authored base; they still need independent semantic, style and small-size inspection. A smaller “roughly Lucide” goal should explicitly select families and report the remaining gaps.', '',
          'Implement the following ordered batches as 20–40 icon slices. Complete the full family and all three supported styles together, with new noun silhouettes before purely decorative variants. Treat the final batch as a review decision, not an instruction to inflate the count.', '',
          '| Order | Scope | Missing names |', '| --- | --- | ---: |']
for batch in batches:
    lines.append(f'| {batch["id"]} | {batch["title"]} | {batch["count"]} |')
lines += ['', f'### First product-foundation pool ({len(priority_names)} names)', '',
          'These are the recommended additions to draw first; this is a coverage proposal, not a claim they are implemented. Prioritize state families beside their existing bases and address the `pi` and `chart-bar` name collisions deliberately.', '',
          ', '.join(f'`{n}`' for n in priority_names)+'.', '',
          '### Acceptance gate for every slice', '',
          'Author original geometry in `draw.py`; preserve public names and platform availability; justify every secondary tone by surface/depth; inspect 16/24/32-point light/dark native renders in all three styles beside the nearest existing family; reject crowded details and ambiguous states; run repository validation, packaging, and native macOS/iOS checks; update reviewed hashes only after inspecting the drawings. A successful generated name or file is not visual acceptance.', '',
          '## Missing names by primary reference category', '',
          '| Category | Reference names | Strong coverage | Contextual | Missing |', '| --- | ---: | ---: | ---: | ---: |']
for category, item in missing_by_category.items():
    lines.append(f'| {category} | {item["reference_count"]} | {item["covered_count"]} | {item["contextual_count"]} | {item["missing_count"]} |')
for category, item in missing_by_category.items():
    if item['missing_count']:
        lines += ['', f'### {category} ({item["missing_count"]})', '', ', '.join(f'`{n}`' for n in item['missing_names'])+'.']
lines += ['', '## Verification boundary', '',
          'This report compares pinned upstream metadata with the checked-in local catalog and selected authoring recipes. It does not certify that all exact-name drawings communicate every upstream state, and it does not replace the complete-set native visual audit. The report itself does not create public aliases; the first original extension slice is documented above. Counts describe this snapshot and must be refreshed after additions.']
markdown_text = '\n'.join(lines)+'\n'
outputs = {output: json_text, ROOT / 'docs/COVERAGE-2026-11-16.md': markdown_text}
if args.check:
    stale = [str(path.relative_to(ROOT)) for path, text in outputs.items() if not path.exists() or path.read_text() != text]
    if stale:
        raise SystemExit('Stale coverage reports: ' + ', '.join(stale))
    print('Coverage reports are current.')
else:
    for path, text in outputs.items():
        path.write_text(text)
print(json.dumps(data['summary'], indent=2))
print('batches', [(x['id'], x['count']) for x in batches])
