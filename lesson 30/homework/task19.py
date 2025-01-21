
string = "Hello, welcome to the world of programming. Hello again!"


index = string.lower().find("hello")


if index != -1:
    print(f"The word 'hello' first occurs at index: {index}")
else:
    print("The word 'hello' is not found in the string.")
