numbers = [3, 1, 2, 3, 4, 1, 5]
# → [3, 1, 2, 4, 5]

def remove_duplicates(numbers: list) -> list:
    cleaned_numbers = []
    for n in numbers:
        if n not in cleaned_numbers:
            cleaned_numbers.append(n)
    return cleaned_numbers
    # return [n for n in numbers if n not in cleaned_numbers]

print(remove_duplicates(numbers))