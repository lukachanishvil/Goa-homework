def capitalize_first_letter(string_list):
    
    return [string.capitalize() for string in string_list]


lowercase_strings = ['hello', 'world', 'python']
capitalized_strings = capitalize_first_letter(lowercase_strings)

print(capitalized_strings)
