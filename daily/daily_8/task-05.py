numbers = [3, 1, 4, 1, 5, 9, 2, 6, 9]
# → 6

def second_largest(numbers: list) -> int:
    return sorted(set(numbers), reverse = True)[1] # set kell ahhoz, hogy hogyha duplán vagy többször szerepel egy szám, akkor is helyesen adja vissza a 2. legnagyobb számot

print(second_largest(numbers))