def print_something(n, str):
    i = 0
    while (i < n):
        print(str)
        i += 1


print_something(3, "meow")


print("Back\n" * 3, end="")


def user_input():
    while True:
        number = int(input("Enter a positive Number: "))
        if (number > 0):
            break
    for i in range(number):
        print("Meow")


user_input()
