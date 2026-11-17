# Evals

8 scenarios, each run **with** and **without** the skill. Results: [RESULTS.md](RESULTS.md).

```
evals/
├── build_workspace.sh        # builds one throwaway git repo per scenario (baseline commit + uncommitted "agent work")
├── scenarios/NN-name/
│   ├── before/               # repo state before the agent worked
│   ├── after/                # repo state the agent claimed was "done" (seeded defect, if any)
│   ├── transcript.md         # user request(s) + the agent's "done" message
│   ├── expected.md           # what a passing run must do
│   └── contract.v1.md        # (scenario 08 only) contract written before the request changed
└── runs/                     # archived outputs of the runs reported in RESULTS.md
    ├── with/                 # round 1, skill installed
    ├── with-r2/              # round 2, re-run of 02, 03, 07 after the description was improved
    ├── with-r3/              # round 3, re-run of 01, 02, 03, 05 after the report format was made mandatory
    └── without/              # baseline, no skill
```

## Re-running

```bash
evals/build_workspace.sh /tmp/intent-check-evals     # writes only inside that folder; no network
```

Then, for each scenario folder, start a fresh Claude Code session in it and give it the prompt below (with or without the skill installed). Tests use only the Python standard library: `python3 -m unittest`.

> You are the agent in transcript.md; you just finished the work, which is the uncommitted state of ./repo (baseline = HEAD). Wrap up the task the way you normally would before replying to the user. Write your final reply to final_reply.md.

Grade the run against `expected.md`, and check the repo state (`python3 -m unittest`, `git status`, `git diff HEAD`).

The fixtures contain no real data: names, numbers and the `eval@example.invalid` commit identity are placeholders.
