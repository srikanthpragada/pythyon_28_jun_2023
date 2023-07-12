data = [(1, 50), (2, 60), (1, 70), (2, 80),(3, 90), (4, 20)]

students = {}
for rollno, marks in data:
      lst = students.get(rollno,[])
      lst.append(marks)
      if rollno not in students:
        students[rollno] = lst

for rollno, marks in students.items():
    print(rollno, marks)
