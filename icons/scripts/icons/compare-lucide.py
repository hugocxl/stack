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
parser.add_argument('--require-complete', action='store_true', help='Fail if any canonical reference concept lacks a strong mapping.')
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
# These public names remain unchanged for compatibility. Dedicated variants
# now provide every precise canonical meaning without reinterpreting old APIs.
compatibility_variants = {
    'pi': ('math-pi', 'Mathematical pi; the existing pi API remains the retained Pi brand mark.'),
    'chart-bar': ('chart-bar-horizontal', 'Horizontal bars; existing chart-bar remains vertical and covers chart-column.'),
    'play': ('play-triangle', 'Unframed play triangle; existing play retains its enclosing circle.'),
    'pause': ('pause-bars', 'Unframed pause bars; existing pause retains its enclosing circle.'),
    'video': ('video-camera', 'Camcorder/video-camera silhouette; existing video retains its film/player drawing.'),
    'radio': ('radio-signal', 'Broadcast signal; existing radio remains a radio receiver and covers radio-receiver.'),
    'volume': ('volume-none', 'Speaker without sound waves; existing volume retains two waves and covers volume-2.'),
    'volume-off': ('volume-slash', 'Speaker with a cancellation slash; existing volume-off retains an X and covers volume-x.'),
}
equivalents.update(compatibility_variants)


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
    # A known shape/state collision must use the dedicated semantic variant,
    # even though the historical canonical-looking local name still exists.
    if name in compatibility_variants or name not in local and name in equivalents:
        target, reason = equivalents[name]
        assert target in local, ('Missing semantic mapping target', name, target)
        record.update(status='semantic-equivalent', local_name=target, reason=reason,
                      equivalence_basis='upstream-alias-and-editorial-review' if target in alias_matches else 'editorial-review')
        if name in compatibility_variants:
            record['preserved_local_compatibility_name'] = name
            record['resolved_name_difference'] = 'brand-collision' if name == 'pi' else 'orientation-collision' if name == 'chart-bar' else 'shape-or-state-difference'
    elif name in local:
        record.update(status='exact-name', local_name=name)
    else:
        record.update(status='missing', local_name=None)
    records.append(record)

by_name = {r['lucide_name']: r for r in records}
counts = collections.Counter(r['status'] for r in records)
covered = counts['exact-name'] + counts['semantic-equivalent']
gap = counts['missing']
if args.require_complete and gap:
    raise SystemExit(f'Incomplete reference coverage: {gap} canonical concepts lack strong mappings.')

by_category = {}
for category in sorted({r['primary_category'] for r in records}):
    subset = [r for r in records if r['primary_category'] == category]
    missing = [r['lucide_name'] for r in subset if r['status'] == 'missing']
    by_category[category] = {'reference_count': len(subset), 'covered_count': len(subset)-len(missing),
                             'contextual_count': 0, 'missing_count': len(missing), 'missing_names': missing}

# Four authoring ownership groups completed one delivery phase. These are not
# separate releases or future batches. Scope metadata retains the earlier
# coverage proposal for reproducibility; only canonical names are used here.
delivery_groups = []
new_names = set()
for group, title in [
    ('product', 'Application workflows, identity and planning'),
    ('design', 'Design, typography, layout, mathematics and navigation'),
    ('technology', 'Development, devices, connectivity, media and analytics'),
    ('world', 'Physical world, health, nature, travel and recreation'),
]:
    scope = json.loads((ROOT / f'scripts/icons/full/{group}-scope.json').read_text())
    canonical_names = [r['lucide_name'] for r in scope]
    if group == 'technology':
        canonical_names += ['play', 'pause', 'video', 'radio', 'volume', 'volume-off']
    group_names = [by_name[n]['local_name'] for n in canonical_names if n in by_name and by_name[n]['local_name']]
    for name in canonical_names:
        if name in by_name:
            by_name[name]['delivery_phase'] = 'full-reference-expansion'
            by_name[name]['authoring_group'] = group
    new_names.update(group_names)
    delivery_groups.append({'group': group, 'title': title, 'reference_concept_count': len(canonical_names),
                            'delivered_concept_count': len(group_names), 'local_names': sorted(group_names)})

