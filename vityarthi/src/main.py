# Import all the necessary functions from the other project files
# We remove the leading dot (.) so the script runs correctly when executed directly.
from calculator import calculate_kpl
from validator import validate_input, is_fuel_zero
from io_handler import display_welcome, get_user_input, display_result, display_goodbye

def run_calculation_session():
    # This function handles one single cycle of the calculation
    
    # 1. Loop until a valid kilometer input is receiveed
    while True:
        km_input_str = get_user_input("Enter the number of kilometers driven: ")
        kilometers = validate_input(km_input_str, "Kilometers")
        # If validation passes (kilometers is not None), exit the loop.
        if kilometers is not None:
            break

    # 2. Loop until a valid and non-zero liter input is received
    while True:
        liters_input_str = get_user_input("Enter the liters of petrol/Diesel used: ")
        liters = validate_input(liters_input_str, "Liters")
        
        # If the input is a valid number
        if liters is not None:
            # Check if the fuel is zero
            if not is_fuel_zero(liters):
                break # Valid non-zero input, so exit the loop
            # If fuel is zero, the loop repeats
    
    # 3. Use the calculated numbres to get KPL
    kpl = calculate_kpl(kilometers, liters)
    
    # 4. Show the final result
    display_result(kpl)


def main():
    # This is the main starting functioon of the program
    display_welcome()
    
    # Set a variable to control the loop
    keep_going = True
    
    # Start the continuous loop
    while keep_going:
        
        # Run the single calculation session
        run_calculation_session()
        
        # Ask the user if they want to calculate once again
        user_choice = get_user_input("\nDo you want to calculate again? (yes/no): ").lower()
        
        # If the user types anything other than "yes", stop the loop
        if user_choice != "yes":
            keep_going = False
    
    display_goodbye()

# Standard Python way is to run the main function when the script is executedd
if __name__ == "__main__":
    main()
