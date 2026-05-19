dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 4}

# {"a": 1, "b": 20, "c": 3, "d": 4}

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    merged_dicts = dict1.copy()
    merged_dicts.update(dict2)
    return merged_dicts

print(merge_dicts(dict1, dict2))

def merge_dicts2(dict1: dict, dict2: dict) -> dict:
    return dict1 | dict2
# A | operátor dict-eknél összevonást jelent Python 3.9+ óta

print(merge_dicts2(dict1, dict2))