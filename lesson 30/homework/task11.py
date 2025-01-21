
sentence = "I love programming in Python. Python is amazing!"


position = sentence.find("Python")


if position != -1:
    print("The word 'Python' first occurs at position:", position)
else:
    print("The word 'Python' is not found in the sentence.")
