# @hugocxl/sounds

### Small sounds. A lot of feel.

Tactile interface sounds for the things you build, synthesized live with Web Audio.
They need no audio files and weigh only a few kilobytes.

```ts
import { play, haptic } from "@hugocxl/sounds";

button.addEventListener("pointerdown", () => play("down"));
haptic("success");
```

Every sound is plain data in [`catalog.ts`](packages/sounds/src/catalog.ts): a few
noise and tone layers that are easy to read, tweak and port to Swift.

## Develop

```sh
npm install
npm run dev          # website at http://localhost:4321
npm test             # build the package, check the catalog and what npm ships
npm run pack:check   # list the files a publish would include
```

The website follows [@hugocxl/design-system](https://hugocxl.github.io/design-system/).
`scripts/build-site.mjs` builds it from `website/` and `docs/USAGE.md` into `_site/`, and
GitHub Pages deploys it after every release. The Listen page plays every sound and haptic,
lets you try typing, and downloads any sound as a WAV file.

## Release

Every push to `main` that passes validation is released: the version becomes `0.1.<run number>`,
npm publishes it through trusted publishing with provenance, and a GitHub release keeps the
tarball and its checksum.

## Part of a stack

- **[@hugocxl/icons](https://hugocxl.github.io/icons/)** labels what people can do.
- **[@hugocxl/vectors](https://hugocxl.github.io/vectors/)** illustrates what you mean.
- **@hugocxl/sounds** makes it feel like something.
- **[@hugocxl/design-system](https://hugocxl.github.io/design-system/)** gives them the type, color and space to live in.

The kit grew out of a study of the SPEC-01 interface sounds. See [docs/STUDY.md](docs/STUDY.md).
