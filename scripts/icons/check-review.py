#!/usr/bin/env python3
"""Reject missing or stale visual reviews; never create review approval automatically."""
import hashlib
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
# docs/audit.json holds one visual verdict per name, bound to the SHA-256 of every
# style's SVG. Hash integrity and design acceptance are separate gates:
# --strict-design also rejects any unresolved design finding.
current = root / 'docs/audit.json'
audit = json.loads(current.read_text())
catalog = json.loads((root / 'catalog.json').read_text())
entries = {entry['name']: entry for entry in audit['entries']}
assert len(entries) == len(audit['entries']), 'Duplicate current audit entries'
assert set(entries) == {icon['name'] for icon in catalog}, 'Current audit coverage differs from catalog'
assert audit['sizesPoints'] == [16,24,32] and audit['rasterScales'] == [1,2]
assert audit['tints'] == ['light','dark']
unresolved=[]
count=0
for icon in catalog:
    entry=entries[icon['name']]
    assert entry['category'] == icon['category']
    assert entry['verdict'] in {'pass','fail','needs-review'}
    assert entry['finding'].strip() and entry['evidence']
    assert set(entry['sha256']) == set(icon['styles'])
    for style in icon['styles']:
        relative = f"{icon['name']}.svg" if style == 'duotone' else f"styles/{style}/{icon['name']}.svg"
        actual=hashlib.sha256((root/'icons'/relative).read_bytes()).hexdigest()
        assert actual == entry['sha256'][style], f"Stale visual review: {icon['name']}/{style}"
        count+=1
    if entry['verdict'] != 'pass': unresolved.append(icon['name'])
print(f'Current visual audit hashes verified: {len(entries)} names, {count} SVGs; {len(unresolved)} unresolved design findings.')
if '--strict-design' in sys.argv and unresolved:
    sys.exit('Strict design acceptance blocked: '+', '.join(unresolved))
