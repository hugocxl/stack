#!/usr/bin/env python3
"""Render a named icon subset in all styles at 16/24/32pt, light/dark, 1x/2x.

Accepts a JSON ledger with entries or a JSON array of icon names. Does not
approve artwork or update hashes. Requires macOS AppKit, no Python dependencies.
"""
import argparse
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('scope', type=Path)
parser.add_argument('output', type=Path)
a = parser.parse_args()
data = json.loads(a.scope.read_text())
names = set(data if isinstance(data, list) else (e['name'] for e in data['entries']))
catalog = json.loads((ROOT / 'catalog.json').read_text())
assert names <= {i['name'] for i in catalog}, 'Unknown icon names'
out = a.output.resolve()
snapshot = out / 'source'
snapshot.mkdir(parents=True, exist_ok=True)
entries = [i for i in catalog if i['name'] in names]
(snapshot / 'catalog.json').write_text(json.dumps(entries, indent=2) + '\n')
for icon in entries:
    for style in icon['styles']:
        relative = Path('icons') / (icon['name'] + '.svg' if style == 'duotone'
                    else f"styles/{style}/{icon['name']}.svg")
        target = snapshot / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)
renderer = (ROOT / 'scripts/icons/render-audit.swift').read_text()
for scale in (1, 2):
    script = out / f'render-{scale}x.swift'
    script.write_text(renderer.replace('let scale:CGFloat=2,', f'let scale:CGFloat={scale},'))
    subprocess.run(['swift', str(script), str(snapshot), str(out / f'{scale}x')], check=True)
