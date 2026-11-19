import { test } from 'node:test';
import assert from 'node:assert/strict';
import { releaseVersion, stampVersion } from '../scripts/prepare-release.mjs';

test('release versions come from the run number', () => {
  assert.equal(releaseVersion('42'), '0.1.42');
  assert.throws(() => releaseVersion('0'));
  assert.throws(() => releaseVersion(undefined));
});

test('stamping updates the manifest and the lockfile together', () => {
  const manifest = { name: '@hugocxl/stack', version: '0.1.0' };
  const lock = { name: '@hugocxl/stack', version: '0.1.0', packages: { '': { name: '@hugocxl/stack', version: '0.1.0' } } };
  stampVersion(manifest, lock, '0.1.7');
  assert.deepEqual([manifest.version, lock.version, lock.packages[''].version], ['0.1.7', '0.1.7', '0.1.7']);
  assert.throws(() => stampVersion({ name: 'other' }, lock, '0.1.8'));
});
