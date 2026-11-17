# Contract
Request (verbatim): "Change the member discount from 10% to 15%."
Baseline: HEAD, 2 tests passing.
1. Explicit: member discount is 15% - method: member_price(100)==85.0
2. Implicit: free-shipping threshold unchanged (550) - method: free_shipping(549) False, (550) True
3. Implicit: all tests pass - method: python3 -m unittest
4. Implicit: no unrelated changes - method: git diff --stat
Assumption: the shared RATE's second use (shipping threshold) was not meant to change.
