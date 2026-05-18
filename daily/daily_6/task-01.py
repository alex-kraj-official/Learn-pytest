#"racecar" → True
# "hello"   → False
# "level"   → True

word = "helo"

def is_palindrome(word: str) -> bool:
    return word == word[::-1]        

print(is_palindrome(word))