scores = {
    "Ron": 98,
    "Harry": 87,
    "Harmione": 86,
    "Bumblebee": 76,
    "Potty":78,
    "Micky":67,
    "Hope":89
}

for number in scores:
    print(number)
    grade = scores[number]
    if grade > 90:
        print("Outstanding")
    elif grade >= 80 and grade <90:
        print("Esceeding expectation")
    elif grade >= 70 and grade < 80:
        print("Excellent")
    else:
        print("Fail")