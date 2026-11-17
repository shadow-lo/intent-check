def parse_age(value):
    age = int(value)
    if age < 0 or age > 150:
        raise ValueError("age out of range")
    return age
