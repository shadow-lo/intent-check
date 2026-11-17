# Report template

Keep the report short. Facts only, no praise, no filler.

```markdown
## intent-check report

**Request:** "<verbatim request, shortened with … only if longer than ~3 lines>"
**Contract:** v<N><, replaced v1 because the user changed the request at "<quote>">

| # | Criterion | Type | Result | Evidence |
|---|---|---|---|---|
| 1 | ... | Explicit | ✅ | src/login.html:42 |
| 2 | ... | Implicit | ✅ | `npm test` → 24/24 passed (baseline 24/24) |
| 3 | ... | Explicit | ❌ → ✅ | Round 1: 2 messages still English; fixed, grep finds 0 |
| 4 | ... | Explicit | ❓ | Needs a browser; run `npm run dev` and open /login |

**Assumptions:** <list, or "None">
**Decisions needed from you:** <list, or "None">
**Scope creep:** <list of unrequested changes, or "None">
**Fix rounds:** <0–3>
**Auditor:** <independent subagent | self, no subagent tool>
**Status:** <one line, see below>
```

## Status line rules

- Every row ✅ → `All criteria met.`
- Any ❓, none ❌/⚠️ → `Met where verifiable; N item(s) could not be verified (see ❓).`
- Any ❌ or ⚠️ after 3 rounds → `Not done: N criteria still open after 3 fix rounds.` Never write "done" or "complete" in this case.

## Writing rules

- Evidence column: a path:line, or a command → result. Max one short line.
- Show history: `❌ → ✅`, `⚠️ → ❌`.
- Redact secrets: `[REDACTED]`.
- Use the user's language for the report text if they wrote in another language; keep the table structure.
- Do not include full logs, full diffs, or file contents.
