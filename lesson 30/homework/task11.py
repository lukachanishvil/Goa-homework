# Input sentence
sentence = "I love programming in Python. Python is amazing!"

# Find the position of the first occurrence of the word "Python"
position = sentence.find("Python")

# Display the result
if position != -1:
    print("The word 'Python' first occurs at position:", position)
else:
    print("The word 'Python' is not found in the sentence.")
