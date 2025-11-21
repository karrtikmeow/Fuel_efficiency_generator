def main():
    print("Welcome to the KPL Calculator")
    
    #loop variable
    keep_going = True
    
    while keep_going:

        print("")

        #take inputs from user
        km_input = input("Enter the number of kilometers driven: ")
        liters_input = input("Enter the liters of petrol/Diesel used: ")
        

        try:
            #to convert string into decimal
            km = float(km_input)
            liters = float(liters_input)
            
            #for checking zero error
            if liters == 0:
                print("Liters cannot be zero.")
            else:
                kpl = km / liters
                print("Your fuel efficiency is: " + str(round(kpl, 2)) + " KPL")

             #incase they type letters   
        except:
            print("Error: Please enter valid numbers.")
            
        user_choice = input("Do you want to calculate again? (yes/no): ")
        
        if user_choice != "yes":
            keep_going = False
            print("Goodbye")

if __name__ == "__main__":
    main()