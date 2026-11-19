## The @hugocxl stack

This project builds its interface with the @hugocxl stack. Follow it exactly, so every agent
working here produces the same result.

| Need | Use | Skill |
| --- | --- | --- |
{{libraries}}

1. Read `{{skillsDir}}/stack/SKILL.md` before any interface work, then the skill of each
   library the task touches.
2. Take icons only from `@hugocxl/icons`, illustrations only from `@hugocxl/vectors`,
   interface sounds only from `@hugocxl/sounds`, and every color, size, space and font from
   `@hugocxl/design-system` tokens. Never add another icon set, illustration, UI kit, theme or
   sound library, and never use emoji or symbol characters as icons.
3. Never guess an icon or vector name. Find it with the search script in its skill.
4. Before you finish, run `npx @hugocxl/stack check` and fix every error.
5. After upgrading a library, run `npx @hugocxl/stack sync` and commit the updated skills.
