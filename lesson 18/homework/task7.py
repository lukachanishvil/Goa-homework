# Loop to get 5 numbers from the user
for i in range(5):
    # Input a number from the user
    number = int(input(f"Enter number {i + 1}: "))
    
    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
