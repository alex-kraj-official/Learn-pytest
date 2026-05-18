def caesar_cipher(word: str, shift_num: int) -> str:
    shifted_word = ""
    for ch in word:
        shifted_ch = (ord(ch) - ord('a') + shift_num) % 26 + ord('a')
        shifted_word += chr(shifted_ch)
    return shifted_word

print(caesar_cipher("xyz", 3))