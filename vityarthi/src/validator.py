def validate_input(value_str, name):
    # This tries to turn the user's text input into a number (float)
    try:
        value = float(value_str)
        # Check if the number is negative, which is not allowed for distance or fuel
        if value < 0:
            print(f"Error: {name} cannot be negative. Please try again.")
            return None
        # If successful, return the valid number
        return value
    # If the user typed letters instead of numbers, catch the error
    except ValueError:
        print(f"Error: Invalid input for {name}. Please enter only numbers.")
        return None

def is_fuel_zero(liters):
    # This checks if the liters input is zero to prevent crashing the program
    if liters == 0:
        print("Error: Liters of fuel used cannot be zero. Please enter a value greater than zero.")
        return True
    # If not zero, return False
    return False