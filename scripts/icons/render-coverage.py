#!/usr/bin/env python3
"""Export an isolated authoring group and render its native review matrix.

Requires the authoring environment and macOS; does not approve or rehash reviews.
"""
import argparse
import contextlib
import importlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('group',choices=['design','product','technology','world'])
parser.add_argument('--output',type=Path)
a=parser.parse_args()
out=(a.output or ROOT/'review/full'/a.group).resolve()
snapshot=out/'source';snapshot.mkdir(parents=True,exist_ok=True)
import draw
module=importlib.import_module('full.'+a.group)
before=set(draw.DRAWINGS)
module.register(vars(draw))
names=set(draw.DRAWINGS)-before
brands=ROOT/'scripts/icons/brands.json'
(snapshot/'scripts/icons').mkdir(parents=True,exist_ok=True)
shutil.copy2(brands,snapshot/'scripts/icons/brands.json')
(snapshot/'icons').mkdir(exist_ok=True)
for name in json.loads(brands.read_text()):shutil.copy2(ROOT/'icons'/f'{name}.svg',snapshot/'icons'/f'{name}.svg')
draw.ROOT=snapshot
# draw.main reads only --check; do not accidentally pass it through here.
with (out/'export.log').open('w') as log,contextlib.redirect_stdout(log):draw.main()
catalog=json.loads((snapshot/'catalog.json').read_text())
(snapshot/'catalog-full.json').write_text(json.dumps(catalog,indent=2)+'\n')
(snapshot/'catalog.json').write_text(json.dumps([i for i in catalog if i['name'] in names],indent=2)+'\n')
renderer=(ROOT/'scripts/icons/render-audit.swift').read_text()
for scale in (1,2):
    script=out/f'render-{scale}x.swift';script.write_text(renderer.replace('let scale:CGFloat=2,','let scale:CGFloat='+str(scale)+','))
    with (out/f'render-{scale}x.log').open('w') as log:subprocess.run(['swift',str(script),str(snapshot),str(out/f'{scale}x')],stdout=log,check=True)
print(f'{a.group}: exported {len(names)} new icons; full matrix under {out}')
