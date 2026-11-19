#!/usr/bin/env bash
set -euo pipefail
: "${RELEASE_TAG:?Missing release tag}"
: "${GITHUB_SHA:?Missing source commit}"
: "${GH_REPO:?Missing repository}"

# Never move an existing version tag to different source code.
if git rev-parse --verify "refs/tags/$RELEASE_TAG" >/dev/null 2>&1; then
  test "$(git rev-parse "$RELEASE_TAG^{commit}")" = "$GITHUB_SHA"
else
  git -c tag.gpgSign=false tag "$RELEASE_TAG" "$GITHUB_SHA"
  git push origin "refs/tags/$RELEASE_TAG"
fi

# Notes start from this package's previous release, not whichever package released last.
PREVIOUS_TAG=$(git tag --list "${RELEASE_TAG%-v*}-v*" --sort=-v:refname | grep -vxF "$RELEASE_TAG" | head -n 1 || true)

if gh release view "$RELEASE_TAG" --json isDraft >/dev/null 2>&1; then
  if test "$(gh release view "$RELEASE_TAG" --json isDraft --jq .isDraft)" = false; then
    echo "Release $RELEASE_TAG is already published; nothing to change."
    exit 0
  fi
else
  gh release create "$RELEASE_TAG" --verify-tag --draft --generate-notes \
    --title "@hugocxl/design-system ${RELEASE_TAG##*-}" \
    ${PREVIOUS_TAG:+--notes-start-tag "$PREVIOUS_TAG"}
fi

# Recover incomplete drafts on retry. Publish only after every asset is uploaded.
gh release upload "$RELEASE_TAG" release/*.tgz release/SHA256SUMS --clobber
gh release edit "$RELEASE_TAG" --draft=false
