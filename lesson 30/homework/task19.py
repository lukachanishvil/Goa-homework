# Input string
string = "Hello, welcome to the world of programming. Hello again!"

# Find the index of the first occurrence of the word "hello"
index = string.lower().find("hello")

# Display the result
if index != -1:
    print(f"The word 'hello' first occurs at index: {index}")
else:
    print("The word 'hello' is not found in the string.")
