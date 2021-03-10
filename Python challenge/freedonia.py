def calculate_tax(amount, state, hour):
    percentage = {
        'Chico':    0.5,
        'Groucho':  0.7,
        'Harpo':    0.5,
        'Zeppo':    0.4
    }
    return amount + amount * percentage[state] * hour / 24