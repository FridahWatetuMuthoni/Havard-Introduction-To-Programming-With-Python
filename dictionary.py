# Dicts in Python

person = {
    "name": "fridah",
    "email": "fridah@gmail.com",
    "number": "012345678",
    "city": "Nairobi",
    "job": "software engineer"
}

for key, value in person.items():
    print(f"{key}:{value}")

print(person["job"])


for key in person:
    print(key, person[key], sep='->')

students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell Terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None
    },
]

print(type(students))
print(type(students[0]))

for student in students:
    print(student["name"], student["house"], student['patronus'], sep="-")
