def count_word_occurrences(text, word):
    # Convert the text to lowercase for case-insensitive matching
    text = text.lower()
    
    # Count the occurrences of the word in the text
    count = text.split().count(word.lower())
    
    return count

# Example usage
text = "Python is a great programming language. Python is also easy to learn."
word = "python"
occurrences = count_word_occurrences(text, word)

print(f"The word '{word}' appears {occurrences} times in the text.")
