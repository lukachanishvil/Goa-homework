
string = input("Enter a string: ")
substring = input("Enter the substring to search for: ")


index = string.find(substring)


if index != -1:
    print(f"The substring '{substring}' first occurs at index:", index)
else:
    print(f"The substring '{substring}' was not found in the string.")
