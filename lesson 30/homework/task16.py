def count_the_occurrences(paragraph):
    # Convert the paragraph to lowercase to ensure case-insensitive matching
    paragraph = paragraph.lower()
    
    # Count the occurrences of the word "the"
    count = paragraph.split().count("the")
    
    return count

# Example usage
paragraph = "The quick brown fox jumps over the lazy dog. The dog is not happy."
occurrences = count_the_occurrences(paragraph)

print("The word 'the' appears", occurrences, "times in the paragraph.")
