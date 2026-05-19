words = ("hello world foo bar")
# → "bar foo world hello"

def reverse_words(words: str) -> str:
    word_splitted = words.split(" ")
    return " ".join(word_splitted[::-1])

print(reverse_words(words))