def count_the_occurrences(paragraph):
    
    paragraph = paragraph.lower()
    
    
    count = paragraph.split().count("the")
    
    return count


paragraph = "The quick brown fox jumps over the lazy dog. The dog is not happy."
occurrences = count_the_occurrences(paragraph)

print("The word 'the' appears", occurrences, "times in the paragraph.")
