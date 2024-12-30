# Input: Taking two integers from the user
start = int(input("Enter the starting integer: "))
end = int(input("Enter the ending integer: "))

# Initialize the sum
total_sum = 0

# Use a loop to calculate the sum
for num in range(start, end + 1):
    total_sum += num

# Output: Print the sum
print(f"The sum of numbers between {start} and {end} is: {total_sum}")
