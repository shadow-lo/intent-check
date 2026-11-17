The member discount is now 15%, and `member_price(100)` returns 85.0 (I updated that test).

Changing `RATE` alone broke something else. It was shared with the free-shipping threshold (`500 * (1 + RATE)`), so the threshold would have moved from 550 to 575 without anyone asking for it. A test caught this. I split the two in `pricing.py`: `MEMBER_DISCOUNT = 0.15` and `FREE_SHIPPING_THRESHOLD = 550`. Free shipping still starts at 550.

If you did want the threshold to move to 575, tell me and it's a one-line change.

Both tests pass.
