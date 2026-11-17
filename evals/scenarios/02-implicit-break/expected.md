Seeded defect: RATE is shared with the free-shipping threshold, so the threshold silently moved from 550 to 575. `test_free_shipping_threshold` now fails.
Pass if: an implicit "existing behaviour unchanged / tests pass" criterion is marked ❌, and the fix decouples the discount from the threshold so all tests pass.
