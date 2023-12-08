people = ['anna', 'mary', 'jane', 'annay', 'jlo']


for index, value in enumerate(people):
    print(f"People[{index}]: {value}")


numbers = [1, 2, 3, 4, 5, 6]

for index, value in enumerate(numbers):
    numbers[index] = value * 2

print(numbers)


students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

for index in range(len(students)):
    print(index + 1, students[index])
