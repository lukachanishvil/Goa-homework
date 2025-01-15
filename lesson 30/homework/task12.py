# Ask the user for a string and a substring to search for
string = input("Enter a string: ")
substring = input("Enter the substring to search for: ")

# Find the starting index of the first occurrence of the substring
index = string.find(substring)

# Display the result
if index != -1:
    print(f"The substring '{substring}' first occurs at index:", index)
else:
    print(f"The substring '{substring}' was not found in the string.")
