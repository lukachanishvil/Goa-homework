# Ask the user for a string and a character
string = input("Enter a string: ")
character = input("Enter a character to count: ")

# Count the occurrences of the specified character in the string
count = string.count(character)

# Display the result
print(f"The character '{character}' appears {count} times in the string.")
