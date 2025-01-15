def replace_spaces_with_underscores(string):
    # Replace all spaces with underscores
    return string.replace(" ", "_")

# Example usage
input_string = input("Enter a string: ")
modified_string = replace_spaces_with_underscores(input_string)

print("Modified string:", modified_string)
