# stack

Monorepo of the `@hugocxl` libraries, Swift package (`hugocxlStack`), `@hugocxl/ai`, and the shared GitHub Actions workflows and script/hook templates used by all `hugocxl/*` repositories.

## Commands

```sh
pnpm install                  # workspace install (never use npm at root)
pnpm test                     # every package's tests
pnpm build:site && pnpm check:site
swift test                    # hugocxlStack Swift package
```

## Why & Invariants

- Use `pnpm` for workspace installs, never `npm` — releases still pack and publish with `npm` because npm trusted publishing requires it.
- Keep packages independent: a library depends on another's published npm version, never the workspace copy, so each package ships on its own schedule.
- `.github/workflows/reusable-*.yml` and `templates/` are the single source of truth for all `hugocxl/*` repos. Keep inputs backward-compatible when editing them.
- Each subpackage has its own `AGENTS.md` for package-specific commands and invariants; read it before changing that folder.
- Never use bare `git stash` (it is shared across worktrees).

## Commits & Releases

- Commit and push only when asked.
- Commit messages must use `<Added|Changed|Removed|Improved|Fixed>: <One user-facing sentence.>` (enforced by `.githooks/commit-msg`).
- A push to `main` that touches a package folder releases that package to npm with provenance and tags `<folder>-v<version>`.
