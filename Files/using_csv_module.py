import csv

# csv library is used to read and write csv files


def reading_csv_file():
    students = []
    file_path = "./Files/students.csv"
    with open(file_path) as file:
        reader = csv.reader(file)
        for name, house in reader:
            students.append({"name": name, "house": house})
    for student in students:
        print(student)


# reading_csv_file()


def csv_file_reader():
    students = []
    file_path = "./Files/data.csv"
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for line in reader:
            students.append(line)
    print(students)


csv_file_reader()


def get_user_data():
    while True:
        name = input("What is your name: ")
        home = input("What's your home: ")
        if (name and home):
            return name, home


def writing_csv_file():
    file_path = "./Files/data_2.csv"
    name, home = get_user_data()
    with open(file_path, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([name, home])


def writing_csv_dict_file():
    file_path = "./Files/data_2.csv"
    name, home = get_user_data()
    with open(file_path, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})


writing_csv_dict_file()
