# Lucide coverage comparison — 2026-11-16

@hugocxl/icons covers **2,055 of 2,055 pinned Lucide canonical concepts (100.0%)**: **1,971 exact names** and **84 reviewed alternate names**. **0 concepts remain without a strong semantic mapping.** The full reference expansion is delivered in one phase; artwork quality and platform verification have separate evidence.

The catalog contains **2,462 names**: 2,381 original UI names and 81 retained brand names. The full phase adds **1,619 original names** after the earlier 579-name foundation. Compatibility names and extra local variants do not increase the reference-concept count.

## Pinned reference and reproducibility

- Official [Lucide 1.73.0 release](https://github.com/lucide-icons/lucide/releases/tag/1.73.0), published 2026-11-14T06:04:58Z. The metadata snapshot was pinned on the audit date.
- Commit: `55782beff3a0133df79c417eb68f96e8f19e2404`.
- Inventory: 2,055 canonical `icons/*.json` entries and 304 alias records. Aliases, Lab and package exports are excluded as independent concepts.
- Local `catalog.json` SHA-256: `fc86604f8d8d63474844cb1792b7f122d3b3b0eebb6fc53d7628d495846444e1`.
- Upstream archive SHA-256: `f5469fa3574960f5e62780160204512766e1463d5d8b0a9c95515d058fd6062c`.
- Metadata-only inventory SHA-256: `f8da62ef9b13b3ba9fdd62ba31bed8966ce2dc1a9cbc194e6cb2d13ce5466962`.
- Rebuild with `python3 scripts/icons/compare-lucide.py --require-complete`; check coverage and report currency without writing with `--check --require-complete`. `--inventory METADATA.json` accepts another snapshot with the same schema.
- The [machine-readable report](lucide-coverage.json) lists every canonical name, resolved category, upstream alias and local mapping. Its snapshot hash changes when the catalog changes.

Reference metadata supplies names and semantics only. All new geometry is authored in this repository under [DESIGN.md](DESIGN.md) and [STYLE.md](../scripts/icons/STYLE.md); no Lucide paths are imported.

## Full single-phase expansion

The earlier foundation covered 436 / 2,055 reference concepts, leaving 1,613 missing concepts and six shape/state mismatches. This phase implements all 1,619 remaining concepts with 4,857 default, Solid and Stroke SVGs. The four authoring groups are ownership boundaries within this one phase:

| Authoring group | Added concepts | Delivered concepts |
| --- | ---: | ---: |
| Application workflows, identity and planning | 427 | 427 |
| Design, typography, layout, mathematics and navigation | 565 | 565 |
| Development, devices, connectivity, media and analytics | 295 | 295 |
| Physical world, health, nature, travel and recreation | 332 | 332 |

All delivered names support the three published styles. Native per-name review and repository/platform checks remain separate acceptance gates; a successful mapping or generated file alone is not visual approval.

## Preserved names and precise variants

The following historical APIs retain their existing meanings. Each canonical reference concept now maps to the explicit variant shown:

| Lucide concept / historical local name | Precise @hugocxl/icons variant | Compatibility detail |
| --- | --- | --- |
| `pi` | `math-pi` | Mathematical pi; the existing pi API remains the retained Pi brand mark. |
| `chart-bar` | `chart-bar-horizontal` | Horizontal bars; existing chart-bar remains vertical and covers chart-column. |
| `play` | `play-triangle` | Unframed play triangle; existing play retains its enclosing circle. |
| `pause` | `pause-bars` | Unframed pause bars; existing pause retains its enclosing circle. |
| `video` | `video-camera` | Camcorder/video-camera silhouette; existing video retains its film/player drawing. |
| `radio` | `radio-signal` | Broadcast signal; existing radio remains a radio receiver and covers radio-receiver. |
| `volume` | `volume-none` | Speaker without sound waves; existing volume retains two waves and covers volume-2. |
| `volume-off` | `volume-slash` | Speaker with a cancellation slash; existing volume-off retains an X and covers volume-x. |

## Counting rules

Exact names count once per canonical reference entry. Alternate-name mappings count only when the principal meaning agrees; similar tags and broad metaphors are insufficient. The comparison does not create API aliases or promise drop-in Lucide compatibility. Full coverage is specific to the pinned metadata version.

Upstream historical aliases are not automatic matches. Separate `file-headphone`, `mic-signal`, `sliders-vertical` and `tram-front` drawings now cover their precise concepts; the older music-document, podcast, horizontal-slider and train drawings retain their distinct meanings. Text start/end mappings for existing left/right controls cover left-to-right interfaces; direction-aware selection is required for RTL.

Reference categories overlap and can inherit through `$extends:` entries. All resolved categories remain in JSON; the first category is used for disjoint totals below. Category membership does not certify specialist fitness, medical or accessibility suitability.

## Reviewed alternate names

| Lucide canonical name | @hugocxl/icons name | Meaning |
| --- | --- | --- |
| `arrow-left-right` | `swap-horizontal` | Opposing horizontal direction/transfer arrows. |
| `arrow-up-down` | `swap-vertical` | Opposing vertical direction/transfer arrows. |
| `audio-waveform` | `waveform` | Audio amplitude waveform. |
| `bike` | `bicycle` | Same bicycle concept under a different noun. |
| `chart-bar` | `chart-bar-horizontal` | Horizontal bars; existing chart-bar remains vertical and covers chart-column. |
| `chart-column` | `chart-bar` | Local recipe draws vertical columns; Lucide chart-bar is horizontal. |
| `chevrons-right-left` | `chevrons-in` | Two inward-facing horizontal chevrons. |
| `circle-dollar-sign` | `dollar` | Local dollar sign has an enclosing circle. |
| `circle-exclamation-point` | `circle-alert` | Exclamation point in a circle. |
| `circle-pause` | `pause-circle-fill` | Circular pause control; historical local fill suffix is retained. |
| `circle-play` | `play-circle` | Circular play control. |
| `circle-question-mark` | `circle-help` | Question mark in a circle. |
| `circle-stop` | `stop-circle` | Circular stop control. |
| `columns-2` | `columns` | Two-column layout. |
| `eighth-notes` | `music` | Pair of connected eighth notes. |
| `face-neutral` | `meh` | Neutral facial expression. |
| `face-slightly-frowning` | `frown` | Frowning facial expression. |
| `face-slightly-smiling` | `smile` | Smiling facial expression. |
| `file-archive` | `file-zip` | Compressed/archive file with a zipper. |
| `file-down` | `file-download` | Document with downward transfer arrow. |
| `file-music` | `file-audio` | Local audio document uses a musical note, not headphones. |
| `file-play` | `file-video` | Local video document uses a play triangle. |
| `file-spreadsheet` | `file-table` | Document containing a cell grid. |
| `file-up` | `file-upload` | Document with upward transfer arrow. |
| `fingerprint-pattern` | `fingerprint` | Fingerprint identity pattern. |
| `flask-conical` | `flask` | Conical laboratory flask. |
| `folder-archive` | `folder-zip` | Compressed/archive folder with zipper. |
| `folder-down` | `folder-download` | Folder with downward transfer arrow. |
| `folder-up` | `folder-upload` | Folder with upward transfer arrow. |
| `funnel` | `filter` | Same filtering funnel. |
| `gauge` | `gauge-medium` | Analog gauge with needle; local also offers low/high/max states. |
| `git-commit-horizontal` | `git-commit` | Commit node on a horizontal branch. |
| `house` | `home` | Same home/house concept. |
| `letter-b` | `bold` | Local bold control draws a B; upstream retains bold as an alias for letter-b. |
| `list-indent-decrease` | `outdent` | Decrease text indentation. |
| `list-indent-increase` | `indent` | Increase text indentation. |
| `list-sort-ascending` | `sort-ascending` | List ordering upward/ascending. |
| `list-sort-descending` | `sort-descending` | List ordering downward/descending. |
| `loader-circle` | `spinner` | Circular loading progress indicator. |
| `luggage` | `suitcase` | Wheeled travel suitcase. |
| `message-square` | `message` | Local message uses a rounded rectangular speech bubble. |
| `message-square-check` | `message-check` | Rectangular speech bubble with check. |
| `message-square-heart` | `message-heart` | Rectangular speech bubble with heart. |
| `message-square-more` | `message-dots` | Rectangular speech bubble with ellipsis. |
| `message-square-plus` | `message-plus` | Rectangular speech bubble with plus. |
| `message-square-text` | `message-text` | Rectangular speech bubble with text lines. |
| `mic` | `microphone` | Same microphone concept. |
| `mic-off` | `microphone-off` | Microphone disabled with diagonal strike. |
| `octagon-exclamation-point` | `octagon-alert` | Octagonal warning with exclamation point. |
| `pause` | `pause-bars` | Unframed pause bars; existing pause retains its enclosing circle. |
| `paw-print` | `paw` | Animal paw print. |
| `pi` | `math-pi` | Mathematical pi; the existing pi API remains the retained Pi brand mark. |
| `play` | `play-triangle` | Unframed play triangle; existing play retains its enclosing circle. |
| `radio` | `radio-signal` | Broadcast signal; existing radio remains a radio receiver and covers radio-receiver. |
| `radio-receiver` | `radio` | Local recipe draws a radio receiver box with antenna. |
| `rotate-ccw` | `rotate-left` | Counterclockwise rotation arrow. |
| `rotate-ccw-clock` | `history` | Clock/history with counterclockwise arrow. |
| `rotate-cw` | `rotate-right` | Clockwise rotation arrow. |
| `rows-2` | `rows` | Two-row layout. |
| `server` | `server-rack` | Server rack with multiple storage units. |
| `shield-exclamation-point` | `shield-alert` | Shield containing an exclamation point. |
| `shopping-basket` | `basket` | Shopping basket with handle. |
| `sliders-horizontal` | `sliders` | Local recipe draws horizontal adjustment tracks. |
| `smartphone` | `phone-android` | Generic handheld touchscreen phone; local name is platform-specific. |
| `square-check` | `checkbox` | Checked square control. |
| `square-dashed-text` | `text-select` | Text-selection region. |
| `square-letter-p` | `parking` | Parking P inside a square. |
| `swatch-book` | `swatch` | Fanned color swatches. |
| `text-align-center` | `align-center` | Centered text lines. |
| `text-align-end` | `align-right` | Right-aligned text in a left-to-right interface; direction-sensitive. |
| `text-align-justify` | `align-justify` | Justified text lines. |
| `text-align-start` | `align-left` | Left-aligned text in a left-to-right interface; direction-sensitive. |
| `toggle-left` | `toggle-off` | Toggle thumb on the left. |
| `toggle-right` | `toggle-on` | Toggle thumb on the right. |
| `train-front` | `train` | Front-facing railway train; do not assume tram-specific coverage. |
| `tree-pine` | `tree` | Local tree has the tiered conifer silhouette. |
| `triangle-exclamation-point` | `triangle-alert` | Triangular warning with exclamation point. |
| `type` | `font` | Typographic A / font control. |
| `video` | `video-camera` | Camcorder/video-camera silhouette; existing video retains its film/player drawing. |
| `volume` | `volume-none` | Speaker without sound waves; existing volume retains two waves and covers volume-2. |
| `volume-2` | `volume` | Local speaker uses two sound waves. |
| `volume-off` | `volume-slash` | Speaker with a cancellation slash; existing volume-off retains an X and covers volume-x. |
| `volume-x` | `volume-off` | Local disabled speaker uses an X, not a slash. |
| `x` | `close` | Diagonal close/cancel cross. |

## Coverage by primary reference category

| Category | Reference concepts | Strong coverage | Missing |
| --- | ---: | ---: | ---: |
| accessibility | 22 | 22 | 0 |
| account | 99 | 99 | 0 |
| animals | 16 | 16 | 0 |
| arrows | 161 | 161 | 0 |
| buildings | 22 | 22 | 0 |
| charts | 35 | 35 | 0 |
| communication | 8 | 8 | 0 |
| connectivity | 34 | 34 | 0 |
| cursors | 14 | 14 | 0 |
| design | 81 | 81 | 0 |
| development | 85 | 85 | 0 |
| devices | 114 | 114 | 0 |
| emoji | 14 | 14 | 0 |
| files | 115 | 115 | 0 |
| finance | 45 | 45 | 0 |
| food-beverage | 78 | 78 | 0 |
| gaming | 40 | 40 | 0 |
| home | 40 | 40 | 0 |
| layout | 105 | 105 | 0 |
| letters-digits | 101 | 101 | 0 |
| mail | 21 | 21 | 0 |
| math | 29 | 29 | 0 |
| medical | 35 | 35 | 0 |
| multimedia | 61 | 61 | 0 |
| nature | 20 | 20 | 0 |
| navigation | 44 | 44 | 0 |
| notifications | 18 | 18 | 0 |
| photography | 30 | 30 | 0 |
| science | 26 | 26 | 0 |
| security | 21 | 21 | 0 |
| shapes | 44 | 44 | 0 |
| shopping | 20 | 20 | 0 |
| social | 76 | 76 | 0 |
| sports | 15 | 15 | 0 |
| sustainability | 1 | 1 | 0 |
| text | 186 | 186 | 0 |
| time | 55 | 55 | 0 |
| tools | 21 | 21 | 0 |
| transportation | 51 | 51 | 0 |
| travel | 15 | 15 | 0 |
| weather | 37 | 37 | 0 |

## Earlier snapshots

| Snapshot | Local names | Strong reference coverage | Missing | Contextual mismatches |
| --- | ---: | ---: | ---: | ---: |
| Original foundation | 550 | 407 / 2,055 | 1,642 | 6 |
| First extension | 579 | 436 / 2,055 | 1,613 | 6 |
| Full single-phase expansion | 2,198 | 2,055 / 2,055 | 0 | 0 |
| Current catalog including later additions | 2,462 | 2,055 / 2,055 | 0 | 0 |

The first extension added 29 accepted concepts. Its handshake prototype was deferred after an ambiguous 16-point review. The full phase authors the handshake concept anew and records its current assessment separately. Earlier audit verdicts remain in the git history rather than being rewritten as current approvals.

## Verification boundary

This comparison establishes canonical concept/name coverage against the pinned metadata. Current geometry, opacity, native rendering and platform integration are evaluated by their own gates and per-name review records. Snapshot hashes make report currency reproducible. Public package/release state is verified separately from local coverage.
