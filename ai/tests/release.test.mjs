import { test } from 'node:test';
import assert from 'node:assert/strict';
import { releaseVersion, releaseTag, stampVersion } from '../scripts/prepare-release.mjs';

test('release versions come from the run number', () => {
  assert.equal(releaseVersion('42'), '0.1.42');
  assert.throws(() => releaseVersion('0'));
  assert.throws(() => releaseVersion(undefined));
});

test('stamping sets the manifest version', () => {
  const manifest = { name: '@hugocxl/ai', version: '0.1.0' };
  stampVersion(manifest, '0.1.7');
  assert.equal(manifest.version, '0.1.7');
});

test('release tags name the package', () => {
  assert.equal(releaseTag('0.1.1'), 'ai-v0.1.1');
});
