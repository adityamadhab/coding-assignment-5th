def sort_students_by_marks(students):
    return sorted(students, key=lambda x: x['marks'], reverse=True)

students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78},
    {"name": "David", "marks": 88}
]

sorted_students = sort_students_by_marks(students)
for student in sorted_students:
    print(student)
