# Correct password
correct_password = "Goa best"
# Counter for incorrect attempts
incorrect_count = 0

# Loop until the correct password is entered
while True:
    # Ask the user for the password
    entered_password = input("Enter the password: ")
    
    # Check if the password is correct
    if entered_password == correct_password:
        print("Access granted!")
        break  # Exit the loop
    else:
        incorrect_count += 1
        print("Incorrect password. Try again.")

# Print the count of incorrect attempts
print(f"Number of incorrect attempts: {incorrect_count}")
