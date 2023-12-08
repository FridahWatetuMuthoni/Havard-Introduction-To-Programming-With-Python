def main():
    number = int(input("What is your number? "))
    print(f"The square of {number} is {square(number)}")


def square(number):
    return number * number


if (__name__ == '__main__'):
    main()
