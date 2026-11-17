The member discount is now 15%, and the tests pass (2 of 2).

One thing the first attempt missed: `RATE` was shared with the free-shipping threshold. Changing it to 0.15 also moved that threshold from 550 to 575, and the shipping test failed. I split it into two constants:
- `MEMBER_DISCOUNT = 0.15` drives `member_price`.
- `SHIPPING_RATE = 0.10` keeps the free-shipping threshold at 550.

I also updated the member price test to expect 85.0.

Assumption: you only wanted the discount to change, not the shipping threshold. If you wanted the threshold to move with it, tell me.
