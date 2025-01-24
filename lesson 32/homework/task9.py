def paragraph_to_sentences(paragraph):
    return [sentence.strip() for sentence in paragraph.split(".") if sentence.strip()]


paragraph = "Python is a great language. It is versatile and powerful. Many people love it."
sentences = paragraph_to_sentences(paragraph)
print(sentences)
