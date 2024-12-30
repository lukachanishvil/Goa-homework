# Input two numbers from the user
num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))

# Variable to store the sum of all printed numbers
total_sum = 0

if num1 > num2:
    # If num1 is greater, print even numbers from num2 to num1 (inclusive)
    for number in range(num2, num1 + 1):
        if number % 2 == 0:
            print(number)
            total_sum += number
else:
    # If num2 is greater, print odd numbers from num1 to num2 (inclusive)
    for number in range(num1, num2 + 1):
        if number % 2 != 0:
            print(number)
            total_sum += number

# Print the sum of all printed numbers
print("The sum of all printed numbers is:", total_sum)
