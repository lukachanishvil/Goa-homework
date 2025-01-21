def find_character_index(string, character):
    
    index = string.find(character)
    
    
    if index != -1:
        return index
    else:
        return f"The character '{character}' is not found in the string."


string = "Hello, world!"
character = 'o'
index = find_character_index(string, character)

print("Index:", index)
