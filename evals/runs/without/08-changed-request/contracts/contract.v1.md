# intent-check contract v1

- Created: 2026-11-17T10:00:00Z
- Supersedes: none
- Baseline: report.py has rows() only

## Original request (verbatim)

> Add a CSV export function to report.py.

## Criteria

| # | Criterion | Type | How to verify |
|---|---|---|---|
| 1 | report.py has a CSV export function | Explicit | Read report.py; call it and check CSV header + rows |
| 2 | rows() behaviour unchanged | Implicit | Call rows() and compare to ROWS |
