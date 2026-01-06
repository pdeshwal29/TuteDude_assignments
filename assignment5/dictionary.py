import re

students = {
    "Akash": 85,
    "Priya": 78,
    "Rohan": 92
}

name = input("Enter the student's name: ")

found = False

for student in students:
    if re.fullmatch(name, student, re.IGNORECASE):
        print(f"{student}'s marks: {students[student]}")
        found = True
        break

if not found:
    print("Student not found.")