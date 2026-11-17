Member discount is now 15%: `member_price(100)` returns 85.0, and I updated that test.

One thing you didn't mention: `RATE` was shared with the free-shipping threshold. Changing it to 0.15 would have moved that threshold from 550 to 575, and the existing free-shipping test failed. I split it into `MEMBER_DISCOUNT = 0.15` and `FREE_SHIPPING_FACTOR = 0.10`, so the threshold stays at 550. I did not see a request to change it. If you did want it to change, tell me.

`python3 -m unittest`: 2 tests, both pass. Changed files: `pricing.py`, `test_pricing.py`.
