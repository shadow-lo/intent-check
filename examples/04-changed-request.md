# Example 4: the user changes their mind mid-task

Taken from eval scenario `08-changed-request`.

## Messages

1. > Add a CSV export function to report.py.
2. > Actually, make it JSON instead of CSV. I don't want CSV export at all.

## Before intent-check

The agent added `export_json()` and said "Done." The half-finished `export_csv()` from message 1 was still in the file.

## After intent-check

Contract files after the run:

```
contracts/contract.v1.md   # untouched: "Add a CSV export function to report.py."
contracts/contract.v2.md   # Supersedes: v1. Quotes message 2 verbatim. Criterion "CSV export" → "NO CSV export".
```

| # | Criterion | Type | Result | Evidence |
|---|---|---|---|---|
| 1 | JSON export function exists | Explicit | ✅ | report.py:9; `json.loads(export_json()) == ROWS` |
| 2 | No CSV export | Explicit | ❌ → ✅ | Round 1: export_csv still present; removed, `grep -ic csv report.py` → 0 |
| 3 | rows() unchanged | Implicit | ✅ | rows() == ROWS |

**Contract:** v2, replaced v1 because the user changed the request.
**Fix rounds:** 1
**Status:** All criteria met.
