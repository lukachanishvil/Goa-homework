def is_uppercase(string):
    # Check if the string consists entirely of uppercase letters
    return string.isupper()

# Example usage
string = input("Enter a string: ")

result = is_uppercase(string)

print(result)
