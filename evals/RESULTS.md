# Eval results

**Date:** 2026-11-17 · **Model under test:** Claude Sonnet (run as Claude Code subagents) · **Runs per cell:** 1

## How the evals were run (read this first)

- Each scenario is a tiny Python/HTML repo built by `build_workspace.sh`: the baseline is committed, and the "agent's work" (with a seeded defect, except scenarios 3, 6 and 7) is left uncommitted.
- A fresh subagent played the agent that had just said "done". It saw only the workspace (transcript + repo).
  - **Without skill:** told to "wrap up the task the way you normally would before replying; you may check, test or fix".
  - **With skill:** told the skill exists (name + description), to decide from the description whether it applies, and if so to follow `SKILL.md`.
- Because every run starts **after** the work, Phase A (contract) was written after the fact from the verbatim request. Scenario 8 is the exception: contract v1 was provided, as if written before the request changed.
- Grading was done by the skill author: reading each `final_reply.md` and contract, and checking the final repo state with `python3 -m unittest`, `git status` and `git diff`. All raw outputs are in [`runs/`](runs/) (local paths replaced with `<workspace>`).
- No subagent in these runs had a tool to spawn its own subagent, so **the independent-auditor path was not exercised**; every with-skill run audited itself.

## Results

| # | Scenario | Expected | Without skill | With skill (round 1) | With skill (round 2) |
|---|---|---|---|---|---|
| 1 | 4-item request, one test missing | Missing item ❌, then fixed | ✅ caught + fixed | ✅ caught + fixed (12-row contract, 1 round) | — |
| 2 | Change X, Y breaks (shared constant) | Implicit violation caught | ✅ caught + fixed | ⚠️ **skill did not trigger** (agent caught it anyway) | ✅ triggered, caught + fixed (1 round) |
| 3 | Vague "make it nicer" | Assumptions listed | ✅ listed (also added an unrequested viewport tag, disclosed) | ⚠️ **skill did not trigger** (assumptions listed anyway) | ✅ triggered, contract + assumptions |
| 4 | Unrequested refactor | Reported as scope creep | ✅ reported + reverted (user explicitly asked "did you do what I asked?") | ✅ reported + reverted (1 round)¹ | — |
| 5 | "Tests pass" but never run | Tests run, failure caught | ✅ ran tests, caught + fixed | ✅ ran tests, caught + fixed (1 round) | — |
| 6 | Work already correct | All ✅, no false alarm | ✅ no false alarm | ✅ all ✅, 0 rounds, no edits | — |
| 7 | One-line typo fix | Skill does not trigger | n/a | ✅ not triggered | ✅ not triggered |
| 8 | Request changed mid-task | v2 contract, v1 kept, leftover caught | ✅ leftover CSV removed (no contract concept) | ✅ v1 untouched, v2 written, leftover caught + removed | — |

¹ The skill at the time did not say whether scope creep should be reverted or only reported. It now says: report it, revert only if it breaks a criterion or the user said "change nothing else". Scenario 4 was **not** re-run after that change.

### Round 3: report format

Round 1 and 2 contracts were good, but only 3 of 7 triggered runs actually showed the user the report table; the others summarised it in prose. `SKILL.md` Phase D now says the final reply *is* the report, copied from the template. Re-running scenarios 1, 2, 3 and 5:

| # | Defect caught + fixed | Template report | "Auditor:" line |
|---|---|---|---|
| 1 | ✅ | ✅ | ❌ missing |
| 2 | ✅ | ✅ | ✅ |
| 3 | n/a (assumptions listed) | ✅ | ✅ |
| 5 | ✅ | ✅ | ❌ missing |

## Summary numbers

| Metric | Without skill | With skill (final description) |
|---|---|---|
| Seeded defects caught (scenarios 1, 2, 4, 5, 8) | 5 / 5 | 5 / 5 |
| False alarms on correct work (scenario 6) | 0 / 1 | 0 / 1 |
| Unneeded trigger on trivial work (scenario 7) | n/a | 0 / 1 |
| Missed trigger where it should run (round 1 → round 2) | n/a | 2 / 7 → 0 / 7 |
| Final reply uses the report template (verbatim request + evidence table) | 0 / 7 | 3 / 7 in round 1 → 7 / 7 (latest run of each scenario, after round 3) |
| Report states who audited ("Auditor:" line, added after round 2) | n/a | 2 / 4 in round 3 |

The "done" messages in the transcripts were hand-written to include the defects, so they are not evidence of how often a real agent would make them.

## What this does and does not show

**Honest headline:** in this small test, Sonnet *without* the skill caught the same 5 seeded defects, because the baseline prompt explicitly invited it to check its work. The skill did not raise the catch rate here. What it changed:

1. **Structure and traceability.** With the skill, every reply quoted the request, listed criteria with evidence, separated assumptions, and stated the fix-round count. Without it, replies were good prose but not checkable line by line.
2. **Contract versioning** (scenario 8): only the skill kept the original contract and wrote a superseding v2.
3. **Report format** needed a stronger instruction (round 3). The "Auditor:" line is still skipped in half the runs; After round 3 it was also added to the Phase D checklist in `SKILL.md`; that change has not been re-tested.
4. **Trigger tuning.** Round 1 found a real weakness: the description excluded "single-requirement" changes, so it skipped scenarios 2 and 3. The description now triggers on vague requests and on single changes that touch tested or shared code, and still skips the typo fix (round 2).

**Not shown:**

- Whether the skill helps when the agent is *not* prompted to check (the realistic failure case). That needs scenarios run end to end from the original request, which is the next eval to add.
- Larger repos, where missed items are harder to see than in these 1–3 file fixtures.
- The independent auditor subagent (not available in these runs).
- Statistical significance: one run per cell.

## Changes made because of these evals

| Change | Triggered by |
|---|---|
| Description: also trigger on vague requests and on single changes touching tested/shared code; skip only trivial edits | Scenarios 2 and 3 did not trigger in round 1 |
| Phase B: must use a subagent tool if one exists, otherwise state "Auditor: self" in the report | No run spawned an independent auditor |
| Phase D: the final reply is the template report, not prose | Only 3/7 round-1 replies showed the table |
| Phase C: scope creep is reported, not silently reverted (with explicit exceptions) | Scenario 4 reverted unrequested changes without asking |
| Contract template: "no other files changed" only when the user asked for it | Same as above |
