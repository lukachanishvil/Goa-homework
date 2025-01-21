def count_word_occurrences(text, word):

    text = text.lower()
    

    count = text.split().count(word.lower())
    
    return count

text = "Python is a great programming language. Python is also easy to learn."
word = "python"
occurrences = count_word_occurrences(text, word)

print(f"The word '{word}' appears {occurrences} times in the text.")
