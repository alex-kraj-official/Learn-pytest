text = "apple banana apple orange banana apple"

def count_words(text: str) -> dict:
    text_split = text.split()
    words_stat = {}
    for word in text_split:
        if word not in words_stat:
            words_stat[word] = 0
        words_stat[word] += 1
    return words_stat

print(count_words(text))
# {"apple": 3, "banana": 2, "orange": 1}