# Handling Runtime Errors
def user_input():
    try:
        number = int(input("Enter a number: "))
        print(number)
    except ValueError:
        print("Please Enter a Number")


# user_input()

def user_input_two():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Please Enter a Number")
    else:
        print(number)


# user_input_two()

def user_input_three():
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Please Enter a Number")
        else:
            break
    return number

# user_input_three()


def user_input_four():
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Please Enter a Number")
        else:
            return number


def user_input_four():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Please Enter a Number")
