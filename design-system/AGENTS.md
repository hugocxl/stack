# Working on @hugocxl/design-system

The design system shared by every @hugocxl project, published as the npm package
`@hugocxl/design-system`. The repository root is the package and its reference page.

## Layout

- `system/ds.css`: every style and token. The source of truth.
- `index.html`: the reference page; each component has a live specimen.
- `DESIGN.md`: the complete definition agents read. Its component markup is copied from the
  specimens in `index.html` by `npm run sync`; never edit those blocks by hand.
- `dist/`: token exports (Tailwind v3 and v4, CSS, Sass, JS, JSON) generated from
  `system/ds.css` by `npm run build`. Never edit them by hand.
- `system/plan.schema.json`: the page plan schema. `skills/design-system/SKILL.md`: the agent
  skill (below).
- Icons and vectors on the reference page come from `@hugocxl/icons` and `@hugocxl/vectors`
  (`npm run sync` copies their artwork).

## Check before you commit

```sh
npm ci
npx playwright install --with-deps chromium
npm run sync && npm run build
npm test               # DESIGN.md lint, sync and export drift, skill check, browser tests
```

## The agent skill

`skills/design-system/SKILL.md` is what agents in other projects read; it points them to
`DESIGN.md` for the full definition. It ships in the npm package and is installed into
projects by [@hugocxl/stack](https://github.com/hugocxl/stack). When you add a recipe, an
export path or a rule agents must not break, update the skill in the same commit;
`scripts/check-skill.mjs` checks its export paths and recipes.

## Releases

Every push to `main` that passes CI publishes a new npm version and a GitHub release, then
rebuilds the websites that use the design system. Work on a branch and merge when it is
ready. Write commit messages as a short imperative sentence.
