#!/usr/bin/env node
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';

// The workflow run number is stable across retries and unique across pushes.
export function releaseVersion(runNumber) {
  if (!/^[1-9]\d*$/.test(String(runNumber)) || !Number.isSafeInteger(Number(runNumber))) {
    throw new Error('A positive, safe GitHub Actions run number is required');
  }
  return `0.1.${runNumber}`;
}

export function stampVersion(manifest, lock, version) {
  if (lock.name !== manifest.name || lock.packages?.['']?.name !== manifest.name) {
    throw new Error('The lockfile does not belong to this package');
  }
  manifest.version = version;
  lock.version = version;
  lock.packages[''].version = version;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const version = releaseVersion(process.env.GITHUB_RUN_NUMBER);
  const manifest = JSON.parse(readFileSync('package.json'));
  const lock = JSON.parse(readFileSync('package-lock.json'));
  stampVersion(manifest, lock, version);
  writeFileSync('package.json', JSON.stringify(manifest, null, 2) + '\n');
  writeFileSync('package-lock.json', JSON.stringify(lock, null, 2) + '\n');
  mkdirSync('release', { recursive: true });
  execFileSync('npm', ['pack', '--pack-destination', 'release'], { stdio: 'inherit' });
  const files = readdirSync('release').filter(file => file.endsWith('.tgz')).sort();
  if (files.length !== 1) throw new Error('Expected exactly one release tarball');
  const sums = files.map(file => `${createHash('sha256').update(readFileSync(`release/${file}`)).digest('hex')}  ${file}`);
  writeFileSync('release/SHA256SUMS', sums.join('\n') + '\n');
  if (process.env.GITHUB_OUTPUT) {
    writeFileSync(process.env.GITHUB_OUTPUT, `version=${version}\ntag=v${version}\n`, { flag: 'a' });
  }
}
