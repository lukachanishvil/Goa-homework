def capitalize_first_letter(string_list):
    # Capitalize the first letter of each string in the list
    return [string.capitalize() for string in string_list]

# Example usage
lowercase_strings = ['hello', 'world', 'python']
capitalized_strings = capitalize_first_letter(lowercase_strings)

print(capitalized_strings)
