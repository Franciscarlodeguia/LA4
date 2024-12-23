def register_user():
    # Create a dictionary to store user information
    user_info = {}
    
    # Collect user information through input prompts
    # input your First name
    user_info['first_name'] = input("Enter First Name: ")
    #input your Last Name
    user_info['last_name'] = input("Enter Last Name: ")
    #enter your course
    user_info['course'] = input("Enter Course: ")
    #enter your year
    user_info['year_level'] = input("Enter Year Level: ")
    #enter you section
    user_info['section'] = input("Enter Section: ")
    #enter your username
    user_info['userName'] = input("Enter Username: ")
    #enter your password
    user_info['password'] = input("Enter Password: ")
    
    # Collect pin code with a maximum length check
  #while statement
    while True:
        pin_code = input("Enter Pin Code (max 8 characters): ")
        #if statement
        if len(pin_code) <= 8:  # Check if the pin code length is valid
            user_info['pinCode'] = pin_code  # Store the pin code
            break  # Exit the loop if the pin code is valid
            #else statement
        else:
            print("Pin Code must be a maximum of 8 characters. Please try again.")
    
    # Congratulate the user upon successful registration
    print("Congratulations! You have successfully registered.")
    return user_info  # Return the user information dictionary

def login_user(user_info):
    # Loop to allow multiple login attempts
    while True:
        # Prompt for username and password
        #enter your username
        username_input = input("Enter Username: ")
       #eneter your password
         password_input = input("Enter Password: ")
        
        # Check if the entered username and password match the registered ones
        if username_input == user_info['userName'] and password_input == user_info['password']:
            # If authentication is successful, prompt for pin code
            while True:
                pin_code_input = input("Enter Pin Code: ")
                
                # Check if the entered pin code matches the registered one
                if pin_code_input == user_info['pinCode']:
                    # If pin code is correct, display registered information
                    #print if you log in succesful
                    print("Login successful! Here is your registered information:")
                    #print your first name
                    print(f"First Name: {user_info['first_name']}")
                    #print your last name
                    print(f"Last Name: {user_info['last_name']}")
                    #print your course
                    print(f"Course: {user_info['course']}")
                 #print your year
                       print(f"Year Level: {user_info['year_level']}")
                       #print your section
                    print(f"Section: {user_info['section']}")
                    return  # Exit the login function
                else:
                    print("Incorrect Pin Code. Please try again.")  # Prompt for pin code again
        else:
            print("Incorrect Username or Password. Please try again.")  # Prompt for credentials again

def main():
    # Start the registration process
    user_info = register_user()
    
    # Loop to ask if the user wants to log in
    while True:
        login_choice = input("Do you want to log in? (YES/NO): ").strip().upper()
        
        if login_choice == 'YES':
            # If the user wants to log in, call the login function
            login_user(user_info)
        elif login_choice == 'NO':
            # If the user does not want to log in, exit the program
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter YES or NO.")  # Handle invalid input

# Entry point of the program
if __name__ == "__main__":
    main()