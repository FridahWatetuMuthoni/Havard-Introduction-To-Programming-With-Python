def reading_csv_file():
    file_path = "./Files/students.csv"
    with open(file_path) as file:
        for line in file:
            name, house = line.rstrip().split(",")
            print(f"Name: {name}, House: {house}")


# reading_csv_file()

def get_student_name(student):
    return student["name"]


def sorting_csv_file():
    students = []
    file_path = "./Files/students.csv"
    with open(file_path) as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append({"name": name, "house": house})
    sorted_students = []
    for student in sorted(students, key=get_student_name):
        sorted_students.append(student)
    return sorted_students


# print(sorting_csv_file())

# Using a lamdba function as an arguement to another function

def sorting_names_csv():
    students = []
    file_path = "./Files/students.csv"
    with open(file_path) as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append({"name": name, "house": house})
    sorted_students = []
    # Using a lambda function
    for student in sorted(students, key=lambda student: student["name"]):
        sorted_students.append(student)
    return sorted_students


print(sorting_names_csv())
