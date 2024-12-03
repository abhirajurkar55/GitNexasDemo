

# emails=['abhi@gmail.com','abhilash@gmail.com','abhilashrajurkar@gmail.com','abhi@hotmail.com','abhi@yahoo.com','abhi@hotmail.com','abhiR@yahoo.com']
# for email in emails:
#     if email.endswith('@yahoo.com'):
#         print(email)
        
    



# Dictionary to store user accounts (username: {password, email})
user_accounts = {}

# Predefined destinations and prices
destinations = {
    "New York": 300,
    "Los Angeles": 500,
    "Chicago": 400,
    "Houston": 350,
    "Miami": 450
}

def create_account():
    print("Create a New Account")
    
    while True:
        username = input("Enter a username: ")
        if username in user_accounts:
            print("Username already exists. Please choose a different username.")
        else:
            break
    
    password = input("Enter a password: ")
    email = input("Enter your email: ")
    
    # Store the account details
    user_accounts[username] = {
        "password": password,
        "email": email
    }
    
    print(f"Account created successfully for username: {username}!\n")

def login():
    print("Login to Your Account")
    
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if username in user_accounts and user_accounts[username]["password"] == password:
            print(f"Login successful! Welcome, {username}!\n")
            return username
        else:
            print("Invalid username or password. Please try again.")

def select_destination():
    print("Available Destinations:")
    for index, (destination, price) in enumerate(destinations.items(), start=1):
        print(f"{index}. {destination} - ${price}")
    
    while True:
        try:
            choice = int(input("Select a destination by entering the corresponding number: "))
            if 1 <= choice <= len(destinations):
                selected_destination = list(destinations.keys())[choice - 1]
                selected_price = destinations[selected_destination]
                return selected_destination, selected_price
            else:
                print("Invalid choice. Please select a valid destination number.")
        except ValueError:
            print("Please enter a valid number.")

def enter_passenger_details():
    print("Enter Passenger Details:")
    passenger_name = input("Enter passenger name: ")
    passenger_age = input("Enter passenger age: ")
    passenger_gender = input("Enter passenger gender (M/F): ")
    return passenger_name, passenger_age, passenger_gender

def confirm_booking(username, destination, price, passenger_details):
    print("\nBooking Details:")
    print(f"Username: {username}")
    print(f"Destination: {destination}")
    print(f"Total Price: ${price}")
    print("Passenger Details:")
    print(f"Name: {passenger_details[0]}")
    print(f"Age: {passenger_details[1]}")
    print(f"Gender: {passenger_details[2]}")
    
    confirm = input("Do you want to confirm your booking? (yes/no): ").strip().lower()
    if confirm == 'yes':
        print("Booking confirmed! Thank you for using our service.\n")
    else:
        print("Booking canceled.\n")

def main():
    while True:
        print("Welcome to the Flight Booking System!")
        print("1. Create a New Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            create_account()
        elif choice == '2':
            username = login()
            if username:
                destination, price = select_destination()
                passenger_details = enter_passenger_details()
                confirm_booking(username, destination, price, passenger_details)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()