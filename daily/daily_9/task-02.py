students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 42},
    {"name": "Carol", "grade": 91},
    {"name": "Dave", "grade": 58},
    {"name": "Eve", "grade": 73},
]

# ["Carol", "Alice", "Eve"]

def top_students(students: dict) -> list:
    top_3_students = []
    top_3_students.append(sorted(set(s["grade"] for s in students), reverse = True)[0])
    return top_3_students

print(top_students(students))