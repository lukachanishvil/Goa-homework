def find_character_index(string, character):
    # Find the index of the specified character
    index = string.find(character)
    
    # Return the index or a message if the character is not found
    if index != -1:
        return index
    else:
        return f"The character '{character}' is not found in the string."

# Example usage
string = "Hello, world!"
character = 'o'
index = find_character_index(string, character)

print("Index:", index)
