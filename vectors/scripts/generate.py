#!/usr/bin/env python3
"""Generate platform adapters from the canonical SVGs in figures/; --check detects drift."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG = '{http://www.w3.org/2000/svg}'
PACKAGE = 'packages/vectors'
ASSETS = 'Sources/Vectors/Resources/Vectors.xcassets'
WIDTH, HEIGHT = 480, 360
outputs = {}


def emit(path, text):
    outputs[path] = text


def symbol(stem):
    """modular-design -> ModularDesignVector, mirroring the Icon suffix used by @hugocxl/icons."""
    return ''.join(part[0].upper() + part[1:] for part in stem.split('-')) + 'Vector'


def camel(attribute):
    if attribute.startswith(('aria-', 'data-')):
        return attribute
    return re.sub(r'-([a-z])', lambda match: match.group(1).upper(), attribute)


def parse(svg):
    root = ET.parse(svg).getroot()
    title = root.find(SVG + 'title').text
    desc = root.find(SVG + 'desc').text
    paths = [dict(path.attrib) for path in root.findall(SVG + 'path')]
    attributes = {key: value for key, value in root.attrib.items() if key != 'color'}
    assert attributes.get('viewBox') == f'0 0 {WIDTH} {HEIGHT}', f'{svg.name}: unexpected viewBox'
    return attributes, title, desc, paths


def props(attributes, native):
    result = {camel(key): value for key, value in attributes.items()}
    if native:
        result.pop('xmlns', None)
        result.pop('role', None)
    else:
        result.setdefault('xmlns', 'http://www.w3.org/2000/svg')
    return json.dumps(result)


def component(stem, native):
    name = symbol(stem)
    attributes, title, desc, paths = parse(ROOT / 'figures' / f'{stem}.svg')
    head = 'import { createElement, forwardRef } from "react";\n'
    if native:
        head += 'import { Svg, Path } from "react-native-svg";\n'
        root_props = (f'{{...{props(attributes, True)}, width: size, height: size * {HEIGHT} / {WIDTH}, color, '
                      f'accessible: true, accessibilityRole: "image", accessibilityLabel: {json.dumps(title)}, ...props, ref}}')
        children = [f'createElement(Path, {props(path, True)})' for path in paths]
        target = 'Svg'
    else:
        root_props = f'{{...{props(attributes, False)}, width: size, height: size * {HEIGHT} / {WIDTH}, color, ...props, ref}}'
        children = [f'createElement("title", null, {json.dumps(title)})', f'createElement("desc", null, {json.dumps(desc)})']
        children += [f'createElement("path", {props(path, False)})' for path in paths]
        target = '"svg"'
    body = f'createElement({target}, {root_props},\n    ' + ',\n    '.join(children) + ')'
    return head + (f'export const {name} = /*#__PURE__*/ forwardRef(function {name}('
                   f'{{size = {WIDTH}, color = "currentColor", ...props}}, ref) {{\n  return {body};\n}});\n')


def declaration(stem, native):
    name = symbol(stem)
    if native:
        return ('import type { ComponentRef, ForwardRefExoticComponent, RefAttributes } from "react";\n'
                'import type { Svg, SvgProps } from "react-native-svg";\n'
                f'export declare const {name}: ForwardRefExoticComponent<Omit<SvgProps, "ref"> & '
                '{ size?: number; color?: string } & RefAttributes<ComponentRef<typeof Svg>>>;\n')
    return ('import type { ForwardRefExoticComponent, RefAttributes, SVGProps } from "react";\n'
            f'export declare const {name}: ForwardRefExoticComponent<Omit<SVGProps<SVGSVGElement>, "ref"> & '
            '{ size?: number; color?: string } & RefAttributes<SVGSVGElement>>;\n')


figures = sorted((ROOT / 'figures').glob('*.svg'), key=lambda svg: svg.stem)
stems = [svg.stem for svg in figures]
if len({symbol(stem) for stem in stems}) != len(stems):
    sys.exit('Export names collide')

# Catalog: one entry per figure, joined with the use-case manifest.
manifest = json.loads((ROOT / 'catalog/manifest.json').read_text(encoding='utf-8'))
catalog = []
for group in manifest['groups']:
    for case in group['cases']:
        if not case.get('asset'):
            continue
        stem = Path(case['asset']).stem
        _, title, desc, _ = parse(ROOT / case['asset'])
        catalog.append({
            'name': stem,
            'export': symbol(stem),
            'title': title,
            'description': desc,
            'category': group['title'],
            'categoryId': group['id'],
            'placement': case['placement'],
            'priority': case['priority'],
            'file': case['asset'],
        })
catalog.sort(key=lambda item: item['name'])
if [item['name'] for item in catalog] != stems:
    sys.exit('catalog/manifest.json and figures/ disagree; run python scripts/build.py')
emit(f'{PACKAGE}/dist/catalog.json', json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')

for platform in ['js', 'react', 'react-native']:
    native = platform == 'react-native'
    exports = []
    for svg in figures:
        base = f'{PACKAGE}/dist/{platform}/{svg.stem}'
        if platform == 'js':
            emit(base + '.js', f'export const {symbol(svg.stem)} = ' + json.dumps(svg.read_text(encoding='utf-8')) + ';\n')
            emit(base + '.d.ts', f'export declare const {symbol(svg.stem)}: string;\n')
        else:
            emit(base + '.js', component(svg.stem, native))
            emit(base + '.d.ts', declaration(svg.stem, native))
        exports.append(f'export {{ {symbol(svg.stem)} }} from "./{svg.stem}.js";')
    for ext in ['js', 'd.ts']:
        emit(f'{PACKAGE}/dist/{platform}/index.{ext}', '\n'.join(exports) + '\n')
emit(f'{PACKAGE}/LICENSE', (ROOT / 'LICENSE').read_text(encoding='utf-8'))

# Swift: a vector-preserving template asset catalog and a typed enum.
cases = []
for svg in figures:
    name = symbol(svg.stem)[:-len('Vector')]
    cases.append(f'    case `{name[0].lower() + name[1:]}` = "{svg.stem}"')
    base = f'{ASSETS}/{svg.stem}.imageset'
    emit(f'{base}/{svg.name}', svg.read_text(encoding='utf-8'))
    emit(f'{base}/Contents.json', json.dumps({
        'images': [{'filename': svg.name, 'idiom': 'universal'}],
        'info': {'author': 'xcode', 'version': 1},
        'properties': {'preserves-vector-representation': True, 'template-rendering-intent': 'template'},
    }, indent=2) + '\n')
emit(f'{ASSETS}/Contents.json', '{"info":{"author":"xcode","version":1}}\n')
emit('Sources/Vectors/Resources/LICENSE', (ROOT / 'LICENSE').read_text(encoding='utf-8'))
emit('Sources/Vectors/Vector.swift', '// Generated by scripts/generate.py.\nimport Foundation\n\n'
     '/// Every illustration in the library, named after its SVG file.\n'
     'public enum Vector: String, CaseIterable, Sendable, VectorResource {\n' + '\n'.join(cases) +
     '\n    public var resourceName: String { rawValue }\n}\n')

check = '--check' in sys.argv
failed = []
for path, text in outputs.items():
    target = ROOT / path
    if check:
        if not target.exists() or target.read_text(encoding='utf-8') != text:
            failed.append(path)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding='utf-8')
for directory in [f'{PACKAGE}/dist', ASSETS]:
    for target in (ROOT / directory).rglob('*'):
        if target.is_file() and target.relative_to(ROOT).as_posix() not in outputs:
            if check:
                failed.append(target.relative_to(ROOT).as_posix())
            else:
                target.unlink()
if failed:
    sys.exit('Generated files out of date (run pnpm run generate): ' + ', '.join(failed[:20]) +
             (f' and {len(failed) - 20} more' if len(failed) > 20 else ''))
print(f'{len(figures)} vectors: generated files ' + ('verified' if check else 'written'))
