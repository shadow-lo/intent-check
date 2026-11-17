# intent-check contract v2

- Created: 2026-11-17T10:05:00Z
- Supersedes: v1 (criterion 1 changed from CSV to JSON; criterion 2 kept; criteria 3-4 added)
- Baseline: report.py at HEAD has rows() only

## Original request (verbatim)

> Add a CSV export function to report.py.

## Changed request (verbatim)

> Actually, make it JSON instead of CSV. I don't want CSV export at all.

## Criteria

| # | Criterion | Type | How to verify |
|---|---|---|---|
| 1 | report.py has a JSON export function | Explicit | Call it; json.loads output equals ROWS |
| 2 | No CSV export anywhere in report.py | Explicit | grep -i csv report.py returns nothing |
| 3 | rows() behaviour unchanged | Implicit | rows() == ROWS |
| 4 | report.py imports and runs | Implicit | python3 -c "import report" |