extension_names = list(runpy.run_path(str(ROOT / 'scripts/icons/expansion.py'))['NAMES'])
assert all(name in lucide for name in extension_names), 'Historical extension names must exist in the pinned reference'
assert len(new_names) == sum(g['delivered_concept_count'] for g in delivery_groups), 'Expansion groups must not count the same local name twice'

baseline_before_extension = {
    'catalog_count': 550, 'original_ui_count': 469, 'legacy_brand_count': 81,
    'literal_name_intersection': 339, 'exact_name_count': 331, 'semantic_equivalent_count': 76,
    'contextual_match_count': 6, 'covered_reference_names': 407, 'coverage_percent': 19.81,
    'missing_count': 1642, 'strong_coverage_gap': 1648,
}
baseline_before_full_expansion = {
    'catalog_count': 579, 'original_ui_count': 498, 'legacy_brand_count': 81,
    'exact_name_count': 360, 'semantic_equivalent_count': 76, 'covered_reference_names': 436,
    'coverage_percent': 21.22, 'missing_count': 1613, 'contextual_match_count': 6, 'strong_coverage_gap': 1619,
}
data = {
    'schema_version': 2, 'audit_date': '2026-11-16',
    'reference': {
        'project': 'Lucide core', 'version': upstream['release']['tag_name'],
        'commit': upstream['release']['target_commitish'], 'published_at': upstream['release']['published_at'],
        'release_url': upstream['release']['html_url'],
        'inventory_url': f'https://github.com/lucide-icons/lucide/tree/{upstream["release"]["tag_name"]}/icons',
        'archive_url': upstream['release']['tarball_url'], 'archive_sha256': upstream['archive_sha256'],
        'metadata_sha256': hashlib.sha256(json.dumps(lucide, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        'unit': 'One canonical icons/*.json entry. Excludes aliases as independent icons, Lab, and package exports.',
    },
    'local_snapshot': {
        'catalog_path': 'catalog.json', 'catalog_sha256': hashlib.sha256(catalog_bytes).hexdigest(),
        'catalog_count': len(catalog), 'original_ui_count': sum(r['origin'] == 'original' for r in catalog),
        'legacy_brand_count': sum(r['origin'] == 'legacy' for r in catalog),
    },
    'methodology': {
        'exact_name': 'Same canonical name, excluding known brand, orientation and shape/state differences. Does not certify artwork quality.',
        'semantic_equivalent': 'Editorially reviewed alternate local name with the same principal intent. This report creates no API aliases. Every mapping is disclosed.',
        'missing': 'No strong mapping established. Similar tags, categories and broad metaphors are insufficient.',
        'categories': 'Recursively resolve Lucide $extends: categories; deduplicate in source order. First category provides disjoint totals only.',
        'compatibility': 'Eight historical same-name differences are resolved by explicit new variants. Existing public names and their geometry remain unchanged.',
        'limitations': 'Pinned semantic coverage is separate from visual quality and platform validation. Exact-name coverage is not evidence of upstream geometry or API compatibility. Logical text start/end mappings are LTR only.',
    },
    'summary': {
        'reference_canonical_count': len(lucide), 'reference_alias_count': sum(len(r.get('aliases', [])) for r in lucide.values()),
        'literal_name_intersection': len(set(local) & set(lucide)), 'excluded_name_collisions': 2,
        'exact_name_count': counts['exact-name'], 'semantic_equivalent_count': counts['semantic-equivalent'],
        'covered_reference_names': covered, 'coverage_percent': round(covered/len(lucide)*100, 2),
        'missing_count': gap, 'contextual_match_count': 0, 'strong_coverage_gap': gap,
        'exact_name_caveat_count': 0, 'resolved_compatibility_name_differences': len(compatibility_variants),
        'local_names_used_for_coverage': len({r['local_name'] for r in records if r['local_name']}),
        'strict_new_local_names_for_canonical_parity': gap, 'new_style_drawings_at_three_styles': gap*3,
        'contextual_style_corrections_at_three_styles': 0,
    },
    'baseline_before_extension': baseline_before_extension,
    'baseline_before_full_expansion': baseline_before_full_expansion,
    'first_extension_history': {
        'added_names': extension_names, 'added_canonical_count': len(extension_names),
        'catalog_count_after': 579, 'covered_reference_names_after': 436,
        'handshake_status_then': 'Deferred after ambiguous 16-point prototype review.',
        'handshake_status_now': by_name.get('handshake', {}).get('status', 'not-in-reference'),
    },
    'full_expansion_progress': {
        'delivery_phase': 'single-phase full-reference expansion', 'added_local_name_count': len(new_names),
        'added_local_names': sorted(new_names), 'resolved_missing_concepts': 1613-gap,
        'resolved_contextual_states': 6, 'authoring_groups': delivery_groups,
        'visual_review_boundary': 'Per-name native visual assessments are recorded in separate design ledgers; this comparison does not grant visual approval.',
    },
    'missing_by_primary_category': by_category, 'icons': records,
}

lines = [
    '# Lucide coverage comparison — 2026-11-16', '',
    f'@hugocxl/icons covers **{covered:,} of {len(lucide):,} pinned Lucide canonical concepts ({covered/len(lucide)*100:.1f}%)**: **{counts["exact-name"]:,} exact names** and **{counts["semantic-equivalent"]:,} reviewed alternate names**. **{gap:,} concepts remain without a strong semantic mapping.** The full reference expansion is delivered in one phase; artwork quality and platform verification have separate evidence.', '',
    f'The catalog contains **{len(catalog):,} names**: {data["local_snapshot"]["original_ui_count"]:,} original UI names and {data["local_snapshot"]["legacy_brand_count"]} retained brand names. The full phase adds **{len(new_names):,} original names** after the earlier 579-name foundation. Compatibility names and extra local variants do not increase the reference-concept count.', '',
    '## Pinned reference and reproducibility', '',
    f'- Official [Lucide {upstream["release"]["tag_name"]} release]({upstream["release"]["html_url"]}), published {upstream["release"]["published_at"]}. The metadata snapshot was pinned on the audit date.',
    f'- Commit: `{upstream["release"]["target_commitish"]}`.',
    f'- Inventory: {len(lucide):,} canonical `icons/*.json` entries and {data["summary"]["reference_alias_count"]:,} alias records. Aliases, Lab and package exports are excluded as independent concepts.',
    f'- Local `catalog.json` SHA-256: `{data["local_snapshot"]["catalog_sha256"]}`.',
    f'- Upstream archive SHA-256: `{upstream["archive_sha256"]}`.',
    f'- Metadata-only inventory SHA-256: `{data["reference"]["metadata_sha256"]}`.',
    '- Rebuild with `python3 scripts/icons/compare-lucide.py --require-complete`; check coverage and report currency without writing with `--check --require-complete`. `--inventory METADATA.json` accepts another snapshot with the same schema.',
    '- The [machine-readable report](lucide-coverage.json) lists every canonical name, resolved category, upstream alias and local mapping. Its snapshot hash changes when the catalog changes.', '',
    'Reference metadata supplies names and semantics only. All new geometry is authored in this repository under [DESIGN.md](DESIGN.md) and [STYLE.md](../scripts/icons/STYLE.md); no Lucide paths are imported.', '',
    '## Full single-phase expansion', '',
    f'The earlier foundation covered 436 / 2,055 reference concepts, leaving 1,613 missing concepts and six shape/state mismatches. This phase implements all 1,619 remaining concepts with {len(new_names)*3:,} default, Solid and Stroke SVGs. The four authoring groups are ownership boundaries within this one phase:', '',
    '| Authoring group | Added concepts | Delivered concepts |', '| --- | ---: | ---: |',
]
for group in delivery_groups:
    lines.append(f'| {group["title"]} | {group["reference_concept_count"]} | {group["delivered_concept_count"]} |')
lines += ['', 'All delivered names support the three published styles. Native per-name review and repository/platform checks remain separate acceptance gates; a successful mapping or generated file alone is not visual approval.', '',
          '## Preserved names and precise variants', '',
          'The following historical APIs retain their existing meanings. Each canonical reference concept now maps to the explicit variant shown:', '',
          '| Lucide concept / historical local name | Precise @hugocxl/icons variant | Compatibility detail |', '| --- | --- | --- |']
for name, (target, reason) in compatibility_variants.items():
    lines.append(f'| `{name}` | `{target}` | {reason} |')
lines += ['', '## Counting rules', '',
          'Exact names count once per canonical reference entry. Alternate-name mappings count only when the principal meaning agrees; similar tags and broad metaphors are insufficient. The comparison does not create API aliases or promise drop-in Lucide compatibility. Full coverage is specific to the pinned metadata version.', '',
          'Upstream historical aliases are not automatic matches. Separate `file-headphone`, `mic-signal`, `sliders-vertical` and `tram-front` drawings now cover their precise concepts; the older music-document, podcast, horizontal-slider and train drawings retain their distinct meanings. Text start/end mappings for existing left/right controls cover left-to-right interfaces; direction-aware selection is required for RTL.', '',
          'Reference categories overlap and can inherit through `$extends:` entries. All resolved categories remain in JSON; the first category is used for disjoint totals below. Category membership does not certify specialist fitness, medical or accessibility suitability.', '',
          '## Reviewed alternate names', '',
          '| Lucide canonical name | @hugocxl/icons name | Meaning |', '| --- | --- | --- |']
for record in records:
    if record['status'] == 'semantic-equivalent':
        lines.append(f'| `{record["lucide_name"]}` | `{record["local_name"]}` | {record["reason"]} |')
lines += ['', '## Coverage by primary reference category', '',
          '| Category | Reference concepts | Strong coverage | Missing |', '| --- | ---: | ---: | ---: |']
for category, item in by_category.items():
    lines.append(f'| {category} | {item["reference_count"]} | {item["covered_count"]} | {item["missing_count"]} |')
if gap:
    lines += ['', '### Uncovered concepts', '']
    lines.append(', '.join(f'`{r["lucide_name"]}`' for r in records if r['status'] == 'missing')+'.')
lines += ['', '## Earlier snapshots', '',
          '| Snapshot | Local names | Strong reference coverage | Missing | Contextual mismatches |', '| --- | ---: | ---: | ---: | ---: |',
          '| Original foundation | 550 | 407 / 2,055 | 1,642 | 6 |',
          '| First extension | 579 | 436 / 2,055 | 1,613 | 6 |',
          f'| Full single-phase expansion | {579+len(new_names):,} | {covered:,} / {len(lucide):,} | {gap:,} | 0 |',
          f'| Current catalog including later additions | {len(catalog):,} | {covered:,} / {len(lucide):,} | {gap:,} | 0 |', '',
          'The first extension added 29 accepted concepts. Its handshake prototype was deferred after an ambiguous 16-point review. The full phase authors the handshake concept anew and records its current assessment separately. Earlier audit verdicts remain in the git history rather than being rewritten as current approvals.', '',
          '## Verification boundary', '',
          'This comparison establishes canonical concept/name coverage against the pinned metadata. Current geometry, opacity, native rendering and platform integration are evaluated by their own gates and per-name review records. Snapshot hashes make report currency reproducible. Public package/release state is verified separately from local coverage.']

outputs = {
    ROOT/'docs/lucide-coverage.json': json.dumps(data, indent=2, ensure_ascii=False)+'\n',
    ROOT/'docs/COVERAGE.md': '\n'.join(lines)+'\n',
}
if args.check:
    stale = [str(path.relative_to(ROOT)) for path, content in outputs.items() if not path.exists() or path.read_text() != content]
    if stale:
        raise SystemExit('Stale coverage reports: '+', '.join(stale))
    print('Coverage reports are current.')
else:
    for path, content in outputs.items():
        path.write_text(content)
print(json.dumps(data['summary'], indent=2))
