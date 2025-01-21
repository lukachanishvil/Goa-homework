def replace_spaces_with_underscores(string):
    
    return string.replace(" ", "_")


input_string = input("Enter a string: ")
modified_string = replace_spaces_with_underscores(input_string)

print("Modified string:", modified_string)
