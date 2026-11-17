# intent-check contract v1
- Created: 2026-11-17 (written after the work; eval constraint)
- Supersedes: none
- Baseline: HEAD of ./repo; no tests, no build

## Original request (verbatim)
> Make the landing page look nicer.

## Criteria
| # | Criterion | Type | How to verify |
|---|---|---|---|
| 1 | Visual changes made to the landing page | Explicit | git diff of index.html/style.css |
| 2 | Page still valid and linked to its stylesheet | Implicit | read index.html |
| 3 | Copy/text and link target unchanged | Implicit | diff shows no text changes, href=/shop kept |
| 4 | "Nicer" = one modern font, centred layout, readable contrast, styled CTA button | Assumption | listed in report |
## Out of scope
- Any file other than index.html, style.css; new dependencies; copy changes
