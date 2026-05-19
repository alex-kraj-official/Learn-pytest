# swap(3, 7)  → (7, 3)
# swap(10, 5) → (5, 10)

numbers1 = (3, 7)
numbers2 = (10, 5)

def swap(numbers: tuple) -> tuple:
    return numbers[::-1]

print(swap(numbers2))