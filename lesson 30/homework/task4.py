def convert_to_uppercase(string_list):
    # Convert each string in the list to uppercase
    return [string.upper() for string in string_list]

# Example usage
lowercase_strings = ['hello', 'world', 'python']
uppercase_strings = convert_to_uppercase(lowercase_strings)

print(uppercase_strings)
