# Working on @hugocxl/sounds

Tactile interface sounds synthesized with Web Audio, published as one npm package
(`packages/sounds`, TypeScript compiled to `dist/`). The website is in `website/`.

## Layout

- `packages/sounds/src/catalog.ts`: every sound as plain data (noise and tone layers), the
  sound names and the haptic map. Tones sit on notes of G major so sounds never clash.
- `packages/sounds/src/engine.ts`: `play`, `haptic`, volume and mute. `wav.ts`: `toWav`.
- `docs/USAGE.md`: the docs page of the website. `docs/STUDY.md`: the study behind the kit.
- `packages/sounds/skills/sounds/SKILL.md`: the agent skill (below).

## Check before you commit

```sh
pnpm install
pnpm run typecheck
pnpm test               # builds, checks the catalog, the skill and what npm ships
pnpm run dev            # website at http://localhost:4321 — listen to every change
```

Listen to a changed sound before committing; tests cannot judge it.

## The agent skill

`packages/sounds/skills/sounds/SKILL.md` is what agents in other projects read. It ships in
the npm package and is installed into projects by
[@hugocxl/stack](https://github.com/hugocxl/stack). When you add, rename or remap a sound or
haptic, update the skill's table in the same commit; `tests/skill.test.mjs` fails otherwise.

## Releases

Every push to `main` that changes `sounds/` and passes `.github/workflows/sounds.yml` publishes
a new npm version and a GitHub release tagged `sounds-v<version>`, then redeploys the stack
website with it. Work on a branch and merge when it is ready. Write commit messages as a
short imperative sentence.
