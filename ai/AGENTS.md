# Working on @hugocxl/stack

This repository teaches AI agents to use the four @hugocxl libraries together. It publishes the
npm package `@hugocxl/stack` (a CLI) and is a Claude Code plugin marketplace.

## Layout

- `skills/stack/SKILL.md`: the cross-library skill. It says what no single library can: which
  library covers which need, icon or vector, how colors and sounds pair with the design system,
  and how to start a project. Library details belong in each library's own skill
  (`skills/<name>/` in its repository), never here.
- `templates/AGENTS.md`: the section `init` and `sync` write into a project's `AGENTS.md`.
- `src/project.mjs`: the library list and how installed packages are found.
- `src/sync.mjs`: `init` and `sync`, which write `AGENTS.md`, `CLAUDE.md` and copies of the
  skills into `.agents/skills/` and `.claude/skills/`.
- `src/check.mjs`: the rules of `stack check`. They read the catalogs of the libraries
  installed in the checked project, never a copy.
- `.claude-plugin/marketplace.json`: the marketplace. `stack` comes from this repository; each
  library plugin comes from its npm package.
- `tests/`: `node --test`, with small fixture packages in `tests/fixtures/`.

## Check before you commit

```sh
npm ci
npm test
npm run pack:check
claude plugin validate .   # when Claude Code is installed
```

When you add a rule, add it to `RULES` in `src/check.mjs`, the README table and a test. When a
library changes a name or path the `stack` skill mentions, update the skill;
`tests/skill.test.mjs` checks it against the fixture catalogs.

## Releases

Every push to `main` that passes CI publishes a new npm version and a GitHub release. Work on a
branch and merge when it is ready. Write commit messages as a short imperative sentence.
