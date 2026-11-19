#!/usr/bin/env node
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';

// Versions published before the package moved into the hugocxl/stack monorepo, whose run
// numbers start again from 1.
export const PREVIOUS_RELEASES = 11;

// The workflow run number is stable across retries and unique across pushes.
export function releaseVersion(runNumber) {
  if (!/^[1-9]\d*$/.test(String(runNumber)) || !Number.isSafeInteger(Number(runNumber))) {
    throw new Error('A positive, safe GitHub Actions run number is required');
  }
  return `0.1.${PREVIOUS_RELEASES + Number(runNumber)}`;
}

// Release tags share the monorepo, so each one names its package.
export function releaseTag(version) {
  return `vectors-v${version}`;
}

export function stampVersion(manifests, version) {
  for (const manifest of Object.values(manifests)) manifest.version = version;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const version = releaseVersion(process.env.GITHUB_RUN_NUMBER);
  const paths = ['packages/vectors'];
  const manifests = Object.fromEntries(paths.map(path => [path, JSON.parse(readFileSync(`${path}/package.json`))]));
  stampVersion(manifests, version);
  for (const [path, manifest] of Object.entries(manifests)) {
    writeFileSync(`${path}/package.json`, JSON.stringify(manifest, null, 2) + '\n');
  }
  mkdirSync('release', { recursive: true });
  execFileSync('npm', ['pack', '--workspaces', '--pack-destination', 'release'], { stdio: 'inherit' });
  const files = readdirSync('release').filter(file => file.endsWith('.tgz')).sort();
  if (files.length !== 1) throw new Error('Expected exactly one release tarball');
  const sums = files.map(file => `${createHash('sha256').update(readFileSync(`release/${file}`)).digest('hex')}  ${file}`);
  writeFileSync('release/SHA256SUMS', sums.join('\n') + '\n');
  if (process.env.GITHUB_OUTPUT) {
    writeFileSync(process.env.GITHUB_OUTPUT, `version=${version}\ntag=${releaseTag(version)}\n`, { flag: 'a' });
  }
}
