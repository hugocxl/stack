# Website illustration briefs

The [illustration manifest](manifest.json) covers situations where an illustration can clarify a feature, explain a process, or communicate a state. It includes general website pages and product UI, as well as commerce, media, education, health, travel, and other sector-specific uses.

Each entry describes where the figure could appear and proposes a composition. An `asset` path connects the brief to an SVG in the library. An entry without that field is a brief for future artwork.

## Priorities

- **Core** covers common website placements and widely reused product concepts.
- **Extended** covers narrower feature explanations, workflow steps, and industry-specific pages.
- **Specialist** covers domain-specific concepts that need subject knowledge or a particularly literal illustration.

## Extending the catalog

Give each brief a stable `id`, a short `title`, a concrete `placement`, a `visual` composition, and a `priority`. The build joins the [source briefs](use-cases.json) with the scene definitions and resolves asset paths in the manifest. IDs and asset paths are unique across groups.

Before adding a brief, check whether an existing figure can serve the same placement with the same visual message. A new brief earns its place when the distinction affects what a viewer needs to understand. For example, an inbox feature needs to show how incoming items are organized. An empty inbox needs to make the absence of items visible.
