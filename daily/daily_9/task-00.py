nested = {
    "user": {"name": "Alice", "age": 25},
    "location": {"city": "Budapest", "country": "Hungary"}
}

def flatten_dict(nested):
    unnested = {}
    for key, value in nested.items():
        for inner_key, inner_value in value.items():
            unnested[inner_key] = inner_value
    return unnested

print(flatten_dict(nested))