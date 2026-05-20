# → "Hello World Foo Bar"

def capitalize_words(words: str) -> str:
    # words_s = words.split()
    # capitalized_words = ""
    # for w in words_s:
    #     # print(type(w))
    #     cw = w.capitalize()
    #     # print(cw)
    #     capitalized_words += (" " + cw)
    # capitalized_words = capitalized_words[1:]
    # return capitalized_words

    return " ".join(w.capitalize() for w in words.split())

print(capitalize_words("hello world foo bar"))