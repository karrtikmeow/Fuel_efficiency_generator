def display_welcome():
    # Show a friendly welcome message when the program starts
    print("\n--- Welcome to the Modular KPL Calculator ---")
    print("This tool helps you calculate your vehicle's fuel efficiency.")

def get_user_input(prompt):
    # Takes in raw text from the user based on the question (prompt)
    return input(prompt)

def display_result(kpl_value):
    # Show the final KPL result to the user
    print(f"\n✅ Your Fuel Efficiency is: {kpl_value} KPL")

def display_goodbye():
    # Show a message when the user decides to quit the program
    print("\nThank you for using the KPL Calculator. Goodbye!")