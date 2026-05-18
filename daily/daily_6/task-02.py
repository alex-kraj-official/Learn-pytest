numbers = [1, 2, 3, 2, 4, 3, 5]
# [2, 3]

def find_duplicates(numbers: list) -> list:
    duplicates = set()
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
        else:
            duplicates.add(num)
    return duplicates

print(find_duplicates(numbers))