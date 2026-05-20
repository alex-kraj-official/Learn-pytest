numbers = [1, 2, 4, 6, 7, 9, 10]

def find_missing_numbers(numbers: list) -> list:
    missing_numbers = []
    for n in range(1,max(numbers)+1,1):
        if n not in numbers:
            missing_numbers.append(n)
    return missing_numbers

print(find_missing_numbers(numbers))