# Contract template

Copy this block, fill it in, save it (default: temp dir; see SKILL.md Phase A step 5). Do not edit it after work starts.

```markdown
# intent-check contract v1

- Created: <ISO timestamp>
- Supersedes: none
- Baseline: <e.g. HEAD=abc1234; tests 24/24 passing via `npm test`; or "no tests found">

## Original request (verbatim)

> <paste the user's message exactly, including typos. Replace any secrets with [REDACTED]>

## Criteria

| # | Criterion | Type | How to verify |
|---|---|---|---|
| 1 | ... | Explicit | ... |
| 2 | ... | Implicit | ... |
| 3 | ... | Assumption | ... |

## Assumptions (explain each)

- A3: <what was ambiguous> → <what you chose> because <reason>.

## Out of scope (stated so it can be checked for creep)

- <files / areas the request did not mention>
```

## Rules for splitting a request

1. **One criterion = one checkable fact.** "Add a remember-me box and translate errors" is two criteria, not one.
2. **Lists become one criterion per item.** "Add A, B, C, D and E" is five explicit criteria. Missing items in long lists is the most common failure.
3. **Quantifiers are explicit criteria.** "All error messages" means every message, so the verify method must enumerate them (e.g. grep), not sample one.
4. **Always add these implicit criteria when they apply:**
   - The code builds / runs (if there is a build or run command).
   - Existing tests still pass (if tests exist). Record the baseline count.
   - Existing behaviour the request did not mention is unchanged.
   - Scope is checked separately in Phase B (scope creep list). Add "no other files changed" as a criterion only when the user said so ("only touch X", "change nothing else").
5. **Ambiguity becomes an Assumption row**, never a silent choice. Words like "nicer", "faster", "clean up", "improve", "better" always produce at least one assumption.
6. **Do not invent requirements.** If the user did not ask for it and it is not unavoidable, it is not a criterion. Adding it during work would be scope creep.
7. **Negative requirements count.** "Don't touch the API" is an explicit criterion verified with the diff.

## Examples

### Example 1: multi-item request

Request: "Add a /health endpoint that returns {status: 'ok'}, log every request, and update the README."

| # | Criterion | Type | How to verify |
|---|---|---|---|
| 1 | `GET /health` exists | Explicit | Read router file; call it in a test or local run |
| 2 | Response body is exactly `{"status":"ok"}` | Explicit | Run test / local request, compare output |
| 3 | Every request is logged | Explicit | Read middleware; run two different routes and check log output |
| 4 | README documents `/health` | Explicit | grep README for `/health` |
| 5 | Existing tests still pass | Implicit | Run test suite, compare with baseline |
| 6 | Log format/destination | Assumption | Report choice (stdout, one line per request) |

### Example 2: vague request

Request: "Make the landing page look nicer."

| # | Criterion | Type | How to verify |
|---|---|---|---|
| 1 | Landing page visual changes were made | Explicit | Diff of landing page files; before/after screenshot if possible |
| 2 | Page still renders without errors | Implicit | Build + load page; console has no new errors |
| 3 | Content/text unchanged | Implicit | Diff shows no copy changes |
| 4 | "Nicer" = consistent spacing, one font family, higher contrast | Assumption | Listed in report for the user to accept or reject |

### Example 3: negative requirement

Request: "Rename `getUser` to `fetchUser` everywhere, don't change behaviour."

| # | Criterion | Type | How to verify |
|---|---|---|---|
| 1 | No remaining `getUser` identifiers | Explicit | `grep -rn "getUser" src/` returns nothing (except intended, e.g. changelog) |
| 2 | All call sites use `fetchUser` | Explicit | grep count matches old count |
| 3 | Behaviour unchanged | Explicit | Test suite passes with same count as baseline; diff shows only renames |
| 4 | Only rename-related edits | Implicit | `git diff` hunks contain only the rename ("don't change behaviour" makes this a criterion) |
