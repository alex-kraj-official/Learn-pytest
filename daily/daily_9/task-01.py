students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 42},
    {"name": "Carol", "grade": 91},
    {"name": "Dave", "grade": 58},
    {"name": "Eve", "grade": 73},
]

# {
#     "excellent": ["Carol"],
#     "good": ["Alice", "Eve"],
#     "average": ["Dave"],
#     "failing": ["Bob"]
# }

def group_by_grade(students: dict) -> dict:
    excellent_students = [s["name"] for s in students if s["grade"] >= 90]
    good_students = [s["name"] for s in students if 70 <= s["grade"] <= 89]
    average_students = [s["name"] for s in students if 50 <= s["grade"] <= 69]
    failing_students = [s["name"] for s in students if s["grade"] < 50]
    
    students_stats = {
        "excellent": excellent_students,
        "good": good_students,
        "average": average_students,
        "failing": failing_students
    }

    return students_stats

print(group_by_grade(students))