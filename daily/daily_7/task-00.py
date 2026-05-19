numbers = [1, 3, 2, 3, 4, 3, 2, 1, 3]

# 3

def most_common(numbers: list) -> int:
    count_elements = {}
    for num in numbers:
        if num not in count_elements:
            count_elements[num] = 0
        count_elements[num] += 1
    return max(count_elements, key=lambda x: count_elements[x])

print(most_common(numbers))

# lambda x: valami(x)
# # ugyanaz mint:
# def névtelen(x):
#     return valami(x)