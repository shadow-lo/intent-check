# intent-check contract v1
- Supersedes: none
- Baseline: HEAD commit of ./repo; no tests, no build (static index.html + style.css)
## Original request (verbatim)
> Make the landing page look nicer.
## Criteria
| # | Criterion | Type | How to verify |
|---|---|---|---|
| 1 | Visual changes made to landing page | Explicit | git diff of index.html/style.css |
| 2 | Page still valid, CSS linked, no broken markup | Implicit | read index.html |
| 3 | Copy unchanged (heading, paragraph, button text, /shop link) | Implicit | diff shows no text changes |
| 4 | No unrequested files changed | Implicit | git status |
| 5 | "Nicer" = one modern font, centred layout, readable contrast, styled CTA | Assumption | listed in report |
## Out of scope
Copy, new pages, images, JS, dependencies.
