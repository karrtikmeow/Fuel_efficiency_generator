def calculate_kpl(kilometers, liters):
    # This function calculates Kilometers Per Liter (KPL)
    # KPL is the distance driven divided by the fuel used.
    kpl = kilometers / liters
    # Round the final result to 2 decimal places for neatness
    return round(kpl, 2)