# Simple Function that just prints something

def greeting():
    print("Hello World")


greeting()

# A function that have arguements and returns a value


def addition(num1, num2):
    return num1 + num2


result = addition(10, 20)
print(result)

# Passing Defaults to functions that can be used if the parameter is not passed


def sum(num=1):
    return num + num


print(f"Without an arguement: {sum()}")
print(f"With arguement: {sum(10)}")

# a function that accepts multiple arguements


def my_func(*args):

    if (len(args) > 0):
        for element in args:
            print(element)


my_func("anna", "jane", "emily", "jackline", "martin")

# a function that accepts multiple arguements and keyword arguements


def my_function(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

    # traversing the tuple returned from the arguements entered in the function
    if (len(args) > 0):
        for element in args:
            print(element)

    # traversing the dictonary formed from the keyword arguements
    for key, value in kwargs.items():
        print(f"{key}: {value}")


my_function("anna", "jane", "emily", "jackline", "martin",
            username="Anna", email="anna@gmail.com")
