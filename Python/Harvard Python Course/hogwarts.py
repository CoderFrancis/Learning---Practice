students = ["Hermione", "Harry", "Ron"]

# this command will list the names in students
for student in students:
    print(student)

# this command adds in the index or a number to the corresponding student name
for i in range(len(students)):
    print(i + 1, students[i])