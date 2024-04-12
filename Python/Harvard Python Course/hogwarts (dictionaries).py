students = ["Hermione", "Harry", "Ron"]

# this command will list the names in students
for student in students:
    print(student)

# this command adds in the index or a number to the corresponding student name
for i in range(len(students)):
    print(i + 1, students[i])

# successfully appended my name into the code
# students.append("Mikhail")
# print(students)

# dictionaries includes key-value pairs
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

# inputting a dictionary into a list
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
