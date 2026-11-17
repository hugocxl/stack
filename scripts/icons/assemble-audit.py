#!/usr/bin/env python3
"""Assemble manually inspected ledgers; never infer verdicts or refresh hashes."""
import collections
import hashlib
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ['audit-quality-baseline.json', 'audit-quality-design.json',
           'audit-quality-product.json', 'audit-quality-technology.json',
           'audit-quality-world.json']
entries = {}
for filename in SOURCES:
    source = json.loads((ROOT / 'docs' / filename).read_text())
    for original in source.get('entries', source.get('icons', [])):
        entry = dict(original)
        entry['styles'] = entry.get('styles', entry.get('checkedStyles', entry.get('stylesReviewed')))
        entry['verdict'] = entry.get('verdict', entry.get('status'))
        entry['finding'] = entry.get('finding', entry.get('rationale', entry.get('notes', '')))
        entry['reviewSource'] = filename
        entries[entry['name']] = entry
catalog = json.loads((ROOT / 'catalog.json').read_text())
assert set(entries) == {i['name'] for i in catalog}, 'Incomplete visual review'
for icon in catalog:
    entry = entries[icon['name']]
    entry.setdefault('category', icon['category'])
    assert entry['category'] == icon['category']
    assert set(entry['sha256']) == set(icon['styles'])
    for style in icon['styles']:
        relative = f"{icon['name']}.svg" if style == 'duotone' else f"styles/{style}/{icon['name']}.svg"
        assert hashlib.sha256((ROOT / 'icons' / relative).read_bytes()).hexdigest() == entry['sha256'][style], f"Stale review: {relative}"
report = dict(date='2026-11-17', reviewers='Codex full-catalog quality audit with independent cross-review of changed families',
              method='Fresh AppKit visual inspection of every catalog name; all styles at 16/24/32pt, light/dark, 1x/2x. Changed artwork re-rendered and re-inspected. AI assessment, not human design certification.',
              sizesPoints=[16, 24, 32], rasterScales=[1, 2], tints=['light', 'dark'],
              counts=dict(collections.Counter(e['verdict'] for e in entries.values())),
              entries=sorted(entries.values(), key=lambda e: e['name']))
(ROOT / 'docs/design-audit-2026-11-17.json').write_text(json.dumps(report, indent=2) + '\n')
head = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>IconsCXL quality audit</title>
<style>body{font:15px system-ui;margin:24px;background:#f5f5f5;color:#222}header{position:sticky;top:0;background:#f5f5f5;padding:16px 0}input,select{font:inherit;padding:8px}article{background:white;border:1px solid #ccc;border-left:5px solid #39804c;border-radius:8px;padding:16px;margin:16px 0}article[data-verdict=fail]{border-left-color:#b32b22}article[data-verdict=needs-review]{border-left-color:#a76a00}.matrix{display:flex;flex-wrap:wrap;gap:16px}.pair{display:flex}.tile{display:flex;align-items:center;justify-content:center;gap:16px;padding:12px;background:#fafafa;min-width:140px}.dark{background:#171717}.dark img{filter:invert(1)}h2{font-size:18px}p{max-width:960px}</style>
<h1>IconsCXL quality audit · 17 November 2026</h1><p>Every current name has an individual visual assessment. Previews use current SVGs; the JSON ledger binds verdicts to reviewed SHA-256 hashes. Native evidence covers 16/24/32 points, both tints, 1×/2×. Browser previews are not native-rendering evidence.</p><p><a href="QUALITY-AUDIT-2026-11-17.md">Findings and validation</a> · <a href="quality-changes-2026-11-17.html">Before and after</a> · <a href="design-audit-2026-11-17.json">Full ledger</a> · <a href="COVERAGE-2026-11-16.md">Lucide coverage</a></p>
<header><input id="search" placeholder="Search icons or findings" aria-label="Search"><select id="verdict" aria-label="Verdict"><option value="all">All icons</option><option value="issues">Open findings</option><option value="pass">Pass</option><option value="fail">Fail</option><option value="needs-review">Needs review</option></select> <span id="count"></span></header><main>'''
cards=[]
for entry in report['entries']:
    name=entry['name']
    matrix=''
    for style in entry['styles']:
        src=f'../icons/{name}.svg' if style=='duotone' else f'../icons/styles/{style}/{name}.svg'
        sizes=''.join(f'<img src="{src}" alt="{html.escape(name)} {style} {size}px" width="{size}" height="{size}" loading="lazy">' for size in (16,24,32))
        matrix+=f'<section><b>{style}</b><div class="pair"><div class="tile">{sizes}</div><div class="tile dark">{sizes}</div></div></section>'
    cards.append(f'<article data-verdict="{entry["verdict"]}"><h2>{name} · {entry["verdict"]}</h2><p>{html.escape(entry["finding"])}</p><div class="matrix">{matrix}</div></article>')
script='''</main><script>const search=document.querySelector('#search'),verdict=document.querySelector('#verdict'),cards=[...document.querySelectorAll('article')];function filter(){let n=0;for(const card of cards){const v=verdict.value;card.hidden=!(card.textContent.toLowerCase().includes(search.value.toLowerCase())&&(v==='all'||(v==='issues'?card.dataset.verdict!=='pass':card.dataset.verdict===v)));if(!card.hidden)n++;}document.querySelector('#count').textContent=n+' icons';}search.addEventListener('input',filter);verdict.addEventListener('change',filter);filter();</script></html>'''
(ROOT / 'docs/design-audit-2026-11-17.html').write_text(head+'\n'.join(cards)+script)
# Keep the small current batch easy to review without searching the full family.
focused_names = {entry['name'] for entry in json.loads(
    (ROOT / 'docs/audit-sf-2026-11-17.json').read_text())['entries']}
focused_head = head.replace('IconsCXL quality audit · 17 November 2026',
                            '35 new icons · subtle polish')
focused_head = focused_head.replace('Every current name has an individual visual assessment.',
    'SF Symbols-inspired coverage, drawn in the existing IconsCXL language. '
    '35 additions and refinements to AirPlay, Zoom In and Zoom Out. '
    'Each row shows default, Solid and Stroke in light and dark at 16, 24 and 32px.')
focused_cards = [card for entry, card in zip(report['entries'], cards)
                 if entry['name'] in focused_names]
(ROOT / 'docs/sf-expansion-2026-11-17.html').write_text(
    focused_head+'\n'.join(focused_cards)+script)
print(report['counts'])
