data = [(1, 50), (2, 60), (1, 70), (2, 80),(3, 90), (4, 20)]

students = {}
for rollno, marks in data:
    if rollno in students:
        students[rollno] = students[rollno] + marks
    else:
        students[rollno] = marks

for rollno, total in students.items():
    print(rollno, total)
