scores = {
    "Ron": 98,
    "Harry": 87,
    "Harmione": 86,
    "Bumblebee": 76,
    "Potty":78,
    "Micky":67,
    "Hope":89
}

student_grades = {}

for student in scores:
    score = scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeding Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)