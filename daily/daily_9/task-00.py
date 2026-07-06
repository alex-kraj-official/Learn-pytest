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

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 42},
    {"name": "Carol", "grade": 91},
    {"name": "Dave", "grade": 58},
    {"name": "Eve", "grade": 60},
]

# ["Alice", "Carol", "Eve"]

def get_passing_students(students: dict) -> list:
    return [s["name"] for s in students if s["grade"] >= 60]

print(get_passing_students(students))
