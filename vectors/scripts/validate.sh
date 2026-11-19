#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -I scripts/verify.py --expect 2000 --similarity .965
python3 -I scripts/generate.py --check
npm test
npm run typecheck
npm pack --workspaces --dry-run --json > /dev/null
npm run build:site
npm run check:site
echo "validation passed"
