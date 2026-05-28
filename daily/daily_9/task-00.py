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