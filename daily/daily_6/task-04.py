nested = [1, [2, 3], [4, [5, 6]], 7]

# [1, 2, 3, 4, 5, 6, 7]

def flatten(nested: list) -> list:
    one_dim_list = []
    for e in nested:
        if isinstance(e, list):
            one_dim_list += flatten(e)
        else:
            one_dim_list.append(e)
    return one_dim_list

print(flatten(nested))