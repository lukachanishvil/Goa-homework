def reverse_and_format(text):
    reversed_text = text[::-1]
    return f"The reverse of '{text}' is '{reversed_text}'."

result = reverse_and_format("hello")
print(result)
