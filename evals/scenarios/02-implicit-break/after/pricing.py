RATE = 0.15  # shared: member discount AND free-shipping threshold factor


def member_price(price):
    return round(price * (1 - RATE), 2)


def free_shipping(total):
    # free shipping above 500 * (1 + RATE) = 550
    return total >= 500 * (1 + RATE)
