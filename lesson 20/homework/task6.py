# Input: Taking a number from the user
number = int(input("Enter a number: "))

# Check if the number is prime
if number <= 1:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):  # Loop from 2 to square root of the number
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

