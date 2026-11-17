# Verification methods

Pick the strongest method that is available and safe (read-only). Write the method into the contract in Phase A, then use it in Phase B.

## Evidence strength (strongest first)

1. **Executed check**: a command you ran in this audit, with its real output (test, build, script, request to a local server).
2. **Direct observation**: file content at a path and line, a diff hunk, a screenshot you took.
3. **Static search**: grep / find results that prove presence or absence.
4. **Nothing else counts.** Claims in the conversation, commit messages, comments in code, or "I did X" summaries are not evidence.

## By criterion kind

| Criterion kind | Method | Evidence to cite |
|---|---|---|
| Something was added (function, field, file, UI element) | Read the file; grep for it | `path:line` |
| Something was removed or renamed | grep for the old name, expect zero hits | command + "0 matches" |
| "All X" / "every X" | Enumerate all X with grep/find, check each | count checked / count total |
| Behaviour works | Run the relevant test, or run the code with a sample input | command + key output lines |
| Exact output / text | Run and compare expected vs actual | expected vs actual |
| Existing behaviour not broken | Run the full test suite, compare with baseline | `N/N passed (baseline N/N)` |
| Builds / compiles | Run the build command | command + exit code |
| UI / visual | Screenshot before and after (if a browser tool exists); otherwise read markup/CSS | screenshot name, or `path:line` with ⚠️/❓ note |
| Docs updated | grep the doc for the new term | `README.md:line` |
| "Don't touch X" | `git diff --stat` / `git diff -- X` is empty | command + empty output |
| Performance claim | Run a benchmark only if one exists in the repo; otherwise ❓ | command + numbers |
| Assumption | Not verified as true/false. Verify that the work matches the assumption you chose, and list it in the report | `path:line` |

## Scope creep check

```bash
git status --porcelain
git diff --stat <baseline>          # or: git diff --stat HEAD if work is uncommitted
```

For each changed file, name the criterion that required it. Files with no criterion are scope creep. Report them; do not silently revert them (the user decides).

If the project is not a git repo, compare against file listings or modification times you recorded at baseline, and say the check is weaker.

## When evidence cannot be collected

Mark ❓ and write why, in one line, plus what the user can run. Examples:

- "❓ Needs a real browser; no browser tool available. Run `npm run dev` and open /login."
- "❓ Test needs network access to a payment API. Not run (audit is read-only and offline)."
- "❓ No test suite exists; behaviour not executed."

## Safety limits while collecting evidence

- Run only commands that do not change state outside temp dirs: tests, builds, linters, type checkers, `git diff`, `git log`, `git status`, grep, reading files.
- Do not: install or upgrade packages, push, deploy, run migrations against real databases, delete files, send HTTP requests to non-local hosts, upload anything.
- If a test command would hit external services, do not run it; mark ❓.
- Never paste secret values into evidence. Cite `config/.env:3 (value redacted)` instead.
- Keep evidence short: the 1–5 lines that prove the point, not full logs.
