def find_character_index(string, character):
    
    index = string.find(character)
    
    
    if index != -1:
        return index
    else:
        return f"The character '{character}' is not found in the string."


string = input("Enter a string: ")
character = input("Enter a character to find: ")

index = find_character_index(string, character)

print(index)
