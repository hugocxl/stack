import { cpSync, mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';

const FIXTURES = new URL('./fixtures/packages/', import.meta.url);

/** A throwaway project with the given fixture libraries installed and files written. */
export function project({ libraries = ['design-system', 'icons', 'vectors', 'sounds'], files = {}, manifest = {} } = {}) {
  const root = mkdtempSync(join(tmpdir(), 'stack-test-'));
  writeFileSync(join(root, 'package.json'), JSON.stringify({ name: 'fixture', private: true, ...manifest }, null, 2));
  for (const id of libraries) cpSync(new URL(id, FIXTURES), join(root, 'node_modules/@hugocxl', id), { recursive: true });
  for (const [path, content] of Object.entries(files)) {
    mkdirSync(dirname(join(root, path)), { recursive: true });
    writeFileSync(join(root, path), content);
  }
  return root;
}

/** Run the CLI in-process and capture its output. */
export async function run(main, argv) {
  const out = [];
  const code = await main(argv, { log: line => out.push(line), error: line => out.push(line) });
  return { code, output: out.join('\n') };
}
